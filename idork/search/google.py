import requests
from ..exceptions import *
from bs4 import BeautifulSoup
from typing import List, Optional, Union

# ./idork/search/google.py
# Author: w4ne
# Date: 02/03/2022

class Google:

    user_agent = "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:97.0) Gecko/20100101 Firefox/97.0"

    def __init__(self, proxy_url: Optional[str] = None) -> None:
        self.proxy_url = proxy_url
        self.url_list = []
        self.headers = {"user-agent": self.user_agent}

    def search(self, query: Optional[str]=None, lang: str="en", results: int=5) -> List[Union[str, None]]:
        if not query: raise MissingArgument("Missing Argument: \"query\"")

        params = f"q={query}&lang={lang}&num={results}"
        resp = requests.get("https://www.google.com/search", params=params, proxies=dict(http=self.proxy_url), headers=self.headers)
        self._parse_resp(resp.text)

        return self.url_list

    def _parse_resp(self, html: str) -> None:
        soup = BeautifulSoup(html, "html.parser")
        find = soup.find_all("div", attrs={"class": "g"})

        for se in find:
            link = se.find('a', href=True)
            title = se.find('h3')
            if link and title:self.url_list.append(link['href'])
