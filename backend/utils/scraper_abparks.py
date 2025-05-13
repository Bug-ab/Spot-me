
from playwright.sync_api import sync_playwright

def check_ab_parks(campground_url):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto(campground_url)
        page.wait_for_selector("body")
        html = page.content()
        print("Scraped Alberta Parks page.")
        browser.close()
