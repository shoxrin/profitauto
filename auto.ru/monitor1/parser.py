import time
import requests
from bs4 import BeautifulSoup
from requests.sessions import session


class Parser:
    def __init__(self):
        self.tmp = [] #Временное хранилище ссылок для отправленных объявлений
        self.session = requests.Session() #Создание сессии
        #Заголовки 
        self.headers = {
            'Accept': '*/*',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3',
            'Connection': 'keep-alive',
            'Content-Length': '137',
            'content-type': 'application/json',
            'Cookie': '_csrf_token=1c0ed592ec162073ac34d79ce511f0e50d195f763abd8c24; autoru_sid=a%3Ag5e3b198b299o5jhpv6nlk0ro4daqbpf.fa3630dbc880ea80147c661111fb3270%7C1580931467355.604800.8HnYnADZ6dSuzP1gctE0Fw.cd59AHgDSjoJxSYHCHfDUoj-f2orbR5pKj6U0ddu1G4; autoruuid=g5e3b198b299o5jhpv6nlk0ro4daqbpf.fa3630dbc880ea80147c661111fb3270; suid=48a075680eac323f3f9ad5304157467a.bc50c5bde34519f174ccdba0bd791787; from_lifetime=1580933172327; from=yandex; X-Vertis-DC=myt; crookie=bp+bI7U7P7sm6q0mpUwAgWZrbzx3jePMKp8OPHqMwu9FdPseXCTs3bUqyAjp1fRRTDJ9Z5RZEdQLKToDLIpc7dWxb90=; cmtchd=MTU4MDkzMTQ3MjU0NQ==; yandexuid=1758388111580931457; bltsr=1; navigation_promo_seen-recalls=true',
            'Host': 'auto.ru',
            'origin': 'https://auto.ru',
            'Referer': 'https://auto.ru/ryazan/cars/mercedes/all/',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:72.0) Gecko/20100101 Firefox/72.0',
            'x-client-app-version': '202002.03.092255',
            'x-client-date': '1580933207763',
            'x-csrf-token': '1c0ed592ec162073ac34d79ce511f0e50d195f763abd8c24',
            'x-page-request-id': '60142cd4f0c0edf51f96fd0134c6f02a',
            'x-requested-with': 'fetch'
        }
        #Прокси
        self.proxies = {
            'https': 'http://user65270:03kyol@185.120.76.193:5609',
            'http': 'http://user65270:03kyol@185.120.76.193:5609'

        }
        self.params = {
            'section': "all",
            'category': "cars",
            'sort': "cr_date-desc",
            'price_to': 300000,
            'geo_id': [213]
        }
        #Добавление прокси и заголовков к сессии
        #self.session.proxies = self.proxies
        #self.session.headers = self.headers

    #Функция для получения объявлений
    def getData(self, url):
        response = requests.post(url=url, json=self.params, headers=self.headers, proxies=self.proxies)#self.session.post(url=url, json=self.params) #Создание запроса к сайту
        data = response
        print(response.json())
        return data

    #Функция для сортировки объявлений и получении нужной информации
    def getAnnouncements(self, url):
        data = self.getData(url)
        offers = [] #Список с объявлениями
        #if not(data[0]['saleId'] in self.tmp):
        #    offers.append(data[0]['saleId'])
        #    self.tmp.append(data[0]['saleId'])
        #Перебор html блоков объявлений для дальнейшей обработки
        i = 0 #Переменная для перехода по объявлениям
        #while i <= len(data) - 1: #len(data)-1 это количество пришедших объявлений
        #    if data
            # offers.append({
            #    'title': link.text,
            #    'price': item.find('span', class_ = 'ListingItemPrice__content').text,
            #    'params': item.find('div', class_ = 'ListingItemTechSummaryDesktop__column').text,
            #    'geo': item.find('span', class_ = 'MetroListPlace__regionName MetroListPlace_nbsp').text,
            #    #'img': item.find('img', class_ = 'LazyImage__image'),
            #    'link': 'https://auto.ru' + link.get('href'),
            #    #'time': timeadd
            #})

        return 

parser = Parser()
while True:
    an = parser.getAnnouncements('https://auto.ru/-/ajax/desktop/listing/')
    #print(an)
    time.sleep(10)