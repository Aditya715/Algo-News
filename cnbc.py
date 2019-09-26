from bs4 import BeautifulSoup as bs
import requests
import json

def cnbc():
	url = 'https://www.cnbc.com/stocks/'
	list_of_json = list()
	response = requests.get(url)
	if response.status_code == 200:
		soup = bs(response.text, "lxml")
		news_section = soup.find_all("div", class_="Card-standardBreakerCard")
		for each_news in news_section:
			title_sec = each_news.find("div", class_="Card-textContent")
			title = title_sec.text if title_sec else None
			if title:
				url_sec = title_sec.find("a", class_="Card-title")
				src_url = url_sec.get("href")
				time_sec = title_sec.find("a", class_="Card-time")
				news_time = time_sec.text if time_sec else None
				temp = {
					'title' 		: title,
					'img_url' 		: None,
					'timestamp' 	: news_time,
					'description' 	: '',
					'src_url'		: src_url,
					'src_name'		: 'cnbc',
				}
				list_of_json.append(temp)
				print(temp)
	with open("cnbc_news.json", "w") as jsonfile:
		json.dump(list_of_json, jsonfile)

cnbc()