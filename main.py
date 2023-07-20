import requests
from bs4 import BeautifulSoup
import smtplib
import sheety


MY_EMAIL = "trakerprice@gmail.com"
password = "xyiqizsofnypjsyd"

URL = "https://pharma-shop.tn/protection-superieure-a-spf-50/2136-svr-sun-secure-blur-spf50-50ml-3662361002597.html"

response = requests.get(URL)
data = response.text
soup = BeautifulSoup(data, "html.parser")
price = (soup.find("span", itemprop="price").text.split()[0])
price_int = float(price.replace(",", "."))

article = soup.find("h1", class_="h1").text







data = sheety.get_customer_emails()
emails = [row["email"] for row in data]
names = [row["firstName"] for row in data]
prices = [row["bedget"] for row in data]
for p, email, name in zip(prices, emails, names):
    if price_int <= float(p) :
        message = f"Subject:Pharma Price Alert!\n\nhi! {name}\n{article} is now {price_int}DT\n{URL}"
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=password)
            connection.sendmail(from_addr=MY_EMAIL, to_addrs=email, msg=message)



# if price_int < 52 :
#     message = f"Subject:Pharma Price Alert!\n\n{article} is now {price_int}DT\n{URL}"
#     with smtplib.SMTP("smtp.gmail.com") as connection:
#         connection.starttls()
#         connection.login(user=MY_EMAIL, password=password)
#         for email in emails:
#
#             connection.sendmail(from_addr=MY_EMAIL, to_addrs=email, msg=message)
