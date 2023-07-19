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





print("Welcome to Traker price.\n \
We find the best price deals and email them to you.")

first_name = input("What is your first name? ").title()
last_name = input("What is your last name? ").title()

email1 = "email1"
email2 = "email2"
while email1 != email2:
    email1 = input("What is your email? ")
    if email1.lower() == "quit" \
            or email1.lower() == "exit":
        exit()
    email2 = input("Please verify your email : ")
    if email2.lower() == "quit" \
            or email2.lower() == "exit":
        exit()

print("OK. You're in the club!")

sheety.post_new_row(first_name, last_name, email1)
data = sheety.get_customer_emails()
emails = [row["email"] for row in data]
names = [row["firstName"] for row in data]



if price_int < 53 :
    message = f"Subject:Pharma Price Alert!\n\n{article} is now {price_int}DT"
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=password)
        for email in emails:

            connection.sendmail(from_addr=MY_EMAIL, to_addrs=email, msg=message)