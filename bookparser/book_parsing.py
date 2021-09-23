from scrapy.crawler import CrawlerProcess
from scrapy.settings import Settings
from bookparser import settings  # добавляем персональные настройки settings.py  <--

# указываем местоположение класса осуществляющего опрос  <--
from bookparser.spiders.labirint import LabirintSpider

if __name__ == '__main__':
    crawler_settings = Settings()  # берём настройки
    crawler_settings.setmodule('bookparser.settings')  # добавляем персональные настройки<--

    crawler_proc = CrawlerProcess(settings=crawler_settings)  # запускаем процесс
    crawler_proc.crawl(LabirintSpider)  # добавляем имена нужных пауков <--

    crawler_proc.start()  # стартуем выполнение
