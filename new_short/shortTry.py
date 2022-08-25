from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os
import time
from func_timeout import func_set_timeout, FunctionTimedOut


@func_set_timeout(50)
def get_png(pic_name, url):
    try:
        options = webdriver.ChromeOptions()
        options.add_argument('--headless')
        options.add_argument("--window-size=1920,1080")
        chromedriver = r"C:\Program Files\Google\Chrome\Application\chromedriver.exe"
        driver = webdriver.Chrome(options=options, executable_path=chromedriver)
        driver.maximize_window()
        print(url)

        driver.get(url)

        time.sleep(5)

        driver.execute_script("document.body.removeChild(document.body.querySelector('#wm-ipp-base'))")

        time.sleep(0.5)

        driver.get_screenshot_as_file("D:/new_Short/" + pic_name + ".png")
        print("Process {} get one pic !!!".format(pic_name))
        driver.get
        driver.close()

    except Exception as ex:
        with open('C:/Users/95328/PycharmProjects/pythonProject1/new_short/ShortTrror.txt', 'a') as f:
            f.write(pic_name + '  ' + str(ex) + '\n')
        driver.close()
        print(e)


# 你输入的参数
with open("C:/Users/95328/PycharmProjects/pythonProject1/new_short/test1.txt", 'r') as f:

    listIn = f.readlines()

for e in listIn:
    name = e.split('#')[0]
    if int(name)==1443:
        try:
            url = e.split('#')[1][:-1]
            if url[-1] == '?' or '/':
                url = url[:-1]
            get_png(name, url)
        except FunctionTimedOut:
            with open('C:/Users/95328/PycharmProjects/pythonProject1/new_short/ShortTimeOut.txt', 'a') as f:
                f.write(str(e))
            print(name, url, '显著超时')
