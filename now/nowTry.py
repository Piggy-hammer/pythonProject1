from selenium import webdriver
import os
import time
from func_timeout import func_set_timeout, FunctionTimedOut


@func_set_timeout(60)
def get_png(pic_name,url):
    try:
        options = webdriver.ChromeOptions()
        options.add_argument('--headless')
        options.add_argument("--window-size=1920,1080")
        chromedriver = r"C:\Program Files\Google\Chrome\Application\chromedriver.exe"
        driver = webdriver.Chrome(options=options, executable_path=chromedriver)
        driver.maximize_window()
        driver.get(url)
        time.sleep(1)
        driver.get_screenshot_as_file("D:/Now/" + pic_name + ".png")
        print("Process {} get one pic !!!".format(os.getpid()))
        driver.close()
    except Exception as e:
        with open('ShortTrror.txt', 'a') as f:
            f.write(pic_name+'  '+str(e)+'\n')
        driver.close()

with open("list.txt", 'r') as f:
    listIn = f.readlines()
for e in listIn:
    name = e.split('#')[0]
    if int(name.split('$')[0]) > 5364:
        try :
            url = e.split('#')[1]
            if url[-1] == '?' or '/':
                url = url[:-1]
            get_png(name,url)
        except :
            with open('ShortTimeOut.txt', 'a') as f:
                f.write(str(e)+'\n')
            print(name, url,'显著超时')