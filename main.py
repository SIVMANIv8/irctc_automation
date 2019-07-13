import os
import errno
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from authorization import Authorization

browser_path = "Program Files (x86)\Google\Chrome\Application"
full_browser_path = os.path.join("C:/", browser_path)
is_browser_dir = os.path.isdir(full_browser_path)

'''
try: 
    #if not is_browser_dir: raise FileNotFoundError(errno.ENOENT,os.strerror(errno.ENOENT),full_browser_path)
    driver = webdriver.Chrome()
    #driver.get('https://python.org')
except FileNotFoundError as e:
    print(e)

'''

class Irctc:
	def __init__(self):
		print('ass')
		
if __name__ == '__main__':
	auth = Authorization()
	webdriver.Firefox(executable_path='/usr/local/bin/geckodriver')
	print(auth.__crackPassword())
