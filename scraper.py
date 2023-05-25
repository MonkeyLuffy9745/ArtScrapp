from model.repositories.website_repository import WebsiteRepository
WebsiteRepository.connect()
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from Library.spiders.coinAfriqueTogo import coinAfriqueTogo
from Library.spiders.laraimmo import laraimmo

if __name__ == "__main__":
    process = CrawlerProcess(settings=get_project_settings())
    process.crawl(laraimmo)
    process.start()