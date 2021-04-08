import requests
from bs4 import BeautifulSoup
from time import sleep
from datetime import date
import csv
import sendmail

urls = ["https://finance.yahoo.com/quote/AMZN?p=AMZN&.tsrc=fin-srch","https://finance.yahoo.com/quote/GOOG?p=GOOG&.tsrc=fin-srch","https://finance.yahoo.com/quote/MSFT?p=MSFT&.tsrc=fin-srch"]

headers = {'User-Agent' : "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36"}
today = str(date.today()) + ".csv"
csv_file = open(today,"w")
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['Stock Name','Current Price','Previous Close','Open','Bid','Ask','Days Range','52 Week Range','Volume','Avg. Volume'])

for url in urls:
    stocks=  []
    html_page = requests.get(url,headers=headers)

    soup = BeautifulSoup(html_page.content,'lxml')
    header_info = soup.find_all("div",id="quote-header-info")[0]
    stock_title = header_info.find("h1").get_text()
    current_price = header_info.find("div",class_="My(6px) Pos(r) smartphone_Mt(6px)").find("span").get_text()


    stocks.append(stock_title)
    stocks.append(current_price)

    table_info = soup.find_all("table",class_="W(100%)")[0].find_all("tr")
    for data in table_info:
        value = data.find_all("td")[0].get_text()
        stocks.append(value)
    csv_writer.writerow(stocks)
    sleep(5)

csv_file.close()

sendmail.send(filename=today)
