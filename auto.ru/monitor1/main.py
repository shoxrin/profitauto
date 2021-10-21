import time
import logging
from config import PARAMS, WEBHOOK_URLS
import parser
from discord import Webhook, RequestsWebhookAdapter, Embed, Colour


class Monitor:
    def __init__(self, params, webhook_urls):
        self.logger = logging.getLogger(__name__) #логер
        self.get_logger() #Вызов функции для настройки логгера
        self.params = params #Список url для запросов
        self.url = 'https://auto.ru/-/ajax/desktop/listing/'
        self.webhook_urls = webhook_urls #Список вебхуков
        self.parser = parser.Parser() #Создание объекта парсера
        self.parser.status = True 
    
    #Функция запуска монитора
    def run(self):
        while True:
            try:
                #Перебор регионов
                for geo in self.webhook_urls:
                    #Перебор url запросов
                    for webhook_url in self.webhook_urls[geo]:
                        self.logger.info('Поиск новых объявлений! %s', str(geo) + ', ' + str(webhook_url))
                        #Список объявлений
                        announcements = self.parser.getOffers(self.url, self.params[geo][webhook_url])
                        #Если есть объявления
                        if announcements:
                            #Перебор объявлений
                            for announcement in announcements:
                                self.logger.info('Отправка - %s', announcement['title'])
                                #Отпрака объявления в дискорд
                                mesinfo = self.sendMessage(announcement, self.webhook_urls[geo][webhook_url])
                                #Если объявление не отпраленно
                                if not(mesinfo):
                                    time.sleep(3)
                                    self.logger.info('Повторная отправка - %s', announcement['title'])
                                    #Повторная отправка
                                    mesinfo = self.sendMessage(announcement, self.webhook_urls[geo][webhook_url])
                                time.sleep(1)
                        #Если нет объявлений
                        else:
                            self.logger.info('Новых объявлений нет!')
                        time.sleep(10)
                #Задержка перед следуюшим регионом
                time.sleep(5)
            except Exception as ex:
                #Вслучае ошибки
                print(ex)
                time.sleep(5)

    #Отправка объявления в канал
    def sendMessage(self, announcement, webhook_url):
        #Создание вебхука
        webhook = Webhook.from_url(webhook_url, adapter=RequestsWebhookAdapter()) 
        #Создание вставки сообщения
        embed = Embed(
                    color = Colour.blue(), 
                    title = announcement['title']
                )
        try:
            #Если объявление содержит изображение
            if announcement['img']:
                embed.set_thumbnail(url = announcement['img'][0]['src'])
                embed.add_field(name = 'Цена', value = announcement['price'])
                embed.add_field(name = 'Параметры', value = announcement['params'])
                embed.add_field(name = 'Местоположение', value = announcement['geo'])
                embed.add_field(name = 'Ссылка', value = announcement['link'])
                webhook.send(embed=embed)
                self.logger.info('Отправлено - %s', announcement['title'])
            #Если объявление не содержит изображение
            else:
                embed.add_field(name = 'Цена', value = announcement['price'])
                embed.add_field(name = 'Параметры', value = announcement['params'])
                embed.add_field(name = 'Местоположение', value = announcement['geo'])
                embed.add_field(name = 'Ссылка', value = announcement['link'])
                webhook.send(embed=embed)
                self.logger.info('Отправлено - %s', announcement['title'])
            
            return True
        except Exception as ex:
            self.logger.error('Ошибка отправки! %s', ex)
            return False

    #Создание логгера
    def get_logger(self):
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

if __name__ == '__main__':
    Monitor(PARAMS, WEBHOOK_URLS).run()