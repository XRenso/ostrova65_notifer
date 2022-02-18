from bs4 import BeautifulSoup
import requests
from datetime import datetime
from fake_useragent import UserAgent

ua = UserAgent()
headers = {'accept': '*/*', 'user-agent': ua.firefox}
news_url = 'https://sakhalin.info/'
get_news_url='https://sakhalin.info/'
rubriks_url=[]
rubriks_name=[]
city_names = []
city_urls = []
def get_html(url):
	response = requests.get(url, headers=headers)
	if response.status_code == 200:
		result = requests.get(url)
	return result.text


    
def get_topics(html):
    soup = BeautifulSoup(html, 'lxml')
    for a in soup.find_all('div', class_="dropdown-menu dropdown-menu_disable-on-mobile header__menu-button"):
        # i = a.find('a').get('href')
        n = a.find_all('span', class_='header__menu-link')
        #print(n)
        for j in n:
           if j.text.strip() == 'Рубрики':
              i = a.find_all('ul',class_='dropdown-menu__list')
              for b in i:
                  k = b.find_all('li',class_='dropdown-menu__item dropdown-menu__item_thin')
                  for d in k:
                    rubriks_url.append(d.find('a').get('href'))
                    rubriks_name.append(d.text)
           elif j.text.strip() == 'Города':
              i = a.find_all('ul',class_='dropdown-menu__list')
              for b in i:
                  k = b.find_all('li',class_='dropdown-menu__item dropdown-menu__item_thin')
                  for d in k:
                    city_urls.append(d.find('a').get('href'))
                    city_names.append(d.text)




get_topics(get_html(news_url))

def get_urls_from_topic(i):
	try:
		index = rubriks_name.index(i)
		return rubriks_url[index]
	except:
		index = city_names.index(i)
		return city_urls[index]
	
