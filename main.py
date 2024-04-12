import smtplib
from page_contents import get_html

divs = get_html()

# Get Game Title
for i in divs[0:-2]:
    print(f"{i.html}")