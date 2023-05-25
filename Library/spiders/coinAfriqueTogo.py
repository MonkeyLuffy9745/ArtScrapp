import scrapy
from model.models import Article
from model.repositories.website_repository import WebsiteRepository
from model.repositories.article_repository import ArticleRepository


class coinAfriqueTogo(scrapy.Spider):
    website = WebsiteRepository.get_by_libelle("coin-afrique-togo")
    name = website.libelle
    
    def start_requests(self):
        urls = [
            self.website.link
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)



    def parse(self, response):
        print(f'\033[95mStart {self.website.libelle}\033[0m')
        
        for quote in response.css("div.card"):
            print(quote.get())
        #     title = quote.css("h2::text").get()
        #     link = quote.css("a::attr(href)").get()
        #     content = quote.css("p::text")[-3].get()
        #     if(ArticleRepository.get_by_link(link)):
        #         print(Formatter.warning(f'\nWarning: article ignored(already exists): {title}({link})'))
        #     else:
        #         article = Article(title=title, link=link, content=content, created_at=f"{datetime.now().date()}",
        #                         website_token=self.website.token)
        #         ArticleRepository.store(article)
        #         print(Formatter.ok_green(f'\nSuccess: article saved: {title}({link})'))
        # print(f'\nEnd {self.website.name} with link:', Formatter.ok_blue(f'{Formatter.bold(response.url)}\n'))
        # nextLink = response.css('a[rel="next"]::attr(href)').get()
        # if nextLink:
        #     yield scrapy.Request(url=nextLink, callback=self.parse)
        print(f'\033[91mEnd {self.website.libelle}\033[0m')
