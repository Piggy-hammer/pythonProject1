from selenium import webdriver

import time
from func_timeout import func_set_timeout, FunctionTimedOut

try:
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    options.add_argument("--window-size=1920,1080")
    chromedriver = r"C:\Program Files\Google\Chrome\Application\chromedriver.exe"
    driver = webdriver.Chrome(options=options, executable_path=chromedriver)
    driver.maximize_window()
    driver.get('http://web.archive.org/web/20180827165150/https://bitdrive.tech/')
    driver.find_element_by_xpath().click()
    print('done')
    driver.get_screenshot_as_file("D:/" + 'draft' + ".png")
    print("Process {} get one pic !!!".format('darft'))
    driver.close()
except Exception as e:
    print(e)
    driver.close()