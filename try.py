from selenium import webdriver
from selenium.webdriver.chrome.options import Options
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
        js_height = "return document.body.clientHeight"
        driver.get(url)
        time.sleep(0.5)
        k = 1
        height = driver.execute_script(js_height)
        while True:
            if k * 500 < height:
                js_move = "window.scrollTo(0,{})".format(k * 500)
                print(js_move)
                driver.execute_script(js_move)
                time.sleep(0.1)
                height = driver.execute_script(js_height)
                k += 1
            else:
                break
        scroll_width = driver.execute_script('return document.body.parentNode.scrollWidth')
        scroll_height = driver.execute_script('return document.body.parentNode.scrollHeight')
        driver.set_window_size(scroll_width, scroll_height)
        time.sleep(3)
        driver.get_screenshot_as_file("D:/Shots/" + pic_name + ".png")

        print("Process {} get one pic !!!".format(os.getpid()))
        driver.close()
    except Exception as e:
        with open('error.txt','a') as f:
            f.write(pic_name+'  '+str(e)+'\n')
        driver.close()



#你输入的参数
with open("test.txt",'r') as f:
    listIn = f.readlines()
for e in listIn:
    name = e.split('#')[0]
    if int(name) > 5329:
        try :
            url = e.split('#')[1][:-1]
            if url[-1] == '?' or '/':
                url = url[:-1]
            get_png(name,url)
        except :
            with open('timeOut.txt', 'a') as f:
                f.write(name+' '+str(e)+'\n')
            print(name, url,'显著超时')
