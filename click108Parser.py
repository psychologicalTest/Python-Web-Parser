'''
  click108Parser.py
  @about-Parse data from click108
  Created by 中皓 李 on 2017/05/25.
  Copyright © 2017 中皓 李. All rights reserved.
'''

from bs4 import BeautifulSoup #@note-(install via pip3)
import json
from selenium import webdriver #@note-parse ajax call back from website(install via pip3)
import urllib.parse
import json

driver = webdriver.PhantomJS(executable_path=r'/Users/zhonghaoli/Downloads/phantomjs-2.1.1-macosx/bin/phantomjs') # PhantomJS
psychologicalTestArray=[]
psychologicalTestArray.clear()

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
	for articleURL in table : #question loop
		articleContent = {}
		articleContent.clear()

		soup = brewSoup(articleURL.a['href'])
		url = articleURL.a['href']
		parsed = urllib.parse.urlparse(url)
		qID = urllib.parse.parse_qs(parsed.query)['qID'][0]


		table = soup.findAll('span', attrs={'class':'title03'})
		print('======================================')
		articleContent['type'] = 'love'
		print('題目：'+table[1].text)
		articleContent['title'] = table[1].text
		articleContent['questions'] = []
		print('--------------------------------------')
		questions = []
		questions.clear()
		questionsContent = {}
		questionsContent.clear()
		print(table[2].text)
		questionsContent['Qtitle'] = table[2].text
		options = soup.findAll('span', attrs={'class':'txt01'}) ##options
		Qoptions = []
		Qoptions.clear()
		optionCount = 0
		for j in options : #qoption loop

			option = {}
			option.clear()


			if optionCount == 0:
				option['option'] = 'A'
			 
			elif optionCount == 1:
				option['option'] = 'B'
			 
			elif optionCount == 2:
				option['option'] = 'C'
			 
			else:
				option['option'] = 'D'
			 

			option['context'] = j.text
			print(j.text)
			optionCount += 1
			Qoptions.append(option)
		questionsContent['Qoptions'] = Qoptions
		articleContent['questions'].append(questionsContent)

		print (json.dumps(articleContent,sort_keys=True, indent=4, ensure_ascii=False))

		print('--------------------------------------')


		optionPage = 1
		requestURL= articleURL.a['href']+'&sID='+str(optionPage)
		soup = brewSoup(requestURL)
		table = soup.findAll('span', attrs={'class':'title03'})



		while table[2].text  :

			
			questionsContent.clear()
			optionPage += 1
			print(table[2].text)
			questionsContent['Qtitle'] = table[2].text
			options = soup.findAll('span', attrs={'class':'txt01'}) ##options
			Qoptions = []
			Qoptions.clear()

			optionCount = 0
			for j in options :

				option = {}
				option.clear()


				if optionCount == 0:
					option['option'] = 'A'
				 
				elif optionCount == 1:
					option['option'] = 'B'
				 
				elif optionCount == 2:
					option['option'] = 'C'
				 
				else:
					option['option'] = 'D'
				 

				option['context'] = j.text
				print(j.text)
				optionCount += 1
				Qoptions.append(option)
			questionsContent['Qoptions'] = Qoptions


			print('--------------------------------------')
			requestURL= articleURL.a['href']+'&sID='+str(optionPage)
			soup = brewSoup(requestURL)
			table = soup.findAll('span', attrs={'class':'title03'})
			articleContent['questions'].append(questionsContent)
			print (json.dumps(articleContent,sort_keys=True, indent=4, ensure_ascii=False))
			break
		
		

		
		
		psychologicalTestArray.append(articleContent)
		with open("fk.json", 'a') as out:
			out.write(json.dumps(psychologicalTestArray, ensure_ascii=False, indent=4))

		print('==terminated==')
		break

		#print('++++++++++++++++++++++++++++++++++++++')
		#requestURL= 'http://astro.click108.com.tw/unit001/testResult.php?qID='+str(qID)
		#print(requestURL)
		#soup = brewSoup(requestURL)
		#table = soup.findAll('span', attrs={'class':'txt01'})
		#for k in table :
		#	print(k.text)
		#	print('***********************************')
		#print('++++++++++++++++++++++++++++++++++++++')

		#print('end')
		#print('======================================')
