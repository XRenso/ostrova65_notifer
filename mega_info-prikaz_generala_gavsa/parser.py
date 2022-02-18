
from bs4 import BeautifulSoup
import requests
from datetime import datetime
from fake_useragent import UserAgent

ua = UserAgent()
headers = {'accept': '*/*', 'user-agent': ua.firefox}
news_url = 'https://sakhalin.info/'
news_already = []
rubriks_url=[]
rubriks_name=[]

def get_html(url):
	response = requests.get(url, headers=headers)
	if response.status_code == 200:
		result = requests.get(url)
	return result.text



def get_data(html):
	soup = BeautifulSoup(html, 'lxml')
	data = soup.find('span', class_='short-news_date').text
	return data
    
    
def get_topics(html):
    soup = BeautifulSoup(html, 'lxml')
    for a in soup.find_all('li', class_="dropdown-menu__item dropdown-menu__item_thin"):
        i = a.find('a').get('href')
        n = a.find('a').text
        rubriks_url.append(i)
        rubriks_name.append(n)




get_topics(get_html(news_url))
