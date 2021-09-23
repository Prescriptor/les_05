import scrapy
from scrapy.http import HtmlResponse

#Подключаем класс из items.py <--
from bookparser.items import BookparserItem


class LabirintSpider(scrapy.Spider):
    name = 'labirint'
    allowed_domains = ['labirint.ru']
    start_urls = ['https://www.labirint.ru/genres/2380/']

    def parse(self, response: HtmlResponse):
        # Пагинируем <--
        next_page = response.xpath("//a[@class = 'pagination-next__text']/@href").extract_first()
        if next_page:
            yield response.follow(next_page, callback=self.parse)

        # Собираем ссылки на объекты <--
        links = response.xpath("//a[@class = 'cover']/@href").extract()
        for link in links:
            yield response.follow(link, callback=self.book_parse)


    def book_parse(self, response: HtmlResponse):
        book_name = response.xpath("//h1/text()").extract_first()
        book_autor = response.xpath("//authors/text()").extract()
        book_oldprice = response.css("div.buying-priceold-val span::text").extract_first()
        book_newprice = response.css("div.buying-pricenew-val span::text").extract_first()
        book_rating = response.xpath("//div[@id = 'rate']/text()").extract_first()
        book_url = response.url
        # assert isinstance(book_url, object)
        yield BookparserItem(name=book_name, autor=book_autor, oldprice=book_oldprice, newprice=book_newprice, rating=book_rating, url=book_url)


