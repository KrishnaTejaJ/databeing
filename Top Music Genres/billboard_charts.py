from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import ui
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import requests
from bs4 import BeautifulSoup

import time

data = []

def search(song, artist):
	s = song.replace('(', '').replace(')', '').replace('&', '')
	a = artist.replace('(', '').replace(')', '').replace('&', '').replace('Featuring ', '')
	return s + " " + a
driver = webdriver.Firefox(executable_path="./drivers/geckodriver")
for i in range(2006, 2022):
	url_link = f"https://www.billboard.com/charts/year-end/{i}/hot-100-songs/"
	request = requests.get(url_link)
	Soup = BeautifulSoup(request.text, 'lxml')
	c = 0

	for tags in Soup.find_all("li", {"class":"lrv-u-width-100p"}):
		details = {}
		details['Song'] = tags.find('h3').text.strip()
		details['Artist'] = tags.find('span').text.strip()
		details['Year'] = i
		details['Position'] = c+1
		#driver = webdriver.Firefox(executable_path="./drivers/geckodriver")
		driver.get('https://www.chosic.com/music-genre-finder/')
		search_word = search(details['Song'], details['Artist'])
		driver.find_element_by_xpath("""//*[@id="search-word"]""").send_keys(search_word)
		#the below line is to trigger the results
		driver.find_element_by_xpath("""//*[@id="search-word"]""").send_keys(Keys.BACKSPACE)
		#driver.find_element_by_xpath("""//*[@id="hh1"]""").click()
		WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, """//*[@id="hh1"]"""))).click()
		time.sleep(1)
		details['Genre'] = driver.find_element_by_xpath('/html/body/div/div[1]/div/div[1]/article[1]/div[4]/div/div[2]/a[1]').text

		data.append(details)
		c += 1
		if c == 10:
			break

		#driver.close()
driver.close()
print(data)
