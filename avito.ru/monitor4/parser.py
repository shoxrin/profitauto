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
            'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36',
            'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Language':'ru,en-US;q=0.5',
            'Accept-Encoding':'gzip, deflate, br',
            'DNT':'1',
            'Connection':'keep-alive',
            'Upgrade-Insecure-Requests':'1',
            'Pragma':'no-cache',
            'Cache-Control':'no-cache'
        }
        #Прокси
        self.proxies = {
            'https': 'http://user65270:03kyol@185.120.76.193:5609',
            'http': 'http://user65270:03kyol@185.120.76.193:5609'
        }
        #Добавление прокси и заголовков к сессии
        #self.session.proxies = self.proxies
        self.session.headers = self.headers

    #Функция для получения объявлений
    def getHTML(self, url):
        response = self.session.get(url=url) #Создание запроса к сайту
        soup = BeautifulSoup(response.content, 'html.parser') #Парсинг ответа
        items = soup.find_all('div', class_ = 'iva-item-root-Nj_hb') #Формирование списка всех полученных объявлений
        print('[STATUS_CODE]:', response.status_code)

        return items

    #Функция для сортировки объявлений и получении нужной информации
    def getAnnouncements(self, url):
        items = self.getHTML(url)
        announcements = [] #Список с объявлениями
        #Перебор html блоков объявлений для дальнейшей обработки
        for item in items:
            link = item.find('a', class_ = 'link-link-MbQDP') #Ссылка объявления
            timeadd = item.find('div', class_ = 'date-text-VwmJG').text #Время создания объявления
            #Проверка для получения новых объявлений
            # or '2 минуты назад' == timeadd
            if ('Несколько секунд назад' == timeadd or '1 минуту назад' == timeadd) and not(link.get('href') in self.tmp):
                self.tmp.append(link.get('href')) #Добавление использованной ссылки объявления
                #Наполнение списка с новыми объявлениями
                announcements.append({
                    'title': link.text,
                    'price': item.find('span', class_ = 'price-text-E1Y7h').text,
                    'params': item.find('div', class_ = 'iva-item-text-_s_vh').text,
                    'geo': item.find('div', class_ = 'geo-georeferences-Yd_m5').text,
                    'img': item.find('img', class_ = 'photo-slider-image-_Dc4I'),
                    'link': 'https://www.avito.ru' + link.get('href'),
                    'time': timeadd
                })
                #Очистка хранилища использованных ссылок
                if len(self.tmp) == 30:
                    del self.tmp[0:14]
            else:
                break

        return announcements