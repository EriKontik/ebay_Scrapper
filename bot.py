from playwright.sync_api import sync_playwright
import globalfunctions as globalfunctions
import time 
import random
links_to_categories = [
    "https://www.ebay.com/globaldeals/home/more-home-garden",
    "https://www.ebay.com/globaldeals/featured/lifestyle",
    "https://www.ebay.com/globaldeals/more/business-industrial",
    "https://www.ebay.com/globaldeals/more/automotive",
    "https://www.ebay.com/globaldeals/tech/video-games-consoles",
    "https://www.ebay.com/globaldeals/featured/fashion",
    "https://www.ebay.com/globaldeals/fashion/mens-shoes-accessories",
    "https://www.ebay.com/globaldeals/featured/electronics"
]

def human_delay(min_ms=500, max_ms=1500):
    """Adds a random sleep to mimic human hesitation."""
    time.sleep(random.randint(min_ms, max_ms) / 1000)

import random
import time
import json
import csv
from playwright.sync_api import sync_playwright
import globalfunctions as globalfunctions

# ... (links_to_categories and human_delay remain the same)

def main_ebay():
    all_products = []
    
    with sync_playwright() as p:
        browser = p.chromium.launch(
            headless=False,
            args=[
                "--disable-blink-features=AutomationControlled",
                "--start-maximized",
                "--no-sandbox"
            ]
        )
        
        context = browser.new_context(
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36",
            viewport={'width': 1920, 'height': 1080}
        )

        for link in links_to_categories:
            page = context.new_page()
            print(f"Opening category: {link}")
            page.goto(link, wait_until="load")
            human_delay(1000, 3000)

            # Mimic Human Scrolling
            for _ in range(2):
                page.mouse.wheel(0, random.randint(500, 900))
                human_delay(500, 1000)

            # Click 'Load More'
            try:
                load_more = page.locator("button.load-more-btn.btn.btn--secondary")
                if load_more.is_visible(timeout=3000):
                    load_more.hover()
                    human_delay(200, 500)
                    load_more.click()
                    page.wait_for_load_state("networkidle")
            except:
                pass 

            product_elements = page.locator("div.dne-itemtile").all() 

            for item in product_elements:
                try:
                    # Data Extraction
                    name = item.locator("span[itemprop='name']").inner_text().strip()
                    price = item.locator("span[itemprop='price']").inner_text().strip()
                    link_url = item.locator("a[itemprop='url']").first.get_attribute("href")
                    try:
                        delivery = item.locator("span.dne-itemtile-delivery").inner_text(timeout=10)
                    except:
                        delivery = "Standard delivery"
                    try:
                        refurb_badge = item.locator("span.dne-itemcard-badge-text")
                        is_refurbished = refurb_badge.count() > 0
                    except:
                        is_refurbished = False
                    
                    all_products.append({
                        "name": name,
                        "price": price,
                        "link": link_url,
                        "delivery": delivery,
                        "refurbished": is_refurbished
                    })
                except Exception as e:
                    continue
            
            page.close()
            human_delay(1000, 2000)

        browser.close()
    
    # --- EXPORT SECTION ---
    
    # 1. Save to Pickle (Original)
    globalfunctions.save_to_pickle("ebay_scrap.pkl", all_products)

    # 2. Save to JSON
    with open("ebay_products.json", "w", encoding="utf-8") as f:
        json.dump(all_products, f, indent=4, ensure_ascii=False)

    # 3. Save to CSV
    keys = all_products[0].keys() if all_products else []
    if keys:
        with open("ebay_products.csv", "w", newline="", encoding="utf-8") as f:
            dict_writer = csv.DictWriter(f, fieldnames=keys)
            dict_writer.writeheader()
            dict_writer.writerows(all_products)

    print(f"Finished! Total items: {len(all_products)}")
    print("Files saved: ebay_scrap.pkl, ebay_products.json, ebay_products.csv")

if __name__ == "__main__":
    main_ebay()