# 这个是简单的selenium + chrome 的请求模块，简单读取渲染过的动态网页源代码进行处理
import json
import pickle
import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from config.settings import SITE_MAIL_URL


class SeleniumMaker(object):

    def __init__(self, executable_path: str = "../config/chromedriver", headless: bool = False):
        chrome_options = Options()
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--disable-dev-shm-usage')
        chrome_options.add_argument('--disable-gpu')  # 谷歌文档提到需要加上这个属性来规避bug
        chrome_options.add_argument('--hide-scrollbars')  # 隐藏滚动条，应对一些特殊页面
        chrome_options.add_argument('blink-settings=imagesEnabled=false')
        self.save_cookie_path = "data/login_cookie_internal_audit.pickle"
        if headless:
            chrome_options.add_argument("--headless")
        self.driver = webdriver.Chrome(chrome_options=chrome_options, executable_path=executable_path)

    def selenium_request(self, html_url: str) -> str:
        try:
            self.driver.get(html_url)
            page_sources = self.driver.page_source
            return page_sources
        except Exception as e:
            print(e)
            return ""

    def selenium_save_cookie(self):  # 试试
        cookies = self.driver.get_cookies()
        with open("selenuim_seva_cookies.cookie", "w") as fp:
            json.dump(cookies, fp)

    def selenium_read_cookie(self) -> bool:
        try:
            with open("selenuim_seva_cookies.cookie", "r") as fp:
                cookies = json.load(fp)
                for cookie in cookies:
                    self.driver.add_cookie(cookie)
                    return True
        except Exception as e:
            print(e)
            return False

    def save_your_cookie(self):
        with open(self.save_cookie_path, 'wb+') as file_handler:
            pickle.dump(self.driver.get_cookies(), file_handler)

    def load_your_cookie(self) -> bool:
        self.driver.get(SITE_MAIL_URL)
        self.driver.delete_all_cookies()

        try:
            with open(self.save_cookie_path, 'rb') as cookies_file:
                cookies = pickle.load(cookies_file)
                for cookie in cookies:
                    cookie_dict = {
                        'domain': cookie.get('domain'),
                        'name': cookie.get('name'),
                        'value': cookie.get('value'),
                        "expires": '',
                        'path': '/',
                        'httpOnly': False,
                        'HostOnly': False,
                        'Secure': False
                    }
                    self.driver.add_cookie(cookie_dict)
            return True
        except Exception as e:
            print(e)
            return False

        # self.driver.get("http://www.baidu.com")


if __name__ == '__main__':
    # 这个下面开始是单元的测试地方。

    testSina = SeleniumMaker(executable_path="../config/chromedriver", headless=False)
    url = "http://www.baidu.com"
    result = testSina.selenium_request(url)
    testSina.save_cookie()
    testSina.read_cookie()
    # testSina.check(url)
    print(result)
