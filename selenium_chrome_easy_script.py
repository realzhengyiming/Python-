# 这个是简单的selenium + chrome 的请求模块，简单读取渲染过的动态网页源代码进行处理
# first you should download chrome and chromedriver  
# and put chromedriver into /usr/local/bin 
# second ,you also need to pip install selenium ,and this script use python3.


from selenium.webdriver.chrome.options import Options
from selenium import webdriver
import time

class SinaUrls(object):
    pass
    def __init__(self):
        pass

    def getUrlList(self,url):
        # coding=utf-8
        # 导包
        from selenium import webdriver
        import time

        if __name__ == '__main__':
            from selenium.webdriver.chrome.options import Options
            chrome_options = Options()
            chrome_options.add_argument('--no-sandbox')
            chrome_options.add_argument('--disable-dev-shm-usage')
            chrome_options.add_argument('--headless')
            driver = webdriver.Chrome(chrome_options=chrome_options)
            driver.get(url)


            title = driver.title
            # list = driver.find_element_by_xpath('//a[@target="_blank"]')
            # print(title)
            urlList = []  # 一个页面上的所有的url都在这儿了。
            for link in driver.find_elements_by_xpath('//a[@target="_blank"]'):
                tempUrl = link.get_attribute('href')
                if tempUrl=="http://news.sina.com.cn/guest.html":
                    pass
                else:
                    urlList.append(tempUrl)   # 难怪你会那么的抉择。
                    print(link.get_attribute('href'))

            print("下一页的链接在这儿。")
            print(driver.find_element_by_xpath('//*[@id="d_list"]/div/span[15]').get_attribute('href'))
            
            
        page_sources = driver.page_source
        driver.quit()
        return page_sources


    def check(self,url):  # test the selenium status
        # coding=utf-8
        import time
        from selenium import webdriver

        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.implicitly_wait(6)
        driver.get(url)
        # time.sleep(1)

        for link in driver.find_elements_by_xpath("//*[@href]"):
            print(link.get_attribute('href'))
        driver.quit()



if  __name__  == '__main__':
    # 这个下面开始是单元的测试地方。
    
    testSina = SinaUrls()
    url = "http://www.baidu.com"
    urlSina = "https://news.sina.com.cn/roll/#pageid=153&lid=2509&k=&num=50&page=1"  #使用新浪滚动新闻来进行测试
    testSina.getUrlList(urlSina)
    # testSina.check(url)


