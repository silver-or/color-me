import pandas as pd


class Recommend:
    def __init__(self) -> None:
        self.data = pd.read_csv('./save/recommend_cosmetics.csv', encoding='utf-8')

    def spring(self):
        return self.data.loc[self.data['퍼스널컬러']=='봄웜'].iloc[:, 2:4].sample()

    def summer(self):
        return self.data.loc[self.data['퍼스널컬러']=='여름쿨'].iloc[:, 2:4].sample()

    def fall(self):
        return self.data.loc[self.data['퍼스널컬러']=='가을웜'].iloc[:, 2:4].sample()

    def winter(self):
        return self.data.loc[self.data['퍼스널컬러']=='겨울쿨'].iloc[:, 2:4].sample()