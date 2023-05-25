import importlib
import sys
from model.repositories.website_repository import WebsiteRepository
WebsiteRepository.connect()
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings


if __name__ == "__main__":
    # website: Website = WebsiteRepository.get_by_slug("laragrafikart")
    module = importlib.import_module(f"lib.scraping.spiders.{website.slug}_spider")
    spider_class = getattr(module, f"{website.slug.capitalize()}Spider")
    process = CrawlerProcess(settings=get_project_settings())
    process.crawl(spider_class)
    process.start()