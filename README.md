# EbayHunter — eBay Web Scraper

A web scraper that grabs deal data from eBay's global deals pages. It mimics real user behavior (randomized delays, scrolling, hovers) and exports everything to JSON, CSV, and Pickle formats.

---

## What It Does

EbayHunter automates the boring task of hunting for discounted products across eBay. It crawls through 8 different deal categories, pulls product info (name, price, link, shipping details), and saves it in multiple formats so you can use it however you want.

The scraper tries not to get caught — it rotates user agents, randomizes timing between requests, and generally behaves like a human browsing the site.

---

## Features

- **Anti-Detection** — Rotates user agents, disables automation detection flags, adds realistic delays and mouse movements
- **Human-like Behavior** — Random scroll depths, hover-before-click patterns, varying request speeds
- **Multiple Export Formats** — Saves to JSON, CSV, and Pickle all at once
- **Load More Handling** — Clicks "Load More" buttons to grab all available products on a page
- **8 Deal Categories** — Electronics, Fashion, Automotive, Gaming, Home & Garden, Lifestyle, Business, and Shoes
- **Resilient Requests** — Built-in proxy support, session reuse for cookies, and graceful error handling
- **Clean Data** — Captures product name, price, URL, delivery info, and refurbished status

---

## Quick Start

### Install dependencies

```bash
pip install playwright fake-useragent requests
playwright install chromium
```

### Run it

```bash
python ebay_scraper.py
```

Three files will be created in your working directory:

- **`ebay_products.json`** — Use this for APIs and dashboards
- **`ebay_products.csv`** — Open in Excel or pandas
- **`ebay_scrap.pkl`** — Fast Python reloading, good for ML pipelines

---

## What You Get

Each product looks like this:

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

## How It Avoids Detection

The scraper uses two layers to stay under the radar:

**Playwright side:**
- Disables the `AutomationControlled` flag that alerts sites you're using a bot
- Uses a fake desktop user agent and sets a normal 1920x1080 viewport
- Randomizes scroll depth and timing on every page load

**Request side:**
- Rotates user agents on every HTTP request
- Sets normal browser headers (Referer, Accept-Language, etc.)
- Adds random delays between requests (1–5 seconds)
- Can inject HTTP proxies if you need IP rotation

---

## Project Layout

```
ebay-hunter/
├── ebay_scraper.py       # Main scraper using Playwright
├── globalfunctions.py    # Utility functions (requests, pickle I/O)
├── ebay_products.json    # Output (JSON)
├── ebay_products.csv     # Output (CSV)
└── ebay_scrap.pkl        # Output (Pickle)
```

---

## Utilities in `globalfunctions.py`

**Pickle helpers** — `save_to_pickle()` and `load_from_pickle()` for quick Python object storage.

**Request wrapper** — `secure_request()` is a drop-in for `requests.get/post` with built-in anti-detection. Handles user agent rotation, headers, proxies, and session reuse.

```python
response = secure_request("https://example.com", method="GET")
response = secure_request("https://api.example.com", method="POST", payload={"user": "bob"})
```

---

## Categories Covered

- Home & Garden
- Lifestyle
- Business & Industrial
- Automotive
- Video Games & Consoles
- Fashion
- Men's Shoes & Accessories
- Electronics

---

## Legal Note

This is for learning and personal use. Scraping eBay may violate their [Terms of Service](https://www.ebay.com/help/policies/member-behaviour-policies/user-agreement?id=4259), so check their `robots.txt` and ToS first. I'm not responsible if you get in trouble.

---

## Built With

- Python 3.10+
- Playwright for browser automation
- fake-useragent for user agent rotation
- requests for HTTP calls
- CSV, JSON, and Pickle for exports

---

## License

MIT — use it, fork it, change it, whatever.
