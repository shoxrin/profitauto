import time
import logging
from config import URLS, WEBHOOK_URLS
import parser
from discord import Webhook, RequestsWebhookAdapter, Embed, Colour


class Monitor:
    def __init__(self, urls, webhook_urls):
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.INFO)

        c_handler = logging.StreamHandler()
        f_handler = logging.FileHandler('../logs/monitor1.log')
        c_handler.setLevel(logging.INFO)
        f_handler.setLevel(logging.INFO)

        c_format = logging.Formatter('[%(asctime)s][%(levelname)s]:%(message)s', datefmt='%H:%M:%S')
        f_format = logging.Formatter('[%(asctime)s][%(levelname)s]:%(message)s', datefmt='%H:%M:%S')
        c_handler.setFormatter(c_format)
        f_handler.setFormatter(f_format)

        self.logger.addHandler(c_handler)
        self.logger.addHandler(f_handler)

        self.urls = urls
        self.webhook_urls = webhook_urls
        self.parser = parser.Parser()
    
    def run(self):
        while True:
            try:
                for geo in self.urls:
                    for url in self.urls[geo]:
                        self.logger.info('Поиск новых объявлений! %s', str(geo) + ', ' + str(url))
                        announcements = self.parser.getAnnouncements(self.urls[geo][url])
                        if announcements:
                            for announcement in announcements:
                                self.logger.info('Подготовка - %s', announcement['title'] + ', ' + announcement['time'])
                                mesinfo = self.sendMessage(announcement, self.webhook_urls[geo][url])
                                if not(mesinfo):
                                    time.sleep(0.2)
                                    mesinfo = self.sendMessage(announcement, self.webhook_urls[geo][url])
                                time.sleep(3)
                        else:
                            self.logger.info('Новых объявлений нет!')
                        time.sleep(9)

                time.sleep(10)
            except:
                time.sleep(4)

    def sendMessage(self, announcement, webhook_url):
        webhook = Webhook.from_url(webhook_url, adapter=RequestsWebhookAdapter())
        
        embed = Embed(
                    color = Colour.blue(), 
                    title = announcement['title']
                )
        try:
            self.logger.info('Отправка - %s', announcement['title'] + ', ' + announcement['time'])
            if announcement['img']['src'] != 'None':
                embed.set_thumbnail(url = announcement['img']['src'])
                embed.add_field(name = 'Цена', value = announcement['price'])
                embed.add_field(name = 'Параметры', value = announcement['params'])
                embed.add_field(name = 'Местоположение', value = announcement['geo'])
                embed.add_field(name = 'Ссылка', value = announcement['link'])
                webhook.send(embed=embed)
            else:
                embed.add_field(name = 'Цена', value = announcement['price'])
                embed.add_field(name = 'Параметры', value = announcement['params'])
                embed.add_field(name = 'Местоположение', value = announcement['geo'])
                embed.add_field(name = 'Ссылка', value = announcement['link'])
                webhook.send(embed=embed)
            
            return True
        except:
            self.logger.info('Ошибка отправки!')
            return False

if __name__ == '__main__':
    Monitor(URLS, WEBHOOK_URLS).run()