import re
user_fav_city = ''
user_fav_topic = []

from pathlib import Path
def save_user_interest(city=None,*topics):
    with open('config.txt', 'w') as f:
        f.write(city + '\n')
        for i in topics:
            f.write(i + '\n')
            f.close


# save_user_interest("Южно-Сахалинск", "Авто", "Бизнес", "Политика")

trash_symb = '[\n]'
def read_user_conf():
    global user_fav_city
    my_file = Path('config.txt')
    with open('config.txt', 'r') as f:
            i = f.readlines()
            user_fav_city = i[0]
            print(i[0])

            for o in i[1:]:
                final = re.sub(trash_symb, ' ',o)
                user_fav_topic.append(final.strip())
            
read_user_conf()
