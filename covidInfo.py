import time
import os
from selenium import webdriver
from dotenv import load_dotenv
load_dotenv()


PATH_TO_CHROME_DRIVER = os.getenv("DRIVER_PATH")

driver = webdriver.Chrome(PATH_TO_CHROME_DRIVER)  # Optional argument, if not specified will search path.
driver.get('http://www.google.com/')
time.sleep(5)  # Let the user actually see something!
search_box = driver.find_element_by_name('q')
search_box.send_keys('ChromeDriver')
search_box.submit()
time.sleep(5)  # Let the user actually see something!
driver.quit()
