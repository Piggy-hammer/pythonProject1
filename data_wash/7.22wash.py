from datetime import datetime
import pandas as pd

# original = pd.DataFrame(pd.read_csv('D:\data_7.22\ones_graded_washed_new_7.22.csv').set_index('id'))
#
# original.insert(original.shape[1], 'ICO_quarter',None)
#
# for idx, data in original.iterrows():
#     time = datetime.strptime(data['ico_start'].replace('/', '-'), '%Y-%m-%d')
#     original.loc[idx,'ICO_quarter'] = time
#
# original['ICO_quarter'] = pd.to_datetime(original['ICO_quarter'])
#
# original['ICO_quarter'] = original['ICO_quarter'].dt.to_period('Q')
#
# original.to_csv('D:\data_7.22\ones_graded_placeAndQuarterModified_7.22.csv',encoding='utf-8-sig')

original = pd.DataFrame(pd.read_csv('D:\data_7.22\ones_graded_washed_new_7.22_only_identifer.csv').set_index('id'))
company = pd.DataFrame(pd.read_csv('D:\data_7.22\ones_graded_placeAndQuarterModified_7.22.csv').set_index('id'))

original.insert(original.shape[1], 'ICO_quarter',None)

for idx, data in original.iterrows():
    time = datetime.strptime(data['ico_start'].replace('/', '-'), '%Y-%m-%d')
    original.loc[idx,'ICO_quarter'] = time
    original.loc[idx,'country'] = company[idx,'country']

original['ICO_quarter'] = pd.to_datetime(original['ICO_quarter'])

original['ICO_quarter'] = original['ICO_quarter'].dt.to_period('Q')

original.to_csv('D:\data_7.22\ones_graded_placeAndQuarterModified_7.22_only_identifer.csv',encoding='utf-8-sig')
