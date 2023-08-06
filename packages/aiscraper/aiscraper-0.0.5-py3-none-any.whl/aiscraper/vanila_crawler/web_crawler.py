import time
from ratelimiter import RateLimiter
from robotexclusionrulesparser import RobotExclusionRulesParser
from requests_handler import RequestsHandler

class WebCrawler:
    def __init__(self, base_url, depth=2, delay=0):
        self.base_url = base_url
        self.depth = depth
        self.requests_handler = RequestsHandler()
        self.robots_parser = RobotExclusionRulesParser()
        self.limiter = RateLimiter(max_calls=1, period=delay)
        self._parse_robots()

    def _parse_robots(self):
        response = self.requests_handler.get_response(self.base_url + "/robots.txt")
        if response is not None:
            self.robots_parser.parse(response.text)

    def _crawl(self, url):
        if not self.robots_parser.is_allowed("*", url):
            print(f"Not allowed to crawl {url} by robots.txt")
            return []
        with self.limiter:
            response = self.requests_handler.get_response(url)
        if response is None:
            return []
        links = self.requests_handler.parse_links(response, self.base_url)
        print(f"Crawled {url} with {len(links)} links", end='\r')
        return links

    def _crawler(self):
        to_crawl = [self.base_url]
        crawled = {}
        for level in range(self.depth):
            print(f"Crawling level {level+1}...")
            next_to_crawl = []
            for url in to_crawl:
                if url not in crawled:
                    links = self._crawl(url)
                    crawled[url] = links
                    next_to_crawl.extend(links)
            to_crawl = next_to_crawl
        return crawled

    def get_crawled_links(self):
        tree = self._crawler()
        unique_links = set()
        for links in tree.values():
            unique_links.update(links)
        return unique_links
