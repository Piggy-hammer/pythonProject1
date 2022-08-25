import pandas as pd

df_original = pd.DataFrame(pd.read_csv('D:\\tord_v3_mod2.csv').set_index('id'))
df_grade = pd.DataFrame(pd.read_csv('D:\data_7.22\Grades_with_USD_raised_new_wash.csv').set_index('id'))
df = pd.concat([df_grade,df_original],axis=1)
df.to_csv('D:\data_7.22\ones_graded_new_wash_7.22.csv',encoding='utf-8-sig')
# df_original = pd.DataFrame(pd.read_csv('D:\\ones_graded.csv').set_index('id'))
# df_grade = pd.DataFrame(pd.read_csv('D:\\Grades_with_USD_raised_append.csv').set_index('id'))
# df = pd.concat([df_grade,df_original],axis=1)
# df.to_csv('D:\\ones_graded_append.csv',encoding='utf-8-sig')
