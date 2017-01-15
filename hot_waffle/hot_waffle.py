import os

from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from persistent_pineapple import PersistentPineapple
from selenium.webdriver.firefox import firefox_binary
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class hot_waffle(object):
    settings_file = 'settings.json'

    def __init__(self):
        self.settings = PersistentPineapple(self.settings_file,
                                            woc=True,
                                            lofc=True)

    def get_webdriver(self, driver):
        if driver == 'chrome':
            browser = webdriver.Chrome(executable_path = self.settings['chromedriver'])
        elif driver == 'firefox':
            os.environ["PATH"] += os.pathsep + os.path.dirname(os.path.abspath(self.settings['firefoxdriver']))

            binary = FirefoxBinary(r'C:\Program Files (x86)\Mozilla Firefox\firefox.exe')
            browser = webdriver.Firefox(firefox_binary=binary)
        elif driver == 'edge':
            browser = webdriver.Edge(executable_path = self.settings['edgedriver'])
        elif driver == 'ie':
            caps = DesiredCapabilities.INTERNETEXPLORER
            caps['ignoreProtectedModeSettings'] = True

            browser = webdriver.Ie(executable_path = self.settings['iedriver'])
        elif driver == 'safari':
            pass

        return browser

    def run(self, url, driver = 'chrome'):
        browser = self.get_webdriver(driver)

        browser.get(url)


    def set_defaults(self):
        driver = 'drivers\\chromedriver_win32\\chromedriver.exe'
        self.settings['chromedriver'] = driver
        driver = 'drivers\\geckodriver-v0.11.1-win64\\geckodriver.exe'
        self.settings['firefoxdriver'] = driver
        driver = 'drivers\\MicrosoftWebDriver.exe'
        self.settings['edgedriver'] = driver
        driver = 'drivers\\IEDriverServer_x64_2.53.1\\IEDriverServer.exe'
        self.settings['iedriver'] = driver


if __name__ == '__main__':
    hw = hot_waffle()
    hw.set_defaults()

    url = 'https://www.verizon.com'
    hw.run(url, 'chrome')
    #hw.run(url, 'firefox')
    #hw.run(url, 'edge')
    #hw.run(url, 'ie')
