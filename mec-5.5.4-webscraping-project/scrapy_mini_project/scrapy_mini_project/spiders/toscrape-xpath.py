import scrapy


class QuotesSpider(scrapy.Spider):
        name = "toscrape-xpath"
        start_urls = [
            'http://quotes.toscrape.com/page/1/',
        ]
        
        def parse(self, response):
            quotes = response.xpath('//div[@class="quote"]')
            for quote in quotes:
                
                yield {
                    'text':quote.xpath('.//span[@class="text"]/text()').get(),
                    'author':quote.xpath('.//small[@class="author"]/text()').get(),
                    'tags': quote.xpath('.//div[@class="tags"]/a[@class="tag"]/text()').getall()
                    
                }

            
            next_page = response.xpath('//li[@class="next"]/a/@href').get()
            print("########################################################")
            print(next_page)
            if next_page is not None:
                yield response.follow(next_page, callback=self.parse)

               
        