import datetime

import pandas as pd
from wayback import WaybackClient
from func_timeout import func_set_timeout
import time

from wayback.exceptions import BlockedSiteError


@func_set_timeout(10)
def getpic(driver, name):
    pass

def not_nan(para):
    if pd.notnull(para) and type(para) == str and para != '0':
        return True
    else: return False

# def webshotShort(pairList):
#     for e in pairList:
#         print e
#         try:
#             driver.get(e[0])
#             try:
#                 getpic(driver,e[1])
#             except func_timeout.exceptions.FunctionTimedOut:
#                 print('time out with ',e[1])
#             time.sleep(0.1)
#         except Exception as ex:
#            print ex

def getList():
    df = pd.DataFrame(pd.read_csv('D:\\tord_v3_mod2.csv').set_index('id'))
    webname = []
    url = []
    start = []
    end = []
    company = []
    for idx, data in df.iterrows():
        if not_nan(data.website) and not_nan(data.ico_start) and not_nan(data.ico_end) :
        #    print("[{}]名字:{} 网址 {} 开始于 {} 结束于{} ".format(idx,data['name'], data['website'],data['ico_start'],data['ico_end']))
            webUrl = data.website
            if webUrl[-20:] == "?utm_source=icobench":
                webUrl = webUrl[0:-20]
            if webUrl.find('/',9) > 9:
                webUrl = webUrl[:webUrl.find('/', 9)]
            webname.append(idx)
            company.append(data['name'])
            url.append(webUrl)
            start.append(data.ico_start)
            end.append(data.ico_end)
    return zip(webname,url,start,end)


def getWaybackUrl(zipList):
    with open("new_short/ones_with_website.txt", 'a+') as f:
        client = WaybackClient()
        webname = []
        url = []
        count = 0
        for term in zipList :
            if int(term[0]) > 2825:
                start = datetime.datetime.strptime(term[2].replace('/', '-'), '%Y-%m-%d')
                end = datetime.datetime.strptime(term[3].replace('/', '-'), '%Y-%m-%d')
                results = client.search(url=term[1],matchType='exact',from_date=start,to_date=end)
                try:
                    record = next(results).view_url
                    webname.append(term[0])
                    url.append(record)
                    f.write(str(term[0]) + '#' + record+'\n')
                    count =+ 1
                except StopIteration:
                    print(term[0],'没有找到结果')
                except BlockedSiteError:
                    print(term[0],'爬虫被阻止！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！')
        print(count)


if __name__ == '__main__':
    t = time.time()
    zipList = getList()
    getWaybackUrl(zipList)
 #   webshotShort('https://metahash.org/?utm_source=icobench', 'D:\\tstImg1')
    print("Time use: {:.2f}".format(float(time.time() - t)))