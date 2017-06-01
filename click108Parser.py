'''
  click108Parser.py
  @about-Parse data from click108
  Created by 中皓 李 on 2017/05/25.
  Copyright © 2017 中皓 李. All rights reserved.
'''

from bs4 import BeautifulSoup #@note-(install via pip3)
import json
from selenium import webdriver #@note-parse ajax call back from website(install via pip3)

driver = webdriver.PhantomJS(executable_path=r'/Users/zhonghaoli/Downloads/phantomjs-2.1.1-macosx/bin/phantomjs') # PhantomJS

def brewSoup(requestURL):
	driver.get(requestURL)
	pageSource = driver.page_source 
	return BeautifulSoup(pageSource, 'html.parser')

catagory = 'love'
page = 1 ;
while page > 0:
	page -= 1
	requestURL= 'http://astro.click108.com.tw/unit001/index.php?type='+str(catagory)+'&page='+str(page)
	soup = brewSoup(requestURL)
	table = soup.findAll('td', attrs={'class':'txt06'})
	for articleURL in table :

		soup = brewSoup(articleURL.a['href'])
		table = soup.findAll('span', attrs={'class':'title03'})
		print('======================================')
		for j in table[1:] :
			print(j.text)
		print('--------------------------------------')
		options = soup.findAll('span', attrs={'class':'txt01'})
		for j in options :
			print(j.text)
		print('--------------------------------------')
		

		page = 1
		requestURL= articleURL.a['href']+'&sID='+str(page)
		soup = brewSoup(requestURL)
		table = soup.findAll('span', attrs={'class':'title03'})
		while table[2].text  :
			page += 1
			print(table[2].text)
			options = soup.findAll('span', attrs={'class':'txt01'})
			for j in options :
				print(j.text)
			print('--------------------------------------')
			requestURL= articleURL.a['href']+'&sID='+str(page)
			soup = brewSoup(requestURL)
			table = soup.findAll('span', attrs={'class':'title03'})


		print('end')
		print('======================================')
