
from selenium import webdriver
import os.path
import pandas as pd
from func_timeout import func_set_timeout
import time
import func_timeout

@func_set_timeout(10)
def getpic(driver, name):
    driver.get_screenshot_as_file("D:\\Shots\\" + str(name) + ".png")
    print("Process {} get one pic !!!".format(os.getpid()))
    pass


def webshotShort(pairList):
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    options.add_argument('--disable-gpu')
    options.add_argument('--no-sandbox')
    options.add_argument("--window-size=1920,1080")
    chromedriver = r"C:\Program Files\Google\Chrome\Application\chromedriver.exe"
    driver = webdriver.Chrome(options=options, executable_path=chromedriver)
    driver.maximize_window()
    for e in pairList:
        print e
        try:
            driver.get(e[0])
            try:
                getpic(driver,e[1])
            except func_timeout.exceptions.FunctionTimedOut:
                print('time out with ',e[1])
            time.sleep(0.1)
        except Exception as ex:
           print ex


def getList():
    df = pd.DataFrame(pd.read_csv('D:\\tord_v3_mod2.csv').set_index('id'))
    webname = []
    url = []
    count = 0
    for idx, data in df.iterrows():
        if type(data.website) == str and data.website != '0':
            #print("[{}]:{} with {}".format(idx,data['name'], data['website']))
            webname.append(idx)
            url.append(data.website)
    webshotShort(zip(url,webname))
    print count


if __name__ == '__main__':
    t = time.time()
    getList()
 #   webshotShort('https://metahash.org/?utm_source=icobench', 'D:\\tstImg1')
    print("Time use: {:.2f}".format(float(time.time() - t)))