import time
from collections import deque
from urllib.parse import urlparse
from ratelimiter import RateLimiter
from robotexclusionrulesparser import RobotExclusionRulesParser
from .requests_handler import RequestsHandler

class WebCrawler:
    def __init__(self, base_url, depth=2, delay=0):
        self.base_url = base_url
        self.depth = depth
        self.requests_handler = RequestsHandler()
        self.robots_parser = RobotExclusionRulesParser()
        self.limiter = RateLimiter(max_calls=1, period=delay)
        self._parse_robots()

    def _parse_robots(self):
        try:
            response = self.requests_handler.get(self.base_url + "/robots.txt")
            self.robots_parser.parse(response.text)
        except Exception as e:
            print(f"Failed to parse robots.txt from {self.base_url}, reason: {e}")

    def is_valid(self, url):
        parsed = urlparse(url)
        return bool(parsed.netloc) and bool(parsed.scheme)

    def get_crawled_links(self):
        crawled = {}
        to_crawl = deque([(self.base_url, 0)])

        while to_crawl:
            url, depth = to_crawl.popleft()
            if depth > self.depth:
                continue
            if url not in crawled and self.robots_parser.is_allowed("*", url):
                try:
                    with self.limiter:
                        links = self.requests_handler.get_links(url)
                    crawled[url] = links
                    print(f"Crawled {url} with {len(links)} links", end='\r')
                    if depth < self.depth:
                        to_crawl.extend((link, depth + 1) for link in links if self.is_valid(link))
                except Exception as e:
                    print(f"Failed to crawl {url}, reason: {e}")
                time.sleep(self.delay)
        return crawled
