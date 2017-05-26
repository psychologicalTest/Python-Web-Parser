'''
  click108Parser.py
  @about-Parse data from click108
  Created by 中皓 李 on 2017/05/25.
  Copyright © 2017 中皓 李. All rights reserved.
'''

from urllib.parse import quote 
from bs4 import BeautifulSoup #@note-(install via pip3)
import json
from selenium import webdriver #@note-parse ajax call back from website(install via pip3)

driver = webdriver.PhantomJS(executable_path=r'/Users/zhonghaoli/Downloads/phantomjs-2.1.1-macosx/bin/phantomjs') # PhantomJS

def brewSoup(requestURL):
	driver.get(requestURL)
	pageSource = driver.page_source 
	return BeautifulSoup(pageSource, 'html.parser')




catagory = 'love'
#page = 32 
page = 1 ;
while page > 0:
	page -= 1
	requestURL= 'http://astro.click108.com.tw/unit001/index.php?type=love&page=1'
	soup = brewSoup(requestURL)
	#result = soup.findAll("table",{"background","http://yimgs.click108.com.tw/astro2/psychologicTests/images/table02_bg1.gif"})
	table = soup.findAll('td', attrs={'class':'txt06'})
	for i in table :
		print(i) 
     