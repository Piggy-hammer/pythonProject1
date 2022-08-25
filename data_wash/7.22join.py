import pandas as pd
from pandas import DataFrame

df_original: DataFrame = pd.DataFrame(pd.read_csv('D:\data_7.22\ones_graded_washed_original.CSV').set_index('id'))
df_grade = pd.DataFrame(pd.read_csv('D:\data_7.22\Grades_with_USD_raised_new_wash.csv').set_index('id'))

print(df_original.columns)
print(df_grade.columns)
without_identifer = []
drop_ones = []

for idx, data in df_original.iterrows():
    if data['Coinmarketcap_identifier'] == 0:
        without_identifer.append(idx)

for e in df_grade.index.values:
    if e in without_identifer:
        drop_ones.append(e)

print(drop_ones)

df_grade = df_grade.drop(index=drop_ones,axis=0)


for idx, data in df_grade.iterrows():
    df_original.loc[idx,'XYleaves'] = data['XYleaves']
    df_original.loc[idx,'textsNumbers'] = data['textsNumbers']
    df_original.loc[idx, 'maximumDecompositionLevel'] = data['maximumDecompositionLevel']
    df_original.loc[idx, 'averageDecompositionLevel'] = data['averageDecompositionLevel']
    df_original.loc[idx, 'imageArea'] = data['imageArea']
    df_original.loc[idx, 'textArea'] = data['textArea']
    df_original.loc[idx, 'image_text_prop'] = data['image_text_prop']
    df_original.loc[idx, 'image_text_index'] = data['image_text_index']
    df_original.loc[idx, 'quadleaves'] = data['quadleaves']
    df_original.loc[idx, 'equilibrium'] = data['equilibrium']
    df_original.loc[idx, 'H_balance'] = data['H_balance']
    df_original.loc[idx, 'H_Symmetry'] = data['H_Symmetry']
    df_original.loc[idx, 'V_Symmetry'] = data['V_Symmetry']
    df_original.loc[idx, 'nodeProportion'] = data['nodeProportion']
    df_original.loc[idx, 'TotalArea'] = data[' TotalArea']


df_original.to_csv('D:\data_7.22\ones_graded_washed_new_7.22_only_identifer.csv',encoding='utf-8-sig')
