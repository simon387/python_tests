#
# script di demo
#
import logging
import threading
import time
from datetime import datetime, timedelta

import requests
from bs4 import BeautifulSoup

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0",
           "Accept-Encoding": "gzip, deflate",
           "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "DNT": "1",
           "Connection": "close", "Upgrade-Insecure-Requests": "1"}
bot_token = ""
chat_id = "test_chatutti_channel"
price_treshold = 4.000
timestamp_array = []
seconds_deelay = 4
hours_window = 24
url_array = [
	'https://www.amazon.es/dp/B08KHL21CV/',
	'https://www.amazon.de/dp/B08WBB7KXV/',
	'https://www.amazon.es/dp/B08KHKDTSJ/',
	'https://www.amazon.es/dp/B08MDC8J27/',
	'https://www.amazon.fr/dp/B08RWZLDPN/',
	'https://www.amazon.it/dp/B09649JG37/',
	'https://www.amazon.it/dp/B08HM661YM/',
	'https://www.amazon.it/dp/B08MDC8J27/',
	'https://www.amazon.it/dp/B08KHKDTSJ/',
	'https://www.amazon.es/dp/B08HLZXHZY/',
	'https://www.amazon.fr/dp/B08P5XMGX7/',
	'https://www.amazon.fr/dp/B08H98GVK8/',
	'https://www.amazon.fr/dp/B08H93ZRK9/',
	'https://www.amazon.it/dp/B08WBB7KXV/',
	'https://www.amazon.co.uk/dp/B08QJNJ279/',
	'https://www.amazon.fr/dp/B08XQWR62V/',
	'https://www.amazon.co.uk/dp/B08Q36SRKK/',
	'https://www.amazon.es/dp/B08XQWR62V/',
	'https://www.amazon.es/dp/B08HBR7QBM/',
	'https://www.amazon.es/dp/B08LNQTSCT/',
	'https://www.amazon.co.uk/dp/B08LNQTSCT/',
	'https://www.amazon.it/dp/B08RWZLDPN/',
	'https://www.amazon.es/dp/B08CDV9CNS/',
	'https://www.amazon.es/dp/B08H93ZRLL/',
	'https://www.amazon.es/dp/B08L6PCZTR/',
	'https://www.amazon.fr/dp/B08L6PCZTR/',
	'https://www.amazon.it/dp/B08L6PCZTR/',
	'https://www.amazon.de/dp/B08QYQH7QW/',
	'https://www.amazon.es/dp/B08HBJB7YD/',
	'https://www.amazon.de/dp/B08YKH7VMN/',
	'https://www.amazon.es/dp/B08TZD9SH9/',
	'https://www.amazon.fr/dp/B08TZD9SH9/',
	'https://www.amazon.it/dp/B08TZD9SH9/',
	'https://www.amazon.co.uk/dp/B08KHJS572/',
	'https://www.amazon.co.uk/dp/B08H93GKNJ/',
	'https://www.amazon.fr/dp/B08L3Q41SM/',
	'https://www.amazon.es/dp/B08L3Q41SM/',
	'https://www.amazon.co.uk/dp/B08LTJVGYS/',
	'https://www.amazon.de/dp/B08L3Q41SM/',
	'https://www.amazon.de/dp/B08LNY8P5L/',
	'https://www.amazon.de/dp/B08PDP837W/',
	'https://www.amazon.de/dp/B08LLG9KQT/',
	'https://www.amazon.it/dp/B08JDSW1ZW/',
	'https://www.amazon.co.uk/dp/B08L3QCZKZ/',
	'https://www.amazon.es/dp/B08HGYXP4C/',
	'https://www.amazon.es/dp/B08HGS1SXH/',
	'https://www.amazon.it/dp/B08LLG9KQT/',
	'https://www.amazon.de/dp/B08MKWZZ2G/',
	'https://www.amazon.co.uk/dp/B08X12YK8G/',
	'https://www.amazon.co.uk/dp/B08LDS72P2/',
	'https://www.amazon.fr/dp/B08HJ9XFNM/',
	'https://www.amazon.de/dp/B08L3QCZKZ/',
	'https://www.amazon.fr/dp/B08WHJFYM8/',
	'https://www.amazon.fr/dp/B08HN51T8Q/',
	'https://www.amazon.es/dp/B08BQX8VP3/',
	'https://www.amazon.es/dp/B08WRF18SC/',
	'https://www.amazon.co.uk/dp/B08HN642LY/',
	'https://www.amazon.es/dp/B08VH7DWP2/',
	'https://www.amazon.es/dp/B08WS5X6F5/',
	'https://www.amazon.es/dp/B08LNWPYRS/',
	'https://www.amazon.de/dp/B08KHL2J5X/',
	'https://www.amazon.it/dp/B08KHL2J5X/',
	'https://www.amazon.de/dp/B08WH4RK2C/',
	'https://www.amazon.it/dp/B08KGVL9JQ/',
	'https://www.amazon.it/dp/B08LTKLG5K/',
	'https://www.amazon.de/dp/B08LNPPCWJ/',
	'https://www.amazon.fr/dp/B08LNY8P5L/',
	'https://www.amazon.it/dp/B08HLZXHZY/',
	'https://www.amazon.fr/dp/B08KHLDS72/',
	'https://www.amazon.it/dp/B08P3M97FG/',
	'https://www.amazon.de/dp/B08WRV24YD/',
	'https://www.amazon.es/dp/B08WH4RK2C/',
	'https://www.amazon.co.uk/dp/B08LNY8P5L/',
	'https://www.amazon.de/dp/B08P3BJ9Y8/',
	'https://www.amazon.de/dp/B08P34VCVN/',
	'https://www.amazon.de/dp/B08KGVL9JQ/',
	'https://www.amazon.it/dp/B08KHL21CV/',
	'https://www.amazon.it/dp/B08HN4DSTC/',
	'https://www.amazon.it/dp/B08TJ2BHCQ/',
	'https://www.amazon.co.uk/dp/B08WHML7GL/',
	'https://www.amazon.co.uk/dp/B08QVRZH3C/',
	'https://www.amazon.co.uk/dp/B08NW76K61/',
	'https://www.amazon.co.uk/dp/B08QD49S3B/',
	'https://www.amazon.fr/dp/B08Y934HZQ/',
	'https://www.amazon.co.uk/dp/B08H97NYGP/',
	'https://www.amazon.fr/dp/B08HR1NPPQ/',
	'https://www.amazon.fr/dp/B08VH8H82H/',
	'https://www.amazon.co.uk/dp/B08H95Y452/',
	'https://www.amazon.co.uk/dp/B08P3JL63Y/',
	'https://www.amazon.co.uk/dp/B08BQX8VP3/',
	'https://www.amazon.co.uk/dp/B08P8Y81LF/',
	'https://www.amazon.it/dp/B08HGS1SXH/',
	'https://www.amazon.de/dp/B08PDMYN2D/',
	'https://www.amazon.co.uk/dp/B08HGYXP4C/',
	'https://www.amazon.it/dp/B08X12YK8G/',
	'https://www.amazon.it/dp/B08HBQWBHH/',
	'https://www.amazon.de/dp/B08LTKLG5K/',
	'https://www.amazon.fr/dp/B08WRQ3JR1/',
	'https://www.amazon.fr/dp/B08PDP837W/',
	'https://www.amazon.es/dp/B08HBVX53D/',
	'https://www.amazon.es/dp/B08WRQ3JR1/',
	'https://www.amazon.de/dp/B08HBQWBHH/',
	'https://www.amazon.co.uk/dp/B08HJ9XFNM/',
	'https://www.amazon.it/dp/B08JQQ1VD1/',
	'https://www.amazon.de/dp/B08HGYXP4C/',
	'https://www.amazon.co.uk/dp/B08WS5X6F5/',
	'https://www.amazon.fr/dp/B08HR9JSMS/',
	'https://www.amazon.co.uk/dp/B08PFZ28CN/',
	'https://www.amazon.co.uk/dp/B08HLYQ9XL/',
	'https://www.amazon.co.uk/dp/B08KH7RL89/',
	'https://www.amazon.es/dp/B08KHFZN9P/',
	'https://www.amazon.it/dp/B08KKJ37F7/',
	'https://www.amazon.de/dp/B08HR9JSMS/',
	'https://www.amazon.fr/dp/B08R427DMQ/',
	'https://www.amazon.fr/dp/B08KHL2J5X/',
	'https://www.amazon.it/dp/B08WRV24YD/',
	'https://www.amazon.it/dp/B08KHFZN9P/',
	'https://www.amazon.es/dp/B08LLG9KQT/',
	'https://www.amazon.it/dp/B08KHHF881/',
	'https://www.amazon.it/dp/B08QZLMC86/',
	'https://www.amazon.co.uk/dp/B08JCVWTQY/',
	'https://www.amazon.fr/dp/B08KHL21CV/',
	'https://www.amazon.co.uk/dp/B08HM6D7TM/',
	'https://www.amazon.de/dp/B08P3KWZV7/',
	'https://www.amazon.de/dp/B08KHL21CV/',
	'https://www.amazon.de/dp/B08BNNSJMZ/',
	'https://www.amazon.it/dp/B08LNY8P5L/',
	'https://www.amazon.fr/dp/B08LBVNKT1/',
	'https://www.amazon.de/dp/B08HN4DSTC/',
	'https://www.amazon.fr/dp/B08LNQTSCT/',
	'https://www.amazon.co.uk/dp/B08JQQ1VD1/',
	'https://www.amazon.de/dp/B08PFZ28CN/',
	'https://www.amazon.co.uk/dp/B08WBB7KXV/',
	'https://www.amazon.co.uk/dp/B08LDS72P2/',
	'https://www.amazon.co.uk/dp/B08Z83QKWX/',
	'https://www.amazon.co.uk/dp/B08LNPPCWJ/',
	'https://www.amazon.it/dp/B08LBVNKT1/',
	'https://www.amazon.it/dp/B08R427DMQ/',
	'https://www.amazon.fr/dp/B08LLG9KQT/',
	'https://www.amazon.de/dp/B08P7ZKQPP/',
	'https://www.amazon.it/dp/B08P7ZKQPP/',
	'https://www.amazon.es/dp/B08WHML7GL/',
	'https://www.amazon.it/dp/B08WHML7GL/',
	'https://www.amazon.de/dp/B08H98GVK8/',
	'https://www.amazon.fr/dp/B08WRK84PS/',
	'https://www.amazon.es/dp/B08WRV24YD/',
	'https://www.amazon.co.uk/dp/B08HR9JSMS/',
	'https://www.amazon.fr/dp/B08HBF5L3K/',
	'https://www.amazon.de/dp/B08H93ZRK9/',
	'https://www.amazon.es/dp/B08BNNSJMZ/',
	'https://www.amazon.es/dp/B08HBF5L3K/',
	'https://www.amazon.it/dp/B08HBF5L3K/',
	'https://www.amazon.de/dp/B08HBF5L3K/',
	'https://www.amazon.de/dp/B08NZ4G4T2/',
	'https://www.amazon.es/dp/B08CRH6DYB/',
	'https://www.amazon.co.uk/dp/B08QCLRN7S/',
	'https://www.amazon.fr/dp/B08H93ZRLL/',
	'https://www.amazon.it/dp/B08HGYXP4C/',
	'https://www.amazon.de/dp/B08K3PDL9K/',
	'https://www.amazon.de/dp/B08H93ZRLL/',
	'https://www.amazon.co.uk/dp/B08WR6DRQQ/',
	'https://www.amazon.co.uk/dp/B08RWZLDPN/',
	'https://www.amazon.es/dp/B08Y746XN7/',
	'https://www.amazon.fr/dp/B08VH7BD47/',
	'https://www.amazon.co.uk/dp/B08KHL21CV/',
	'https://www.amazon.co.uk/dp/B08Z83QKWX/',
	'https://www.amazon.it/dp/B08CRH6DYB/',
	'https://www.amazon.de/dp/B08WHML7GL/',
	'https://www.amazon.de/dp/B08KHFZN9P/',
	'https://www.amazon.fr/dp/B08WRV24YD/',
	'https://www.amazon.co.uk/dp/B08WH4RK2C/',
]


def check_price(url_amazon, index):
	while True:
		now = datetime.now()
		if now - timedelta(hours=hours_window) <= timestamp_array[index] <= now + timedelta(hours=hours_window):
			logging.info('Link ' + url_amazon + ' already sent in the last ' + str(hours_window) + ' hours')
		else:
			soup = scrape_page(url_amazon)
			price = 0
			converted_price = 0
			try:
				price = soup.find(id="priceblock_ourprice").get_text()
				converted_price = float(price[0:5])
			except:
				print("An exception occurred for " + url_amazon)
			# print('Source code from amazon:')
			# print(soup.prettify())

			if converted_price < price_treshold:
				text = create_telegram_message(soup, price, url_amazon)
				send_telegram(text, url_amazon)
				timestamp_array[index] = datetime.now()
		#
		time.sleep(seconds_deelay)


def scrape_page(url_amazon):
	page = requests.get(url_amazon, headers=headers)
	return BeautifulSoup(page.content, 'html.parser')


def send_telegram(text, url_amazon):
	logging.info('Sending info to telegram channel for: ' + url_amazon)
	api_telegram = 'https://api.telegram.org/bot'
	parse_mode = '&parse_mode=HTML&disable_web_page_preview=false'
	requests.post(api_telegram + bot_token + '/sendMessage?chat_id=@' + chat_id + '&text=' + text + parse_mode)


def create_telegram_message(soup, price, url_amazon):
	description = soup.find(id="productTitle").get_text().strip()
	asin_input = soup.find(id="ASIN")
	asin = asin_input['value']
	img = soup.find(id="landingImage")
	img_src = img['src']
	#
	link_page = url_amazon[8:].split(asin)[0] + asin
	#
	url_splitted = url_amazon.split('/')
	quantity = '%26Quantity.1=1'
	link_add_to_cart = url_splitted[0] + '//' + url_splitted[2] + '/gp/aws/cart/add.html?ASIN.1=' + asin + quantity
	#
	img_container = '<a href="' + img_src + '">  </a>'
	#
	return description + '\n' + \
	       price + '\n' + \
	       '<a href="' + link_page + '">LINK TO PAGE</a>' + '\n' + \
	       img_container + '\n<a href="' + link_add_to_cart + '">ADD TO CART</a>'


def manage_urls():
	for idx, url in enumerate(url_array):
		thread = threading.Thread(target=check_price, args=(url, idx))
		logging.info("Main    : running thread check_price for " + url)
		thread.start()


if __name__ == "__main__":
	log_format = "%(asctime)s: %(message)s"
	logging.basicConfig(format=log_format, level=logging.INFO, datefmt="%H:%M:%S")
	#
	for x in url_array:
		timestamp_array.append(datetime.min)
	#
	manage_urls()
