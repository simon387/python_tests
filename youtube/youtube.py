from telnetlib import EC

import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

# pip install phantomjs
# pip install selenium
# pip uninstall selenium
# pip install -U selenium==3.3.0


# headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0",
# 		   "Accept-Encoding": "gzip, deflate",
# 		   "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "DNT": "1",
# 		   "Connection": "close", "Upgrade-Insecure-Requests": "1"}
url_amazon = "https://www.amazon.it/dp/B08VS8YG8H?tag=techdealer09e-21&linkCode=osi&th=1&psc=1"


# def scrape_page(url):
# 	page = requests.get(url, headers=headers)
# 	return BeautifulSoup(page.content, 'html.parser')


if __name__ == "__main__":
	# soup = scrape_page(url_amazon)
	# lis = soup.find_all("li", {"class": "videoBlockIngress"})
	# driver = webdriver.PhantomJS(executable_path='/usr/local/lib/node_modules/phantomjs/lib/phantom/bin/phantomjs')

	driver = webdriver.PhantomJS()
	driver.set_window_size(1920, 1080)
	driver.get(url_amazon)
	el = driver.find_element_by_css_selector(".videoBlockIngress")
	el.click()
	driver.save_screenshot('screen0.png')
	# attribute_value = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.TAG_NAME, "video"))).get_attribute("src")
	el = driver.find_element_by_css_selector("video")
	driver.save_screenshot('screen1.png')
	print(el.get_attribute("src"))

	driver.quit()
