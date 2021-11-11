import requests

headers = {
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

session = requests.Session()

proxies = {
    'http': 'http://user65270:03kyol@45.91.160.125:18068',
    'https': 'http://user65270:03kyol@45.91.160.125:18068'

}
#Добавление прокси и заголовков к сессии
session.proxies = proxies
session.headers = headers

#session.cookies.clear()

r = session.get('https://youla.ru/sankt-peterburg/auto/s-probegom?attributes[auto_owner_type][0]=161309&attributes[price][to]=30000000&attributes[sort_field]=date_published&attributes[term_of_placement][from]=-1%20day&attributes[term_of_placement][to]=now')

print(r.status_code)