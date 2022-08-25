import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats.mstats import winsorize

original = pd.DataFrame(
    pd.read_csv(r'D:\7.24_BTC_price\ones_graded_placeAndQuarterModified_withCoinID_withBTC_7.24_washed_1.csv'))

'''缩尾处理'''
original['image_text_prop'] = winsorize(original['image_text_prop'], limits=[0.01,0.01])

'''编制imit列表（即每一期的平均image_Text_prop）'''
imit = original.groupby('ICO_quarter').mean()['image_text_prop']
print(imit)
# plt.plot(imit)
# plt.rcParams['figure.figsize'] = (8.0, 20.0)
# plt.subplots_adjust(left=0.1, right=0.9, top=0.9, bottom=0.1)
#plt.show()

years = ['2014Q4', '2016Q3', '2016Q4', '2017Q1', '2017Q2', '2017Q3', '2017Q4', '2018Q1', '2018Q2', '2018Q3', '2018Q4', '2019Q1',
         '2019Q2', '2019Q3', '2019Q4', '2020Q1', '2020Q2', '2020Q3']

original.insert(original.shape[1], 'imitate_0', None)
original.insert(original.shape[1], 'imitate_1', None)
original.insert(original.shape[1], 'imitate_05', None)
original.insert(original.shape[1], 'imitate_2', None)

for idx,data in original.iterrows():
    quarter = original.loc[idx,'ICO_quarter']
    imitate_0 = imit[quarter]
    original.loc[idx,'imitate_0'] = imitate_0
    index = years.index(quarter)

    if index > 3 and index < 15:
        quarter_1 = years[index-1]
        imitate_1 = imit[quarter_1]
        imitate_05 = (imitate_1 + imitate_0) / 2
        original.loc[idx, 'imitate_1'] = imitate_1
        original.loc[idx, 'imitate_05'] = imitate_05
        if index > 4:
            quarter_2 = years[index - 2]
            imitate_2 = imit[quarter_2]
            original.loc[idx, 'imitate_2'] = imitate_2

original.to_csv(r'D:\7.27_imitate\ones_graded_placeAndQuarterModified_withCoinID_withBTC_withimitate_7.27_washed.csv')