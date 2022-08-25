import pandas as pd
import os
import numpy as np

# Folder_Path = 'D:\\7.23_coinmarketcap_api\\in_5000'  # 要拼接的文件夹及其完整路径，注意不要包含中文
# SaveFile_Path = 'D:\\7.23_coinmarketcap_api'  # 拼接后要保存的文件路径
# SaveFile_Name = 'all_coin_id.csv'  # 合并后要保存的文件名
#
# # 修改当前工作目录
# os.chdir(Folder_Path)
# # 将该文件夹下的所有文件名存入一个列表
# file_list = os.listdir()
#
# # 读取第一个CSV文件并包含表头
# df = pd.read_csv(Folder_Path + '\\' + file_list[0])  # 编码默认UTF-8，若乱码自行更改
#
# # 将读取的第一个CSV文件写入合并后的文件保存
# df.to_csv(SaveFile_Path + '\\' + SaveFile_Name, encoding="utf-8", index=False)
#
# # 循环遍历列表中各个CSV文件名，并追加到合并后的文件
# for i in range(1, len(file_list)):
#     df = pd.read_csv(Folder_Path + '\\' + file_list[i])
#     df.to_csv(SaveFile_Path + '\\' + SaveFile_Name, encoding="utf-8", index=False, header=False, mode='a+')

all_coin_id = pd.DataFrame(pd.read_csv('D:\\7.23_coinmarketcap_api\\all_coin_id.csv').set_index('slug'))
need_wash = pd.DataFrame(
    pd.read_csv('D:\\data_7.22\\ones_graded_placeAndQuarterModified_7.22_washed.csv').set_index('id'))

need_wash.insert(need_wash.shape[1], 'Coin_id', None)

for idx, data in need_wash.iterrows():
    slug = data['name'].replace(' ','-').replace('.','-').lower()
    try:
        id = all_coin_id.loc[slug, 'id']
        need_wash.loc[idx, 'Coin_id'] = id
    except  KeyError:
        pass
        print(str(idx), slug, "没有这个上市啊")
    except ValueError:
        print(str(idx), slug, data['token'], id)

need_wash.to_csv('D:\\7.23_coinmarketcap_api\\ones_graded_placeAndQuarterModified_withCoinID_7.23_washed1.csv',encoding='utf-8')
