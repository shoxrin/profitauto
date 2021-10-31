import time
import requests
from bs4 import BeautifulSoup


class Parser:
    def __init__(self):
        self.tmp = [] #Временное хранилище ссылок для отправленных объявлений
        self.session = requests.Session() #Создание сессии
        #Заголовки 
        self.headers = {
            "accept": "application/json, text/javascript, */*; q=0.01",
            "accept-encoding": "gzip, deflate",
            "accept-language": "en-US,en;q=0.9,fr-DZ;q=0.8,fr;q=0.7",
            "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "same-origin",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36",
            "x-requested-with": "XMLHttpRequest"
        }
        #Прокси
        self.proxies = {
            'https': 'http://user65270:03kyol@185.120.76.193:5609',
            'http': 'http://user65270:03kyol@185.120.76.193:5609'
        }
        #Добавление прокси и заголовков к сессии
        self.session.proxies = self.proxies
        self.session.headers = self.headers

    #Функция для получения объявлений
    def getHTML(self, url):
        response = self.session.get(url=url) #Создание запроса к сайту
        soup = BeautifulSoup(response.content, 'html.parser')
        items = soup.find_all('a', attrs={'data-ftid': 'bulls-list_bull'})
        print('[STATUS_CODE]:', response.status_code)
        while response.status_code == 429:
            time.sleep(600)
            response = self.session.get(url=url) #Создание запроса к сайту
            soup = BeautifulSoup(response.content, 'html.parser') #Парсинг ответа
            items = soup.find_all('a', attrs={'data-ftid': 'bulls-list_bull'}) #Формирование списка всех полученных объявлений
            print('[STATUS_CODE]:', response.status_code)
        return items

    #Функция для сортировки объявлений и получении нужной информации
    def getAnnouncements(self, url):
        items = self.getHTML(url)
        announcements = [] #Список с объявлениями
        #Перебор html блоков объявлений для дальнейшей обработки
        for item in items:
            link = item.get('href') #Ссылка объявления
            timeadd = item.find('div', attrs={'data-ftid': 'bull_date'}).text #Время создания объявления
            print(timeadd)
            #Проверка для получения новых объявлений
            # or '2 минуты назад' == timeadd
            if (timeadd == '1 минуту назад' or timeadd == 'Несколько секунд назад') and not(item.find('div', class_='css-x98spp e1vivdbi1')) and not(link in self.tmp):
                self.tmp.append(link) #Добавление использованной ссылки объявления
                #Наполнение списка с новыми объявлениями
                announcements.append({
                    'title': item.find('div', class_='css-1svsmzw e1vivdbi2').find('span').text,
                    'price': item.find('span', class_="css-bhd4b0 e162wx9x0").text,
                    'params': item.find('div', class_='css-3xai0o e162wx9x0').text,
                    'geo': item.find('span', class_="css-fbscyn e162wx9x0").text.split()[0],
                    'img': item.find('div', attrs={'data-ftid': 'bull_image'}).find('noscript').find('img'),
                    'link': link,
                    'time': timeadd 
                })
                #Очистка хранилища использованных ссылок
                if len(self.tmp) == 30:
                    del self.tmp[0:14]
            else:
                break

        return announcements


#p = Parser()
#
#while True:
#    ann = p.getAnnouncements('https://auto.drom.ru/region78/?maxprice=300000')
#    if ann:
#        for an in ann:
#            print(an['link'])
#            print(an['title'])
#            print(an['params'])
#            time.sleep(2)
#    else:
#        print('No offers')
#
#    time.sleep(10)