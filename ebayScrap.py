#NOTE You can get all the info from the specific product by a simple request, remember it

from playwright.sync_api import sync_playwright
import undetected_chromedriver as uc
import time 
import ebay_scrapper.globalfunctions as globalfunctions

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



def main_ebay():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        for link in links_to_categories:
            page = browser.new_page()
            page.goto(link)
            page.route("**/*.{png,jpg,jpeg,webp,css}", lambda route: route.abort())

            page.wait_for_load_state("networkidle")
            try:
                page.locator("button.load-more-btn.btn.btn--secondary").click()
                print(f"Button found at link {link}")
                page.wait_for_load_state("networkidle", timeout=10000)
            except:
                print("No load_more_button found, all products scraped")

            links_to_products = page.locator("a[itemprop='url']").all()
            names_of_products = page.locator("span[itemprop='name']").all()
            prices_of_products = page.locator("span[itemprop='price']").all()

            products = []
            for link, name, price in zip(links_to_products, names_of_products, prices_of_products):
                product = {
                    "link": link.get_attribute("href"),
                    "name": name.inner_text(),
                    "price": price.inner_text()
                }
                products.append(product)
            page.close()
    globalfunctions.save_to_pickle("ebay_scrap.pkl", products)
            

       
if __name__ == "__main__":
    main_ebay()
