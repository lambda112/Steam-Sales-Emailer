from selectolax.parser import HTMLParser
from playwright.sync_api import sync_playwright
from time import sleep

def get_html():
    with sync_playwright() as playwright:
        # SET UP PAGE
        browser = playwright.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto("https://store.steampowered.com/specials/")

        # WAIT FOR PAGE TO LOAD
        page.wait_for_load_state("networkidle")
        page.mouse.wheel(0,4000)
        page.wait_for_selector("div[class *= 'NO-IP'] > div[class *= 'y9MSdl']")
        print("Got Selector")
        sleep(1)

        # GET HTML
        html = page.inner_html("body")
        tree = HTMLParser(html)
        divs = tree.css("div[class *= 'NO-IP'] > div[class *= 'y9MSdl']")
        return divs
    