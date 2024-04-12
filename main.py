import smtplib
import pandas as pd
from playwright.sync_api import sync_playwright
from page_contents import get_html

divs = get_html()
game_data = []

#GET GAME DATA 
for d in divs:
    title = d.css_first("div[class *= 'StoreSaleWidgetTitle']").text()
    new_price = d.css_first("div[class *= 'Wh0L8E']").text()
    old_price = d.css_first("div[class *= '_1EKG']").text()
    review_score = d.css_first("div[class *= '_2SbZztpb'] > div").text()
    
    discount = d.css_first("div[class *= 'StoreSalePriceWidgetContainer'] > div").text()
    if discount == "New":
        discount = d.css_first("div[class *= 'StoreSalePriceWidgetContainer'] > div + div").text()

    data = {
        "title":title,
        "new_price":new_price,
        "old_price":old_price,
        "discount":discount,
        "review_score":review_score,
    }

    game_data.append(data)

game_table = pd.DataFrame(game_data)
game_table.to_excel("game_data.xlsx", index=False)