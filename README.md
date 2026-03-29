eBay Global Deals Intelligence Scraper

A high-performance, anti-detection web scraper designed to aggregate real-time product data from eBay’s Global Deals platform. This project demonstrates advanced browser automation techniques, including behavioral simulation and stealth integration to bypass modern web-shielding technologies.
🚀 Key Features

    Stealth Integration: Utilizes the Playwright Stealth API and custom browser context arguments to bypass navigator.webdriver detection and Chromium flags.

    Human-Centric Behavior: Implements randomized jitter, variable scrolling speeds, and element hovering to mimic organic user interaction.

    Multi-Category Aggregation: Scrapes across 8+ major retail categories simultaneously.

    Robust Error Handling: Handles Playwright "Strict Mode" violations and dynamic UI elements (like "Load More" buttons) gracefully.

    Data Portability: Exports cleaned data into CSV, JSON, and Pickle formats for easy analysis in Excel, Pandas, or PowerBI.

🛠️ Technical Stack

    Core: Python

    Automation: Playwright

    Stealth: Playwright Stealth API & Custom User-Agent Spoofing

    Data Processing: JSON, CSV, Pickle

📋 Data Points Captured

The scraper extracts the following schema for every product:
Variable	Description
name	The full product title.
price	Current deal price (including currency).
link	The direct URL to the product page.
delivery	Shipping information/speed.
refurbished	Boolean flag (True/False) indicating "eBay Refurbished" status.
⚙️ Installation & Usage

    Clone the repository:
    Bash

    git clone https://github.com/yourusername/ebay-deals-scraper.git
    cd ebay-deals-scraper

    Install dependencies:
    Bash

    pip install playwright playwright-stealth
    playwright install chromium

    Run the scraper:
    Python

    python main.py

🧠 Challenges & Solutions
1. Anti-Bot Detection

Problem: eBay employs sophisticated fingerprinting that detects standard automation.
Solution: I implemented a custom browser context with a modified User-Agent and suppressed the AutomationControlled blink feature. I further added a human_delay function that introduces randomized pauses (500ms to 1500ms) to break the mechanical rhythm of the script.
2. Strict Mode Violations

Problem: eBay's HTML structure often uses the same itemprop attributes for both images and text links, causing Playwright to throw a "resolved to 2 elements" error.
Solution: Refined locators using the .first property and scoped element searches within the dne-itemtile container to ensure 1:1 data mapping.
3. Refurbished Status Verification

Problem: The "eBay Refurbished" badge is not present on all items, and standard locators returned "True" even when the element was absent.
Solution: Utilized the .count() method to perform a boolean check on the badge's existence within each specific product card.
📄 License

Distributed under the MIT License. See LICENSE for more information.
Implementation Note

This project is for educational purposes only. Always check eBay's robots.txt and Terms of Service before scraping at scale.