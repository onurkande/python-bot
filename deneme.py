import selenium
import time
from selenium import webdriver
driver_path = "C:\Kullanıcılar\onur\Drivers\chromedriver.exe "
browser = webdriver.Chrome(executable_path=driver_path)

time.sleep(5)
webdriver.get("https://www.sinanerdinc.com/")