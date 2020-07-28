import requests
from typing import Dict
from bs4 import BeautifulSoup
from time import sleep
import json


baseurl = "https://wiki.lesswrong.com/wiki/RAZ_Glossary"


def download_html() -> str:
    """
    Download the html of the relative url
    """
    response = requests.get(baseurl)
    return response.text


def extract_keyword_def_map(html: str) -> Dict[str, str]:
    """
    Create a keyword -> definition dictionary from the html
    """

    soup = BeautifulSoup(html, 'html.parser')
    ret = {}
    for ul in soup.find_all('ul'):
        for li in ul.find_all('li'):
            title = li.find('b')
            if not title:
                continue
            ret[title.string] = li.decode_contents()
    return ret


def save_as_json(dic: Dict[str, str]) -> None:
    with open('keyword_def_map.json', 'w') as fp:
        json.dump(dic, fp)


if __name__ == "__main__":
    html = download_html()
    dic = extract_keyword_def_map(html)
    save_as_json(dic)
