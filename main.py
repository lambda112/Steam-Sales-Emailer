import smtplib
from playwright.sync_api import sync_playwright
from page_contents import get_html

divs = get_html()
game_data = []

#GET GAME TITLE
for d in divs:
    title = d.css_first("div[class *= 'StoreSaleWidgetTitle']").text()

    data = {
        "title":title
    }

    game_data.append(data)

print(game_data)