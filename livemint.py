import json
import requests
from bs4 import BeautifulSoup as bs

def livemint_news():
	url = 'https://www.livemint.com/'
	list_of_json = list()
	response = requests.get(url)
	if response.status_code == 200:
		soup = bs(response.text, "lxml")
		news_section = soup.find_all("section", class_="cardHolder")
		for each_news in news_section:
			#--------------IMAGE URL--------------
			img_section = each_news.find("img", class_="lozard")
			img_url = img_section.get("data-src") if img_section else None
			# ---------------HEADLINES SECTION-------#
			headline_section = each_news.find("h1", class_="headline")
			headline = headline_section.text if headline_section else ''
			#-----------------NEWS URL----------------
			if headline_section:
				news_url = headline_section.find("a").get("href") if headline_section.find("a") else None 
			else:
				news_url = None
			#---------------DATE TIME---------------
			time_section = each_news.find("span", class_="pubtime")
			time_span = time_section.find_all("span") if time_section else None
			try:
				news_time = time_span[-1].text if time_span else None
			except:
				news_time = None
			#---------------DESCRIPTION-----------------
			description_sec = each_news.find("ul", class_="highlights")
			description_text = description_sec.text if description_sec else None
			temp = {
				'title' 		: headline,
				'img_url' 		: img_url,
				'timestamp' 	: news_time,
				'description' 	: description_text,
				'src_url'		: news_url,
				'src_name'		: 'livemint',
			}
			print(temp)
			list_of_json.append(temp)
	if list_of_json:
		with open("news.json", ) as jsonfile:
			json.dump(list_of_json, jsonfile)


livemint_news()