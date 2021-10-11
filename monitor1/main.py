import time
from config import URLS, WEBHOOK_URLS
import parser
from discord import Webhook, RequestsWebhookAdapter, Embed, Colour


class Monitor:
    def __init__(self, urls, webhook_urls):
        self.urls = urls
        self.webhook_urls = webhook_urls
        self.parser = parser.Parser()
    
    def run(self):
        while True:
            print('[INFO]: Поиск новых объявлений!')
            for geo in self.urls:
                print('[INFO]: ', geo)
                for url in self.urls[geo]:
                    announcements = self.parser.getAnnouncements(self.urls[geo][url])
                    print('[INFO]: ', url)
                    if announcements:
                        for announcement in announcements:
                            print('[INFO]: Отправка - ', announcement['title'])
                            self.sendMessage(announcement, self.webhook_urls[geo][url])
                            time.sleep(1)
                    else:
                        print('[INFO]: Новых объявлений нет!')
                    time.sleep(10)

            time.sleep(10)

    def sendMessage(self, announcement, webhook_url):
        webhook = Webhook.from_url(webhook_url, adapter=RequestsWebhookAdapter())
        
        embed = Embed(
                    color = Colour.blue(), 
                    title = announcement['title']
                )
        try:
            embed.set_thumbnail(url = announcement['img']['src'])
            embed.add_field(name = 'Цена', value = announcement['price'])
            embed.add_field(name = 'Параметры', value = announcement['params'])
            embed.add_field(name = 'Местоположение', value = announcement['geo'])
            embed.add_field(name = 'Ссылка', value = announcement['link'])

            webhook.send(embed=embed)
        except:
            embed.add_field(name = 'Цена', value = announcement['price'])
            embed.add_field(name = 'Параметры', value = announcement['params'])
            embed.add_field(name = 'Местоположение', value = announcement['geo'])
            embed.add_field(name = 'Ссылка', value = announcement['link'])

            webhook.send(embed=embed)

if __name__ == '__main__':
    Monitor(URLS, WEBHOOK_URLS).run()