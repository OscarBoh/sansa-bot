from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from time import sleep
import requests

from logger import Logger
from env import USERNAME, PASSWORD

from bs4 import BeautifulSoup as bs


class Instagram():

    logger = Logger()
    wd = None
    wait = None
    #session_url = 'http://127.0.0.1:58849'
    #session_id = '98610ba2e820c199a1308744f8770b81'
    session_url = None
    session_id = None


    def connect(self):
        if not self.session_id and not self.session_url:
            self.logger.debug('Starting new WebDriver session')
            chrome_options = webdriver.ChromeOptions()
            chrome_options.add_argument('--start-maximized')
            
            self.wd = webdriver.Chrome(options=chrome_options, executable_path='/home/ivangonzalezz/Descargas/chromedriver')
            #self.wd.minimize_window()
            self.wd.get('https://instagram.com')
            self.session_id = self.wd.session_id
            self.session_url = self.wd.command_executor._url
        
        else:
            self.logger.debug('Reusing last session')
            chrome_options = webdriver.ChromeOptions()
            chrome_options.add_argument('--start-maximized')
            
            self.wd = webdriver.Chrome(options=chrome_options, executable_path='/home/ivangonzalezz/Descargas/chromedriver')
            response = self.wd.execute('GET_SESSION', {'sessionId': self.session_id,})
            self.session_id = response['sessionId']

        self.logger.debug('Session id: ' + self.session_id)
        self.logger.debug('Session url: ' + self.session_url)
        
        self.wait = WebDriverWait(self.wd, 10)

    def login(self):
        try:
            self.wait.until(EC.element_to_be_selected((By.XPATH, '//p[@class="izU2O"]/a')) and EC.element_to_be_clickable((By.XPATH, '//p[@class="izU2O"]/a')))
            self.wd.find_element_by_xpath('//p[@class="izU2O"]/a').click()
            self.logger.debug("'Entrar' clicked")
            #sleep(2)
            self.wait.until(EC.element_to_be_selected((By.XPATH, '//input[@name="username"]')) and EC.element_to_be_clickable((By.XPATH, '//input[@name="username"]')) and EC.presence_of_element_located((By.LINK_TEXT, 'Regístrate')))
            self.wd.find_element_by_xpath('//input[@name="username"]').send_keys(USERNAME)
            self.logger.debug("Entered username - ")
            #sleep(2)
            self.wait.until(EC.element_to_be_selected((By.XPATH, '//input[@name="password"]')) and EC.element_to_be_clickable((By.XPATH, '//input[@name="password"]')))
            self.wd.find_element_by_xpath('//input[@name="password"]').send_keys(PASSWORD)
            self.logger.debug("'Entered password'")

            self.wait.until(EC.element_to_be_selected((By.XPATH, '//button[@type="submit"]')) and EC.element_to_be_clickable((By.XPATH, '//button[@type="submit"]')))
            self.wd.find_element_by_xpath('//button[@type="submit"]').click()
            self.logger.debug("Clicked on Login button")

        except Exception as err:
            self.logger.error(str(err))

    def popup(self):
        try:
            self.wait.until(EC.element_to_be_selected((By.XPATH, '//button[text()="Ahora no"]')) and EC.element_to_be_clickable((By.XPATH, '//button[text()="Ahora no"]')))
            self.wd.find_element_by_xpath('//button[text()="Ahora no"]').click()
            self.logger.debug('Killed popup')
        except Exception as err:
            self.logger.error(str(err))

    def goExplore(self):
        try:
            self.wait.until(EC.element_to_be_selected((By.XPATH, '//a[@href="/explore/"]')) and EC.element_to_be_clickable((By.XPATH, '//a[@href="/explore/"]')))
            self.wd.find_element_by_xpath('//a[@href="/explore/"]').click()
            self.logger.debug('Traveled to Explore')
        except Exception as err:
            self.logger.error(str(err))

    def likeExplore(self):
        try:
            """self.wd.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            sleep(4)
            self.wd.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            self.wait.until(EC.element_to_be_selected((By.CLASS_NAME, 'eLAPa')) and EC.element_to_be_clickable((By.CLASS_NAME, 'eLAPa')))
            photos = self.wd.find_elements_by_class_name('eLAPa')"""
            """with open('test.html', 'w') as f:
                res = self.wd.page_source
                res = bs(res).prettify()
                #res = requests.get(self.wd.current_url)
                f.write(res)"""
            for j in range(3):
                sleep(3)
                self.wd.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                self.wait.until(EC.element_to_be_selected((By.CLASS_NAME, 'eLAPa')) and EC.element_to_be_clickable((By.CLASS_NAME, 'eLAPa')))
                photos = self.wd.find_elements_by_class_name('eLAPa')
                for i in photos:
                    i.click()
                    self.wait.until(EC.element_to_be_selected((By.XPATH, '//button[@class="dCJp8 afkep _0mzm-"]')) and EC.element_to_be_clickable((By.XPATH, '//button[@class="dCJp8 afkep _0mzm-"]')))
                    self.wd.find_elements_by_xpath('//button[@class="dCJp8 afkep _0mzm-"]')[0].click()
                    self.wait.until(EC.element_to_be_selected((By.CLASS_NAME, 'ckWGn')) and EC.element_to_be_clickable((By.CLASS_NAME, 'ckWGn')))
                    button = self.wd.find_element_by_class_name('ckWGn').click()
                    self.wait.until(EC.element_to_be_selected((By.CLASS_NAME, 'eLAPa')) and EC.element_to_be_clickable((By.CLASS_NAME, 'eLAPa')))
                self.wd.refresh()
                """self.wait.until(EC.element_to_be_selected((By.XPATH, '//a[@href="/explore/"]')) and EC.element_to_be_clickable((By.XPATH, '//a[@href="/explore/"]')))
                self.wd.find_element_by_xpath('//a[@href="/explore/"]').click()"""
                #self.wait.until(EC.element_to_be_selected((By.CLASS_NAME, 'eLAPa')) and EC.element_to_be_clickable((By.CLASS_NAME, 'eLAPa')))
                #photos = self.wd.find_elements_by_class_name('eLAPa')

            
                #photos[1].click()
            #self.logger.debug(str(photos))
        except Exception as err:
            self.logger.error(str(err))

    def close(self):
        self.wd.close()


if __name__ == "__main__":
    instagram = Instagram()
    instagram.connect()
    instagram.login()
    instagram.popup()
    instagram.goExplore()
    sleep(2)
    instagram.likeExplore()
    #instagram.close()
