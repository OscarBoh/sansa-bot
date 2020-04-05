from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
import traceback

# Option 1 - with ChromeOptions
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
headless = true #Set this line to false if headless option is commented

chrome_options.add_argument('--no-sandbox') # required when running as root user. otherwise you would get no sandbox errors. 
driver = webdriver.Chrome(options=chrome_options,
  service_args=['--verbose', '--log-path=/tmp/chromedriver.log'])


def wait_browser(reason):
  print('sleep')
  print(reason)
  sleep(5)
  print('rested')

hashtag = "nesting"

# And now you can add your website / app testing functionality: 
driver.get('https://www.instagram.com/') 
#username = driver.find_element_by_name('username')
wait_browser('web')
username = driver.find_element_by_xpath('//input[@name="username"]').send_keys("anscari24")
password = driver.find_element_by_xpath('//input[@name="password"]').send_keys("salinas77")
login = driver.find_element_by_xpath('//button[@type="submit"]').click()
wait_browser('login')
if headless == false:
  not_off = driver.find_element_by_xpath('//button[@class="aOOlW   HoLwm "]').click()
search = driver.find_element_by_xpath('//input[@class="XTCLo x3qfX "]')
search.send_keys('#' + hashtag)
wait_browser('idk')
try:
  enter_search = driver.find_element_by_xpath('//a[@href="/explore/tags/' + hashtag + '/"]').click()
except:
  print('nope 3')
  traceback.print_exc()
wait_browser('loading photos')
photo_links = driver.find_elements_by_xpath('//a[@href]')
#for i in range(1,50):
#  if "www.instagram.com/p/" in photo_links[i].get_attribute("href"):
#    photo_links[i].click()
#  print(photo_links[i].get_attribute("href"))
#photo_links[19].click()
driver.get(photo_links[19].get_attribute("href"))
wait_browser('loading photo')
options = driver.find_element_by_xpath('//div[@class="MEAGs"]').click()
wait_browser('embed!')
embed = driver.find_elements_by_xpath('//button[@class="aOOlW   HoLwm "]')
embed[3].click()
wait_browser('getting embed')
embed = driver.find_element_by_xpath('//textarea[@class="_4UXK0"]')
print(embed.text)
