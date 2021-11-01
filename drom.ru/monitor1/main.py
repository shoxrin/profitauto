import time
import logging

import discord
from config import URLS, WEBHOOK_URLS
import parser
from discord import Webhook, RequestsWebhookAdapter, Embed, Colour


class Monitor:
    def __init__(self, urls, webhook_urls):
        self.logger = logging.getLogger(__name__) #логер
        self.get_logger() #Вызов функции для настройки логгера
        self.urls = urls #Список url для запросов
        self.webhook_urls = webhook_urls #Список вебхуков
        self.parser = parser.Parser(self.logger) #Создание объекта парсера
    
    #Функция запуска монитора
    def run(self):
        while True:
            #try:
            #Перебор регионов
            for geo in self.urls:
                #Перебор url запросов
                for url in self.urls[geo]:
                    self.logger.info('Поиск новых объявлений! %s', str(geo) + ', ' + str(url))
                    #Список объявлений
                    announcements = self.parser.getAnnouncements(self.urls[geo][url])
                    #Если есть объявления
                    if announcements:
                        #Перебор объявлений
                        for announcement in announcements:
                            self.logger.info('Отправка - %s', announcement['title'] + ', ' + announcement['time'])
                            #Отпрака объявления в дискорд
                            mesinfo = self.sendMessage(announcement, self.webhook_urls[geo][url])
                            #Если объявление не отпраленно
                            if not(mesinfo):
                                time.sleep(3)
                                self.logger.info('Повторная отправка - %s', announcement['title'] + ', ' + announcement['time'])
                                #Повторная отправка
                                mesinfo = self.sendMessage(announcement, self.webhook_urls[geo][url])
                            time.sleep(1)
                    #Если нет объявлений
                    else:
                        self.logger.info('Новых объявлений нет!')
                    time.sleep(10)
            #Задержка перед следуюшим регионом
            time.sleep(8)
            #except Exception as ex:
            ##    self.logger.error('Ошибка! %s', ex)
            ##    #Вслучае ошибки
            #    time.sleep(5)

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
            if not(announcement['img'] is None):
                embed.set_thumbnail(url = announcement['img'])
                embed.add_field(name = 'Цена', value = announcement['price'])
                embed.add_field(name = 'Параметры', value = announcement['params'])
                embed.add_field(name = 'Пробег', value = announcement['probeg'])
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
    Monitor(URLS, WEBHOOK_URLS).run()