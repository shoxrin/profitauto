import time
import logging
from datetime import datetime
import requests
from bs4 import BeautifulSoup


class Parser:
    def __init__(self, logger):
        self.tmp = [] #Временное хранилище ссылок для отправленных объявлений
        self.session = requests.Session() #Создание сессии
        #self.logger = logging.getLogger(__name__)
        #self.get_logger()
        self.logger = logger
        #Заголовки 
        self.headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
            'Cache-Control': 'max-age=0',
            'Connection': 'keep-alive',
            'Host': 'youla.ru',
            'Referer': 'https://youla.ru/',
            'sec-ch-ua': '"Google Chrome";v="95", "Chromium";v="95", ";Not A Brand";v="99"',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.0; WOW64; rv:24.0) Gecko/20100101 Firefox/24.0'
        }
        #Прокси
        self.proxies = {
            #'https': 'http://user65270:03kyol@45.91.160.125:18068',
            'http': 'http://user65270:03kyol@45.91.160.125:18068'

        }
        #Добавление прокси и заголовков к сессии
        self.session.proxies = self.proxies
        self.session.headers = self.headers
        #self.session.cookies.clear()

    #Функция для получения объявлений
    def getHTML(self, url):
        response = self.session.get(url=url) #Создание запроса к сайту
        soup = BeautifulSoup(response.content, 'html.parser')
        items = soup.find_all('li', class_='product_item')
        self.logger.info('[STATUS_CODE]:%s', response.status_code)
        while response.status_code == 429:
            time.sleep(600)
            response = self.session.get(url=url) #Создание запроса к сайту
            items = soup.find_all('li', class_='product_item')
            self.logger.info('[STATUS_CODE]:%s', response.status_code)

        return items

    #Функция для сортировки объявлений и получении нужной информации
    def getAnnouncements(self, url):
        items = self.getHTML(url)
        announcements = [] #Список с объявлениями
        #Перебор html блоков объявлений для дальнейшей обработки
        for item in items:
            if not('product_item--promoted' in item.get('class')):
                link = item.find('a') #Ссылка объявления
                timeadd = item.find('div', class_='product_item__date').text #Время создания объявления              
                dateadd = str(timeadd.split(' ')[0])
                timeadd = str(str(timeadd.split(' ')[len(timeadd.split(' '))-1]).split('.')[0])[:-2]
                timeaddif = int(timeadd.split(':')[0]) * 60 * 60 + int(timeadd.split(':')[1]) * 60
                timenow = datetime.now().time().hour * 60 * 60 + datetime.now().time().minute * 60
                #Проверка для получения новых объявлений
                # or '2 минуты назад' == timeadd
                #if item.find('div', class_='css-x98spp e1vivdbi1') is None:
                if (timenow - timeaddif <= 120 and timenow - timeaddif >= 0 and dateadd == 'сегодня') and not(link.get('href') in self.tmp):
                    self.tmp.append(link.get('href')) #Добавление использованной ссылки объявления
                    #Наполнение списка с новыми объявлениями
                    img = item.find('div', class_='product_item__image').find('image')
                    announcements.append({
                        'title': link.get('title').strip(),
                        'price': item.find('div', class_="product_item__description").text.strip(),
                        'params': '',
                        'geo': item.find('span', class_='product_item__location').text,
                        'img': img,
                        'link': 'https://youla.ru' + str(link.get('href')),
                        'time': timeadd,
                        'ts': [timenow, timeaddif]
                    })

            #Очистка хранилища использованных ссылок
            if len(self.tmp) == 30:
                del self.tmp[0:14]

        return announcements

        #Создание логгера
    def get_logger(self):
        self.logger.setLevel(logging.INFO)

        c_handler = logging.StreamHandler()
        f_handler = logging.FileHandler('../profitauto/youla.ru/logs/monitor1.log')
        c_handler.setLevel(logging.INFO)
        f_handler.setLevel(logging.INFO)

        c_format = logging.Formatter('[%(asctime)s][%(levelname)s]:%(message)s', datefmt='%H:%M:%S')
        f_format = logging.Formatter('[%(asctime)s][%(levelname)s]:%(message)s', datefmt='%H:%M:%S')
        c_handler.setFormatter(c_format)
        f_handler.setFormatter(f_format)

        self.logger.addHandler(c_handler)
        self.logger.addHandler(f_handler)

#p = Parser()
#while True:
#    ann = p.getAnnouncements('https://youla.ru/sankt-peterburg/auto/s-probegom?attributes[auto_owner_type][0]=161309&attributes[price][to]=30000000&attributes[sort_field]=date_published&attributes[term_of_placement][from]=-1%20day&attributes[term_of_placement][to]=now')
#    if ann:
#        for an in ann:
#            print(an['link'])
#            print(an['title'])
#            print(an['price'])
#            time.sleep(2)
#    else:
#        print('No offers')
#
#    time.sleep(10)