import threading

from selenium import webdriver
import time
from func_timeout import func_set_timeout, FunctionTimedOut
from queue import Queue

class Crawl_thread(threading.Thread):
    def __init__(self, thread_id, pic_queue):
        threading.Thread.__init__(self)  # 需要对父类的构造函数进行初始化
        self.thread_id = thread_id
        self.queue = pic_queue

    def run(self):
        '''
        线程在调用过程中就会调用对应的run方法
        :return:
        '''
        print('启动线程：', self.thread_id)
        while True:
            if self.queue.empty(): #如果队列为空，则跳出
                print('queue为空')
                break
            else:
                info = pic_queue.get()
                pic_name = info.split('#')[0]
                url = info.split('#')[1][:-1]
                if url[-1] == '?':
                    url = url[:-1]
                    print(url)
                print(self.thread_id,"开爬", pic_name, url)
                try :
                    self.getpng(pic_name,url)
                except FunctionTimedOut:
                    with open('C:/Users/95328/PycharmProjects/pythonProject1/new_short/Ones_with_UsdRaisedTimeOut1.txt', 'a') as f:
                        f.write(pic_name+'#'+url)
                    print(pic_name, '显著超时')

        print('退出了该线程：', self.thread_id)

    @func_set_timeout(150)
    def getpng(self,pic_name, url):
        try:
            options = webdriver.ChromeOptions()
            options.add_argument('--headless')
            # options.add_argument("--window-size=1920,1080")
            chromedriver = r"C:\Program Files\Google\Chrome\Application\chromedriver.exe"
            driver = webdriver.Chrome(options=options, executable_path=chromedriver)
            driver.maximize_window()
            js_height = "return document.body.clientHeight"
            driver.get(url)
            driver.implicitly_wait(100)

            # driver.execute_script("document.body.removeChild(document.body.querySelector('#wm-ipp-base'))")
            # k = 1
            # height = driver.execute_script(js_height)
            # while True:
            #     if k * 500 < height:
            #         js_move = "window.scrollTo(0,{})".format(k * 500)
            #         print(js_move)
            #         driver.execute_script(js_move)
            #         time.sleep(0.1)
            #         height = driver.execute_script(js_height)
            #         k += 1
            #     else:
            #         break
            # scroll_width = driver.execute_script('return document.body.parentNode.scrollWidth')
            # scroll_height = driver.execute_script('return document.body.parentNode.scrollHeight')
            # driver.set_window_size(scroll_width, scroll_height)
            # time.sleep(2)
            #
            # driver.get_screenshot_as_file("D:/Ones_with_UsdRaised/" + pic_name + ".png")

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
            Wid = driver.execute_script('return document.body.parentNode.scrollWidth' )
            Hei = driver.execute_script('return document.body.parentNode.scrollHeight' )
            if Wid > 1080:
                driver.set_window_size(Wid,Hei)
            else:
                driver.set_window_size(1080, Hei)
            driver.implicitly_wait(60)
            time.sleep(1)

            el = driver.find_element_by_tag_name('body')
            el.screenshot("D:/pro/done3/" + pic_name + ".png")



            print(pic_name, "Process {} get one pic !!!")
            driver.close()

        except Exception as ex:
            with open('C:/Users/95328/PycharmProjects/pythonProject1/new_short/web_error3.txt', 'a') as f:
                f.write(pic_name + '#' +url+'\n')
            driver.close()
            print(pic_name,url,ex)

if __name__ == "__main__":
# 你输入的参数
    with open("C:/Users/95328/PycharmProjects/pythonProject1/new_short/ones_with_website3.txt", 'r') as f:

        listIn = f.readlines()

    pic_queue = Queue()

    for e in listIn:
         # if int(e.split('#')[0]) == 2830:
            pic_queue.put(e)

    crawl_threads = []
    crawl_name_list = ['crawl_1','crawl_2','crawl_3']

    print(pic_queue.qsize())

    for thread_id in crawl_name_list:
            thread = Crawl_thread(thread_id,pic_queue) # 启动爬虫线程
            thread.start() # 启动线程
            crawl_threads.append(thread)