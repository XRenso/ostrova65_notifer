from multiprocessing.sharedctypes import Value
from types import NoneType
from bs4 import BeautifulSoup
import requests
from fake_useragent import UserAgent
import re
import os.path
import user_profile as us_pof
import random

ua = UserAgent()
headers = {'User-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'}
news_url = 'https://sakhalin.info/'
get_news_url = 'https://sakhalin.info/'

pravitelstvo_url = 'https://sakhalin.gov.ru/'


page_number = 1

rubriks_url = []
rubriks_name = []
city_names = []
city_urls = []

pravitelstvo_urls = []
pravitelstvo_title = []

topics_title = []
topics_url = []
topic_desk = []

personal_title = []
personal_url = []




def get_html(url):
    if url is not None:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            result = requests.get(url)
            return result.text


def get_topics(html):
    soup = BeautifulSoup(html, 'lxml')
    for a in soup.find_all('div', class_="dropdown-menu dropdown-menu_disable-on-mobile header__menu-button"):
        # i = a.find('a').get('href')
        n = a.find_all('span', class_='header__menu-link')
        # print(n)
        for j in n:
            if j.text.strip() == 'Рубрики':
                i = a.find_all('ul', class_='dropdown-menu__list')
                for b in i:
                    k = b.find_all('li', class_='dropdown-menu__item dropdown-menu__item_thin')
                    for d in k:
                        rubriks_url.append(d.find('a').get('href'))
                        rubriks_name.append(d.text)
            elif j.text.strip() == 'Города':
                i = a.find_all('ul', class_='dropdown-menu__list')
                for b in i:
                    k = b.find_all('li', class_='dropdown-menu__item dropdown-menu__item_thin')
                    for d in k:
                        city_urls.append(d.find('a').get('href'))
                        city_names.append(d.text)


get_topics(get_html(news_url))


def get_urls_from_topic(i):
    global get_news_url, page_number
    try:
        index = rubriks_name.index(i)
        page_number = 1
        get_news_url = rubriks_url[index]
        return rubriks_url[index]
    except ValueError:
        index = city_names.index(i)
        page_number = 1
        get_news_url = city_urls[index]
        return city_urls[index]

def get_next_page(step):
    global page_number, get_news_url
    page_number += step
    path = get_news_url + '/list' + str(page_number)
    soup = BeautifulSoup(get_html(path), 'lxml')

    if soup.find('div', class_='inner').find('p').text != 'Ничего не найдено':
        path = get_news_url + '/list' + str(page_number)
        get_news_url = path
        #get_news_url = path
    else:
        page_number = 1
        path = get_news_url + '/list' + str(page_number)
        #get_news_url = path
    return path


trash_symbols = '[\xa0\n\t\t\t]'


def get_news_from_topics(url):
    global topics_title, topics_url
    soup = BeautifulSoup(get_html(url), 'lxml')
    topics_title.clear()
    topics_url.clear()
    for a in soup.find_all('a', class_='story-title-link'):
        title = a.text

        # print(topics_title)
        final_title = re.sub(trash_symbols, ' ', title)
        topics_title.append(final_title.strip())
        topics_url.append(a.get('href'))

def get_news_from_user_topics(url):
    global personal_url, personal_title
    soup = BeautifulSoup(get_html(url), 'lxml')
    personal_url.clear()
    personal_title.clear()
    for a in soup.find_all('a', class_='story-title-link'):
        title = a.text

        print(topics_title)
        final_title = re.sub(trash_symbols, ' ', title)
        personal_title.append(final_title.strip())
        personal_url.append(a.get('href'))

def get_topic_descript_sakh(url):
    topic_desk.clear()
    soup = BeautifulSoup(get_html(url), 'lxml')
    for a in soup.find_all('p', class_='text-style-text'):
        desc = a.text
        final_desc = re.sub(trash_symbols, ' ', desc)
        topic_desk.append(final_desc.strip())


def pravitelstvo_getting(url):
    soup = BeautifulSoup(get_html(url), 'lxml')

    quotes = soup.find_all('td', class_='news_text')

    titles = []
    for item in quotes:
        title = item.find('a')
        titles.append(title.text)
    print(titles)




def create_user_news():
    if os.path.exists('config.txt'):
        us_pof.read_user_conf()
        for i in us_pof.user_fav_topic:
            get_news_from_user_topics(get_urls_from_topic(i))
        get_news_from_user_topics(get_urls_from_topic(us_pof.user_fav_city[0]))



#create_user_news()

#random.shuffle(personal_url)
#print(personal_url[0] + ' ' + get_title_from_url(personal_url[0]))
#get_news_from_topics(get_urls_from_topic('Политика'))
# get_topic_descript_sakh(topics_url[1])
# print(get_next_page(100))
# print(topic_desk)
# Debug
# i = input('Какие новости? ')
# get_news_from_topics(get_urls_from_topic(i))
# print(topics_title[0])
#
# get_news_from_topics(get_next_page(10))
# print(get_news_url)
# print(topics_title[0])
# get_news_from_topics(get_urls_from_topic('Бизнес'))
# print(f"Headder - {topics_title[0]} \nURL- {topics_url[0]}")
# get_news_from_topics(get_urls_from_topic('Южно-Сахалинск'))
# print(f"Headder - {topics_title[0]} \nURL- {topics_url[0]}")
# print(topics_title)
# get_news_from_topics(get_urls_from_topic('Южно-Сахалинск'))
# get_topic_descript_sakh(topics_url[1])
# print(topic_desk)
# get_news_from_topics(get_urls_from_topic('Анива'))
# get_topic_descript_sakh(topics_url[1])
# print(topic_desk)
# for o in topics_title:
#   print(topics_title[topics_title.index(o)])
