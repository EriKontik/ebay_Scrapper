# 🕷️ EbayHunter — Stealth Web Scraper for eBay Global Deals

> A production-grade, anti-detection web scraper that silently harvests deal data across eBay's top categories — built with Playwright, human-behavior simulation, and multi-format export pipelines.

---

## 📸 Overview

**EbayHunter** automates the discovery and extraction of discounted products from eBay's Global Deals pages. It navigates the site like a real user — randomized delays, mouse movement, viewport simulation — while collecting structured product data and exporting it to JSON, CSV, and Pickle formats for downstream analysis or integration.

---

## ✨ Features

- 🧠 **Anti-Detection Engine** — Randomized `User-Agent` rotation via `fake_useragent`, spoofed browser fingerprints, and `AutomationControlled` flag disabled
- 🖱️ **Human Behavior Simulation** — Randomized scroll depth, hover-before-click patterns, and millisecond-range timing jitter
- 📦 **Multi-Format Export** — Simultaneously saves to `.json`, `.csv`, and `.pkl` for maximum flexibility
- 🔄 **Dynamic Content Handling** — Detects and clicks "Load More" buttons before scraping to maximize data yield
- 🌐 **Multi-Category Scraping** — Covers 8 eBay deal categories in a single run (Electronics, Fashion, Automotive, Gaming, and more)
- 🔒 **Resilient Request Layer** — `secure_request()` utility with proxy support, session reuse, and graceful HTTP error handling
- 🏷️ **Rich Product Schema** — Captures name, price, product URL, delivery info, and refurbished status per item

---

## 🗂️ Project Structure

```
ebay-hunter/
│
├── ebay_scraper.py        # Main scraper — Playwright-powered, category-aware
├── globalfunctions.py     # Shared utilities: pickle I/O, secure HTTP requests
│
├── ebay_scrap.pkl         # Binary export (Pickle)
├── ebay_products.json     # Structured JSON export
└── ebay_products.csv      # Flat CSV export
```

---

## 🚀 Getting Started

### Prerequisites

```bash
pip install playwright fake-useragent requests
playwright install chromium
```

### Run the scraper

```bash
python ebay_scraper.py
```

On completion, three output files are generated in the working directory:

| File | Format | Use Case |
|---|---|---|
| `ebay_products.json` | JSON | APIs, dashboards, front-end consumption |
| `ebay_products.csv` | CSV | Excel, Google Sheets, pandas analysis |
| `ebay_scrap.pkl` | Pickle | Python-native ML pipelines, fast reload |

---

## 🔬 Data Schema

Each scraped product follows this structure:

```json
{
  "name": "Apple AirPods Pro (2nd Gen)",
  "price": "$189.99",
  "link": "https://www.ebay.com/itm/...",
  "delivery": "Free shipping",
  "refurbished": false
}
```

---

## 🛡️ Anti-Detection Architecture

EbayHunter combines two layers of evasion:

**Playwright Layer** (`ebay_scraper.py`)
- Launches Chromium with `--disable-blink-features=AutomationControlled`
- Injects a realistic `User-Agent` string and sets a `1920x1080` viewport
- Randomizes scroll distance and interaction timing per page

**Request Layer** (`globalfunctions.py`)
- Rotates `User-Agent` on every request via `fake_useragent`
- Sets browser-standard headers (`Accept-Language`, `Referer`, etc.)
- Supports HTTP proxy injection for IP rotation
- Applies a 1–5 second randomized delay between requests

---

## 📦 Utility: `globalfunctions.py`

Two reusable utilities power the project's persistence and request layers:

### `save_to_pickle` / `load_from_pickle`
Binary serialization for fast Python-native storage and retrieval of any object.

### `secure_request(url, method, headers, payload, proxies, session)`
A drop-in replacement for `requests.get/post` with built-in anti-detection measures. Supports session reuse for cookie persistence across requests.

```python
response = secure_request("https://example.com", method="GET")
response = secure_request("https://api.example.com/login", method="POST", payload={"user": "x"})
```

---

## 🗺️ Scraped Categories

| Category | URL |
|---|---|
| Home & Garden | `/globaldeals/home/more-home-garden` |
| Lifestyle | `/globaldeals/featured/lifestyle` |
| Business & Industrial | `/globaldeals/more/business-industrial` |
| Automotive | `/globaldeals/more/automotive` |
| Video Games & Consoles | `/globaldeals/tech/video-games-consoles` |
| Fashion | `/globaldeals/featured/fashion` |
| Men's Shoes & Accessories | `/globaldeals/fashion/mens-shoes-accessories` |
| Electronics | `/globaldeals/featured/electronics` |

---

## ⚠️ Disclaimer

This project is intended for **educational and personal research purposes only**. Scraping eBay may violate their [Terms of Service](https://www.ebay.com/help/policies/member-behaviour-policies/user-agreement?id=4259). Always review a website's `robots.txt` and ToS before scraping. The author is not responsible for any misuse.

---

## 🧰 Tech Stack

![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=flat&logo=python&logoColor=white)
![Playwright](https://img.shields.io/badge/Playwright-1.x-2EAD33?style=flat&logo=playwright&logoColor=white)
![Requests](https://img.shields.io/badge/Requests-HTTP-FF6B35?style=flat)
![CSV/JSON](https://img.shields.io/badge/Export-CSV%20%7C%20JSON%20%7C%20Pickle-lightgrey?style=flat)

---

## 📄 License

MIT — free to use, modify, and distribute with attribution.
