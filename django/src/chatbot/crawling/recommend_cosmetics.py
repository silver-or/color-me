from os import sep
from re import I
from urllib.request import urlopen

import numpy as np
import requests
from bs4 import BeautifulSoup
import pandas as pd
from sqlalchemy import false

class Cosmetics():
    def __init__(self) -> None:
        pass
    
    def recommend_cosmetics(self):
        item_info = []
        for page in range(35):
            url = 'https://www.colorize.co.kr/shop/board/list.php?id=beautypatch&page=' + str(page)
            html_doc = urlopen(url)
            soup = BeautifulSoup(html_doc, 'lxml')
            info = soup.find_all('td', {'class':'nwz-info'})

            for i in info:
                i = i.get_text().split(sep='\r\n\t\t\t\t')
                item_info.append([j.strip() for j in i])

        for i in item_info:
            del i[-1]

        df = pd.DataFrame(item_info, columns=['퍼스널컬러', '브랜드', '제품명'])
        df.dropna(axis=0, inplace=True)
        df.to_csv('../save/recommend_cosmetics.csv', encoding='utf-8')


if __name__ == '__main__':
    Cosmetics().recommend_cosmetics()
