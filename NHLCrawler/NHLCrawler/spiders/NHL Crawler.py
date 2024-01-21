from scrapy.spiders import CrawlSpider, Rule
from scrapy.Linkextractors import LinkExtractor


class CrawlingSpider (CrawlSpider):
    name = "NHLCrawler"
    
