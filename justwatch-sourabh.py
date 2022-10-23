import scrapy
from loguru import logger

class MovieInfo(scrapy.Spider):
    name="justwatch"
    def start_requests(self):
        urls = ['https://www.justwatch.com/ag/movie/k-g-f-chapter-1']
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        '''Parsing function to fetch required info'''
        movie_name = response.xpath("//div[@class='title-block']//div//h1/text()").extract()
        logger.info("Movie Name:: {}".format(movie_name))
        
        genre = set(response.xpath("//div[@class='detail-infos__value']//span/text()").extract())
        logger.info("Genre:: {}".format(genre))
        
        director_name = set(response.xpath("//div[@class='detail-infos__value']//span//a[@class='title-credit-name']/text()").extract())
        logger.info("Director Name:: {}".format(director_name))
        
        cast = set(response.xpath("//div[@class='hidden-horizontal-scrollbar__items']//div[@class='title-credits__actor']//a[@class='title-credit-name']/text()").extract())
        logger.info("Cast:: {}".format(cast))
        
        release_year = response.xpath("//div[@class='title-block']//div//span/text()").extract()
        logger.info("Release Year:: {}".format(release_year))
        
        # language = response.xpath().extract()
        # logger.info("Language:: {}".format(language))
        
        duration = set(response.xpath("//div[@class='detail-infos__value']/text()").extract())
        logger.info("Duration:: {}".format(duration))
        
        imdb_ratings = set(response.xpath("//div[@class='detail-infos__value']//div[@v-uib-tooltip='IMDB']//a/text()").extract())
        logger.info("IMDB Rating:: {}".format(imdb_ratings))
        
        movie_link = response.xpath("//div[@class='presentation-type price-comparison__grid__row__element__icon']/a/@href").extract()
        logger.info("Movie Link:: {}".format(movie_link))
