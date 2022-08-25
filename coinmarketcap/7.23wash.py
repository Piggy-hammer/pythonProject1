import pandas as pd

original = pd.DataFrame(pd.read_csv('D:/7.23_coinmarketcap_api/ones_graded_placeAndQuarterModified_withCoinID_7.23_washed.csv').set_index('id'))
# original.insert(original.shape[1],'coinmarketcap_identifer_washed',0)

print(original.columns)

for idx, data in original.iterrows():
    if pd.notnull(data['Coin_id']) :
        original.loc[idx,'coinmarketcap_identifer_washed'] = 1

for idx, data in original.iterrows():
    if data['Raised_Success']==1 or data['Coin_id'] == 1:
        original.loc[idx, 'ICO_Success'] = 1
    else:
        original.loc[idx, 'ICO_Success'] = 0

original.to_csv('D:/7.23_coinmarketcap_api/ones_graded_placeAndQuarterModified_withCoinID_7.23_washed.csv',encoding='utf-8')