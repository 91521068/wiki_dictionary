import scrapy


class QuotesSpider(scrapy.Spider):
    name = "quotes"
    start_urls = [
        'http://quotes.toscrape.com/page/1/',
        'http://quotes.toscrape.com/page/2/',
    ]

    def parse(self, response):
        for quote in response.xpath('//div[@class="quote"]'):
            text = quote.xpath('span[@class="text"]/text()').extract_first()
            author = quote.xpath('span/small/text()').extract_first()
            print(u'{}: {}'.format(author, text))
