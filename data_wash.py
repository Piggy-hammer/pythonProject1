import numpy
import pandas as pd
import math
import numpy as np

def drop_ones_without_web(df):
    drop_ones = []
    for idx, data in df.iterrows():
        if not pd.notnull(data['nodeProportion']):
            drop_ones.append(idx)
    return df.drop(index=drop_ones)

def ger_image_text_index_with1(df):
    df.insert(df.shape[1], 'index_1', None)
    for idx, data in df.iterrows():
        if pd.notnull(data['image_text_prop']) or data['image_text_prop'] != 0:
            df.loc[idx, 'index_1'] = math.log(abs(data['image_text_prop']-1))

    return df

def get_image_text_prop(df):
    df.insert(df.shape[1],'image_prop',None)
    for idx, data in df.iterrows():
        if pd.notnull(data['imageArea']) or data['imageArea'] != 0:
            df.loc[idx, 'image_prop'] = data['imageArea'] / data['TotalArea']

    df.insert(df.shape[1], 'text_prop', None)
    for idx, data in df.iterrows():
        if pd.notnull(data['textArea']) or data['textArea'] != 0:
            df.loc[idx, 'text_prop'] = data['textArea'] / data['TotalArea']

    return df

def get_ones_with_Success(df):
    df.insert(df.shape[1], 'ICO_Success', 0)
    for idx, data in df.iterrows():
        if pd.notnull(data['raised_usd']) or data['Coinmarketcap_identifier'] != 0:
            df.loc[idx, 'ICO_Success'] = 1
        else:
            df.loc[idx, 'ICO_Success'] = 0
    return df

def get_raised_dummpy(df):
    df.insert(df.shape[1], 'Raised_Success', 0)
    for idx, data in df.iterrows():
        if pd.notnull(data['raised_usd']) and int(data['raised_usd']) > 100:
            df.loc[idx, 'Raised_Success'] = 1
        else:
            df.loc[idx, 'Raised_Success'] = 0
    return df

def get_log(df):
    df.insert(df.shape[1], 'lg_TextArea', None)
    for idx, data in df.iterrows():
        if pd.notnull(data['textArea']) and (data['textArea']) > 0:
            df.loc[idx, 'lg_TextArea'] = math.log(data['textArea'])

    df.insert(df.shape[1], 'lg_imageArea', None)
    for idx, data in df.iterrows():
        if pd.notnull(data['imageArea']) and (data['imageArea']) > 0:
            df.loc[idx, 'lg_imageArea'] = math.log(data['imageArea'])

    df.insert(df.shape[1], 'lg_XYleaves', None)
    for idx, data in df.iterrows():
        if pd.notnull(data['XYleaves']) and (data['XYleaves']) > 0:
            df.loc[idx, 'lg_XYleaves'] = math.log(data['XYleaves'])

    df.insert(df.shape[1], 'lg_quadleaves', None)
    for idx, data in df.iterrows():
        if pd.notnull(data['quadleaves']) and (data['quadleaves']) > 0:
            df.loc[idx, 'lg_quadleaves'] = math.log(data['quadleaves'])

    df.insert(df.shape[1], 'lg_raised_usd', None)
    for idx, data in df.iterrows():
        if pd.notnull(data['raised_usd']) and (data['raised_usd']) > 0:
            df.loc[idx, 'lg_raised_usd'] = math.log(data['raised_usd'])

    df.insert(df.shape[1], 'lg_image_text_prop', None)
    for idx, data in df.iterrows():
        if pd.notnull(data['image_text_prop']) and (data['image_text_prop']) > 0:
            df.loc[idx, 'lg_image_text_prop'] = math.log(data['image_text_prop'])
    return df

def drop_ones_without_Success(df):
    drop_ones = []
    for idx, data in df.iterrows():
        if data.ICO_Success == 0:
            drop_ones.append(idx)
    return df.drop(index=drop_ones, axis=0)

def drop_ones_without_Usd_raised(df):
    drop_ones = []
    for idx, data in df.iterrows():
        if not pd.notnull(data['raised_usd']):
            drop_ones.append(idx)
    return df.drop(index=drop_ones)

def turn_coinmarket_identifator_to_num(df):
    for idx, data in df.iterrows():
        if not pd.notnull(data['Coinmarketcap_identifier']):
            df.loc[idx, 'Coinmarketcap_identifier'] = 0
        else:
            df.loc[idx, 'Coinmarketcap_identifier'] = 1
    return df

def turn_mvp_to_num(df):
    for idx, data in df.iterrows():
        if not pd.notnull(data['mvp']):
            df.loc[idx, 'mvp'] = 0
        else:
            df.loc[idx, 'mvp'] = 1
    return df

def turn_whitelist_to_num(df):
    for idx, data in df.iterrows():
        if not pd.notnull(data['whitelist']) or data['whitelist'] == 'No':
            df.loc[idx, 'whitelist'] = 0
        else:
            df.loc[idx, 'whitelist'] = 1
    return df

def turn_web_git_white_to_num(df):
    for idx, data in df.iterrows():
        if not pd.notnull(data['link_white_paper']) or data['link_white_paper'] == '0' or data['link_white_paper'] == 'None':
            df.loc[idx, 'link_white_paper'] = 0
        else:
            df.loc[idx, 'link_white_paper'] = 1

        if not pd.notnull(data['linkedin_link']) or data['linkedin_link'] == '0' or data['linkedin_link'] == 'None' or data['linkedin_link'] == 'TBD':
            df.loc[idx, 'linkedin_link'] = 0
        else:
            df.loc[idx, 'linkedin_link'] = 1

        if not pd.notnull(data['website']) or data['website'] == '0' or data['website'] == 'None':
            df.loc[idx, 'website'] = 0
        else:
            df.loc[idx, 'website'] = 1

        if not pd.notnull(data['github_link']) or data['github_link'] == '0' or data['github_link'] == 'None':
            df.loc[idx, 'github_link'] = 0
        else:
            df.loc[idx, 'github_link'] = 1

    return df


df = pd.DataFrame(pd.read_csv('D:\data_7.22\ones_graded_placeAndQuarterModified_7.22_only_identifer.csv').set_index('id'))
print(df.columns)

# out = get_ones_with_Success(df)

# out = drop_ones_without_Success(df)

# out = drop_ones_without_web(df)
# out = turn_coinmarket_identifator_to_num(out)
# out = turn_web_git_white_to_num(out)
# out = turn_whitelist_to_num(out)
# out = turn_mvp_to_num(out)
# out = get_ones_with_Success(out)
# out = get_raised_dummpy(out)
# out = ger_image_text_index_with1(out)

out = get_log(df)
out = get_image_text_prop(out)


out.to_csv('D:\data_7.22\ones_graded_placeAndQuarterModified_7.22_only_identifer_washed.csv', encoding='utf-8-sig')
