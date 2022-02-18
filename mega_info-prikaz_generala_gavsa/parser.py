
from bs4 import BeautifulSoup
import requests
from datetime import datetime
from fake_useragent import UserAgent

ua = UserAgent()
headers = {'accept': '*/*', 'user-agent': ua.firefox}
news_url = 'https://sakhalin.info/'
news_already = []
all_rubriks = soup.find_all("li", {"class": "dropdown-menu__item dropdown-menu__item_thin"})
print(all_rubriks)

def get_html(url):
	response = requests.get(url, headers=headers)
	if response.status_code == 200:
		result = requests.get(url)
	return result.text

def get_title(html):
	soup = BeautifulSoup(html, 'lxml')
	title = soup.find('h5').text
	return title

def get_url(html):
	soup = BeautifulSoup(html, 'lxml')
	url = soup.find('h5').find('a').get('href')
	return url
def get_data(html):
	soup = BeautifulSoup(html, 'lxml')
	data = soup.find('span', class_='short-news_date').text
	return data