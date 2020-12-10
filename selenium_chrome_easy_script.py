# 这个是简单的selenium + chrome 的请求模块，简单读取渲染过的动态网页源代码进行处理
import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.options import Options


class SeleniumMaker(object):

    def __init__(self, executable_path: str = "./chromedriver", headless: bool = True):
        chrome_options = Options()
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--disable-dev-shm-usage')
        headless = "--headless" if headless else ""
        chrome_options.add_argument(headless)
        self.driver = webdriver.Chrome(chrome_options=chrome_options, executable_path=executable_path)

    def selenium_request(self, url: str):
        try:
            self.driver.get(url)
            page_sources = self.driver.page_source
            return page_sources
        except Exception as e:
            print(e)
            return ""

    def __del__(self):
        self.driver.quit()


if __name__ == '__main__':
    # 这个下面开始是单元的测试地方。

    testSina = SeleniumMaker()
    url = "http://www.baidu.com"
    urlSina = "https://news.sina.com.cn/roll/#pageid=153&lid=2509&k=&num=50&page=1"  # 使用新浪滚动新闻来进行测试
    testSina.selenium_request(urlSina)
    # testSina.check(url)

