import time
import requests
from bs4 import BeautifulSoup


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
            'https': 'http://user65270:03kyol@45.91.160.125:8068',
            'http': 'http://user65270:03kyol@45.91.160.125:8068'

        }
        #Добавление прокси и заголовков к сессии
        self.session.proxies = self.proxies
        self.session.headers = self.headers

    #Функция для получения объявлений
    def getData(self, url, params):
        response = self.session.post(url=url, json=params) #Создание запроса к сайту
        data = response.json()
        print('[STATUS_CODE]:', response.status_code)
        return data['offers']

    def getTmp(self, url, params):
        data = self.getData(url, params)
        self.tmp.append(('https://auto.ru/' + data[4]['category'] + '/' + data[4]['section'] + '/sale/' + data[4]['vehicle_info']['mark_info']['code'] + '/' + data[4]['vehicle_info']['model_info']['code'] + '/' + data[4]['saleId']).lower())

    #Функция для сортировки объявлений и получении нужной информации
    def getOffers(self, url, params):
        data = self.getData(url, params)
        offers = [] #Список с объявлениями
        i = 0 #Переменная для перехода по объявлениям
        for offer in data: #len(data)-1 это количество пришедших объявлений
            if i >= 3:
                #offerTime = int(''.join(str(offer['additional_info']['creation_date']).split())[:-3])
                link = ('https://auto.ru/' + offer['category'] + '/' + offer['section'] + '/sale/' + offer['vehicle_info']['mark_info']['code'] + '/' + offer['vehicle_info']['model_info']['code'] + '/' + offer['saleId']).lower()
                if not(link in self.tmp):# and (time.time() - offerTime <= 60):
                    self.tmp.append(link)
                    offers.append({
                        'title': offer['vehicle_info']['mark_info']['name'] + ' ' + offer['vehicle_info']['model_info']['name'] + ' ' + str(offer['documents']['year']),
                        'price': str(offer['price_info']['price']) + '₽',
                        'probeg': str(offer['state']['mileage']) + 'км',
                        'params': offer['lk_summary'],
                        'geo': offer['seller']['location']['region_info']['name'],
                        'img': [('https:' + offer['state']['image_urls'][0]['sizes']['456x342'])],
                        'link': link,
                    })
                else:
                    break
            else:
                i += 1

        return offers
#
#p = Parser()
#pa = {
#    'section': "all",
#    'category': "cars",
#    'sort': "cr_date-desc",
#    'price_to': 300000,
#    'geo_id': [10174],
#    'top_days': "1"
#}
#while True:
#    ann = p.getOffers('https://auto.ru/-/ajax/desktop/listing/', pa)
#    if ann:
#        for an in ann:
#            print(an['title'])
#            print(an['link'])
#    else:
#        print('No offers')
#
#    time.sleep(10)