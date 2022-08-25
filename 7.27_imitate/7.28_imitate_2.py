import pandas as pd
from datetime import datetime, timedelta

from scipy.stats.mstats import winsorize

original = pd.DataFrame(
    pd.read_csv(r'D:\7.24_BTC_price\ones_graded_placeAndQuarterModified_withCoinID_withBTC_7.24_washed.csv'))

'''缩尾处理'''
original['image_text_prop'] = winsorize(original['image_text_prop'], limits=[0.05,0.05])

print(original.columns)
original.insert(original.shape[1],'ico_start_time',None)
original.insert(original.shape[1],'imitate_month_1',None)
original.insert(original.shape[1],'imitate_month_2',None)
original.insert(original.shape[1],'imitate_month_3',None)

for idx, data in original.iterrows():
    start_time = datetime.strptime(data['ico_start'].replace('/', '-'), '%Y-%m-%d')
    original.loc[idx,'ico_start_time'] = start_time


for idx, data in original.iterrows():
    end_time = data['ico_start_time']
    start_month_1 = end_time - timedelta(days= 30)
    month_1_total = 0.0
    month_1_count = 0

    start_month_2 = end_time - timedelta(days= 60)
    month_2_total = 0.0
    month_2_count = 0

    start_month_3 = end_time - timedelta(days= 90)
    month_3_total = 0.0
    month_3_count = 0

    for idx1, data1 in original.iterrows():
        this_time = data1['ico_start_time']
        this_prop = data1['image_text_prop']
        if this_time < end_time:
            if this_time > start_month_3:
                month_3_count = month_3_count + 1
                month_3_total = month_3_total + this_prop

                if this_time > start_month_2:
                    month_2_count = month_2_count + 1
                    month_2_total = month_2_total + this_prop

                    if this_time > start_month_1:
                        month_1_count = month_1_count +1
                        month_1_total = month_1_total + this_prop

    if month_3_count > 2 :
        original.loc[idx,'imitate_month_3'] = month_3_total / month_3_count

        if month_2_count > 2 :
            original.loc[idx, 'imitate_month_2'] = month_2_total / month_2_count

            if month_1_count > 2:
                original.loc[idx, 'imitate_month_1'] = month_1_total / month_1_count


original.to_csv(r'D:\7.28_imitate_2\ones_graded_placeAndQuarterModified_withCoinID_withBTC_imitate2_7.28_washed.csv',encoding='utf-8')