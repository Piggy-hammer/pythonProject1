from datetime import datetime
from datetime import timedelta
import calendar
import pandas as pd

original_BTC_price = pd.DataFrame(pd.read_csv(r'D:\7.24_BTC_price\BTC_price.csv'))
datestr = []

for e in original_BTC_price.date:
    day = e.split(' ')[0]
    datestr.append(day)

dates = pd.to_datetime(datestr)

original_BTC_price.insert(original_BTC_price.shape[1], 'dates', dates)
# original_BTC_price['dates'] = pd.to_datetime(original_BTC_price.dates).dt.tz_localize(None)

print(original_BTC_price['dates'].dtypes)
original_BTC_price = original_BTC_price.set_index('dates')

original_dataset = pd.DataFrame(
    pd.read_csv(r'D:\7.23_coinmarketcap_api\ones_graded_placeAndQuarterModified_withCoinID_7.23_washed.csv'))

original_dataset.insert(original_dataset.shape[1],'week_return_0',None)
original_dataset.insert(original_dataset.shape[1],'week_return_1',None)
original_dataset.insert(original_dataset.shape[1],'month_return_0',None)
original_dataset.insert(original_dataset.shape[1],'month_return_1',None)
original_dataset.insert(original_dataset.shape[1],'ICO_period_return',None)
original_dataset.insert(original_dataset.shape[1],'ICO_period_std',None)

for idx, data in original_dataset.iterrows():
    ico_start_time = datetime.strptime(data['ico_start'].replace('/', '-'), '%Y-%m-%d')
    ico_end_time = datetime.strptime(data['ico_end'].replace('/', '-'), '%Y-%m-%d')

    """本周的回报"""
    monday_0 = ico_start_time - timedelta(ico_start_time.weekday())
    sunday_0 = monday_0 + timedelta(6)
    week_return_0 = (original_BTC_price.loc[sunday_0, 'price'] - original_BTC_price.loc[monday_0, 'price']) / \
                    original_BTC_price.loc[monday_0, 'price']
    original_dataset.loc[idx,'week_return_0'] = week_return_0

    """上一周的回报"""
    monday_1 = monday_0 - timedelta(7)
    sunday_1 = monday_0 - timedelta(1)
    week_return_1 = (original_BTC_price.loc[sunday_1, 'price'] - original_BTC_price.loc[monday_1, 'price']) / \
                    original_BTC_price.loc[monday_1, 'price']
    original_dataset.loc[idx,'week_return_1'] = week_return_1

    """本月的回报"""
    first_day_month_0 = datetime(ico_start_time.year, ico_end_time.month, 1)
    last_day_month_0 = datetime(ico_start_time.year, ico_end_time.month, calendar.monthrange(ico_start_time.year,ico_end_time.month)[1])
    month_return_0 = (original_BTC_price.loc[last_day_month_0, 'price'] - original_BTC_price.loc[first_day_month_0, 'price']) / \
                    original_BTC_price.loc[first_day_month_0, 'price']
    original_dataset.loc[idx,'month_return_0'] = month_return_0

    """上一月的回报"""
    last_day_month_1 = first_day_month_0 - timedelta(1)
    first_day_month_1 = datetime(last_day_month_1.year, last_day_month_1.month, 1)
    month_return_1 = (original_BTC_price.loc[last_day_month_1, 'price'] - original_BTC_price.loc[first_day_month_1, 'price']) / \
                     original_BTC_price.loc[first_day_month_1, 'price']
    original_dataset.loc[idx, 'month_return_1'] = month_return_1

    """ICO期间的回报/波动率（标准差）"""
    ICO_period_return = (original_BTC_price.loc[ico_end_time, 'price'] - original_BTC_price.loc[ico_start_time, 'price']) / \
                     original_BTC_price.loc[ico_end_time, 'price']
    original_dataset.loc[idx, 'ICO_period_return'] = ICO_period_return

    price_series = original_BTC_price.loc[ico_start_time:ico_end_time,'price']
    ICO_period_std = price_series.std()
    original_dataset.loc[idx, 'ICO_period_std'] = ICO_period_std

original_dataset.to_csv(r'D:\7.24_BTC_price\ones_graded_placeAndQuarterModified_withCoinID_withBTC_7.24_washed.csv',encoding='utf-8')
