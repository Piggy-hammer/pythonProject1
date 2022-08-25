import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats.mstats import winsorize

original = pd.DataFrame(
    pd.read_csv(r'D:\7.24_BTC_price\ones_graded_placeAndQuarterModified_withCoinID_withBTC_7.24_washed_1.csv')).set_index('id')

original.insert(original.shape[1], 'image_text_minus',None)



for inde, rows in original.iterrows():
    original.loc[inde,'image_minus_text'] = original.loc[inde,'image_prop'] - original.loc[inde,'text_prop']

'''缩尾处理'''
original['image_minus_text'] = winsorize(original['image_minus_text'], limits=[0.05,0.05])


'''编制imit列表（即每一期的平均image_Text_prop）'''
imit = original.groupby('ICO_quarter').mean()['image_minus_text']
print(imit)

years = ['2014Q4', '2016Q3', '2016Q4', '2017Q1', '2017Q2', '2017Q3', '2017Q4', '2018Q1', '2018Q2', '2018Q3', '2018Q4', '2019Q1',
         '2019Q2', '2019Q3', '2019Q4', '2020Q1', '2020Q2', '2020Q3']

original.insert(original.shape[1], 'imitate_minus_0', None)
original.insert(original.shape[1], 'imitate_minus_1', None)
original.insert(original.shape[1], 'imitate_minus_05', None)
original.insert(original.shape[1], 'imitate_minus_2', None)
original.insert(original.shape[1], 'imitate_minus_15', None)
original.insert(original.shape[1], 'imitate_minus_semi_ann', None)
print(original.columns)

for idx,data in original.iterrows():
    quarter = original.loc[idx,'ICO_quarter']

    index = years.index(quarter)

    if index > 3:
        imitate_0 = imit[quarter]
        original.loc[idx, 'imitate_minus_0'] = imitate_0

    if index > 3 and index < 15:
        quarter_1 = years[index-1]
        imitate_1 = imit[quarter_1]
        imitate_05 = (imitate_1 + imitate_0) / 2

        original.loc[idx, 'imitate_minus_1'] = imitate_1
        original.loc[idx, 'imitate_minus_05'] = imitate_05

        if index > 4:
            quarter_2 = years[index - 2]
            imitate_2 = imit[quarter_2]
            original.loc[idx, 'imitate_minus_2'] = imitate_2
            imitate_15 = (imitate_1 + imitate_2) / 2
            original.loc[idx, 'imitate_minus_15'] = imitate_15
            imitate_ann = (imitate_1 + imitate_2 + imitate_0) / 3
            original.loc[idx, 'imitate_minus_semi_ann'] = imitate_ann

imit_success = original[original['ICO_Success'] == 1].groupby('ICO_quarter').mean()['image_minus_text']
print(imit_success)

original.insert(original.shape[1], 'success_imitate_minus_0', None)
original.insert(original.shape[1], 'success_imitate_minus_1', None)
original.insert(original.shape[1], 'success_imitate_minus_05', None)
original.insert(original.shape[1], 'success_imitate_minus_2', None)
original.insert(original.shape[1], 'success_imitate_minus_15', None)
original.insert(original.shape[1], 'success_imitate_minus_semi_ann', None)
print(original.columns)

for idx,data in original.iterrows():
    quarter = original.loc[idx,'ICO_quarter']

    index = years.index(quarter)

    if index > 3 and index < 16:
        imitate_0 = imit_success[quarter]
        original.loc[idx, 'success_imitate_minus_0'] = imitate_0
        quarter_1 = years[index-1]
        imitate_1 = imit_success[quarter_1]
        imitate_05 = (imitate_1 + imitate_0) / 2

        original.loc[idx, 'success_imitate_minus_1'] = imitate_1
        original.loc[idx, 'success_imitate_minus_05'] = imitate_05

        if index > 4:
            quarter_2 = years[index - 2]
            imitate_2 = imit_success[quarter_2]
            original.loc[idx, 'success_imitate_minus_2'] = imitate_2
            imitate_15 = (imitate_1 + imitate_2) / 2
            original.loc[idx, 'success_imitate_minus_15'] = imitate_15
            imitate_ann = (imitate_1 + imitate_2 + imitate_0) / 3
            original.loc[idx, 'success_imitate_minus_semi_ann'] = imitate_ann


original.to_csv(r'D:\8.18_minus_imitate_3\ones_graded_place_Minus_AndQuarterModified_withCoinID_withBTC_withimitate_8.19_washed.csv')

