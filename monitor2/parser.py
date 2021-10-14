import time
import requests
from bs4 import BeautifulSoup
from requests.sessions import session


class Parser:
    def __init__(self):
        self.tmp = []
        self.session = requests.Session()
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
        self.proxies = {
            'https': 'http://user65270:03kyol@185.120.76.193:5609',
            'http': 'http://user65270:03kyol@185.120.76.193:5609'
        }

        self.session.proxies = self.proxies
        self.session.headers = self.headers

    def getHTML(self, url):
        response = self.session.get(url=url)
        soup = BeautifulSoup(response.content, 'html.parser')
        items = soup.find_all('div', class_ = 'iva-item-root-Nj_hb')
        print('[STATUS_CODE]:', response.status_code)

        return items

    def getAnnouncements(self, url):
        items = self.getHTML(url)
        announcements = []
        for item in items:
            link = item.find('a', class_ = 'link-link-MbQDP')
            timeadd = item.find('div', class_ = 'date-text-VwmJG').text
            if ('Несколько секунд назад' == timeadd or '1 минуту назад' == timeadd or '2 минуты назад' == timeadd) and not(link.get('href') in self.tmp):
                self.tmp.append(link.get('href'))
                announcements.append({
                    'title': link.text,
                    'price': item.find('span', class_ = 'price-text-E1Y7h').text,
                    'params': item.find('div', class_ = 'iva-item-text-_s_vh').text,
                    'geo': item.find('div', class_ = 'geo-georeferences-Yd_m5').text,
                    'img': item.find('img', class_ = 'photo-slider-image-_Dc4I'),
                    'link': 'https://www.avito.ru' + link.get('href'),
                    'time': timeadd
                })
                if len(self.tmp) == 30:
                    del self.tmp[0:14]
            else:
                break

        return announcements