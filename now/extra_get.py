import time

from selenium import webdriver

url = "http://web.archive.org/web/20180818011907/https://sbcplatform.com/"
pic_name ='4018'

options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_argument("--window-size=1920,1080")
chromedriver = r"C:\Program Files\Google\Chrome\Application\chromedriver.exe"
driver = webdriver.Chrome(options=options, executable_path=chromedriver)
driver.maximize_window()
js_height = "return document.body.clientHeight"
driver.get(url)
driver.implicitly_wait(120)
driver.execute_script("document.body.removeChild(document.body.querySelector('#wm-ipp-base'))")
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
time.sleep(5)

driver.get_screenshot_as_file("D:/pro/extra/" + pic_name + ".png")