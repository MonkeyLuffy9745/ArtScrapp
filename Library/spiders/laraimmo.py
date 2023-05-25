from datetime import datetime
import scrapy
from model.models import Article
from model.repositories.website_repository import WebsiteRepository
from model.repositories.article_repository import ArticleRepository


class laraimmo(scrapy.Spider):
    website = WebsiteRepository.get_by_libelle("laraimmo")
    name = website.libelle
    
    def start_requests(self):
        urls = [
            self.website.link
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)



    def parse(self, response):
        print(f'\033[95mStart {self.website.libelle}\033[0m')
        
        for quote in response.css("div.col-3"):
            # print(quote.get())
            title = quote.css("a::text").get()
            print("title: ", title)
            link = quote.css("a::attr(href)").get()
            print("link: ", link)
            description = quote.css("p::text").get()
            print("description: ", description)
            if(ArticleRepository.get_by_link(link)):
                print(f'\nWarning: article ignored(already exists): {title}({link})')
            else:
                article = Article(title=title, link=link, description=description, created_at=f"{datetime.now().date()}",
                                website_id=self.website.id)
                ArticleRepository.store(article)
                print(f'\nSuccess: article saved: {title}({link})')
        print(f'\nEnd {self.website.name} with link:', f'{response.url}\n')
        # nextLink = response.css('a[rel="next"]::attr(href)').get()
        # if nextLink:
        #     yield scrapy.Request(url=nextLink, callback=self.parse)
        print(f'\033[91mEnd {self.website.libelle}\033[0m')
