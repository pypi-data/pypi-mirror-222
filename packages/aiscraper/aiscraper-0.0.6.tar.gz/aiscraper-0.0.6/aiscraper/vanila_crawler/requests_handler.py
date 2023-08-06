import requests
from bs4 import BeautifulSoup

class RequestsHandler:
    def __init__(self, user_agent='Mozilla/5.0'):
        self.headers = {'User-Agent': user_agent}

    def get_response(self, url):
        try:
            response = requests.get(url, headers=self.headers, timeout=30)
            response.raise_for_status()
        except (requests.HTTPError, requests.ConnectionError, requests.exceptions.Timeout) as e:
            print(f"Failed to get content from {url}, reason: {e}")
            return None
        return response

    def parse_links(self, response, base_url):
        soup = BeautifulSoup(response.text, "html.parser")
        links_crawled = []
        for link in soup.find_all('a', href=True):
            raw_link = link['href']
            if raw_link.startswith('/'):
                raw_link = base_url + raw_link
            if raw_link.startswith('http') and not (raw_link.endswith('.pdf') or raw_link.endswith('.mp4')):
                links_crawled.append(raw_link.replace(' ', '%20'))
        return list(set(links_crawled))
