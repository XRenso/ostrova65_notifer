import re
import os.path
user_fav_city = ''
user_fav_topic = []

from pathlib import Path

def save_user_interest(city=None, *topics):
   f = open('config.txt', 'w')
   f.write(city + '\n')
   for i in topics:
        f.write(i + '\n')
   f.close()




trash_symb = '[\n]'
def read_user_conf():
    global user_fav_city
    with open('config.txt', 'r') as f:
            i = f.readlines()
            fav_city = i[0]
            trash_symbols = '[\xa0\n\t\t\t]'
            user_fav_city = re.sub(trash_symbols,' ',fav_city).split()
            #print(i[0])

            for o in i[1:]:
                final = re.sub(trash_symb, ' ',o)
                user_fav_topic.append(final.strip())
            
if os.path.exists('config.txt'):
    read_user_conf()
