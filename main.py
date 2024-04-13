import smtplib
import pandas as pd
from page_contents import get_html
from update_text_file import update_count
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

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

number = update_count()
msg = MIMEMultipart()
msg['Subject'] = f'Steam Sales Week - {number}'
msg['From'] = "lambdaa112@gmail.com"
msg['To'] = 'lambdaa112@gmail.com'

with open("game_data.xlsx", "rb") as f:
    file = f.read()

part = MIMEBase('application', "octet-stream")
part.set_payload(file)
encoders.encode_base64(part)
part.add_header('Content-Disposition', 'attachment', filename="game_data.xlsx")
msg.attach(part)


with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user = "lambdaa112@gmail.com" , password= "moyn eugt kmga xrck")
    connection.send_message(msg = msg)