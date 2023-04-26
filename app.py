from selenium import webdriver
from userInfo import username,password
from selenium.webdriver.common.keys import Keys
import time
class Instagram:
    driver_path = "C:\Kullanıcılar\onur\Drivers\chromedriver.exe "
    # C:\\Users\\onur\\Drivers\\chromedriver
    #driver_path = r'C:\Users\onur\Drivers\chromedriver.exe'
    
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.browser = webdriver.Chrome(Instagram.driver_path)
        
    def signIn(self):
        self.browser.get("https://www.instagram.com/accounts/login/")
        time.sleep(5)
        usernameInput = self.browser.find_element('username')
        passwordInput = self.browser.find_element('password')
        
        usernameInput.send_keys(username)
        passwordInput.send_keys(password)
        
        passwordInput.send_keys(Keys.ENTER)
    
    def getFollowers(self):
        pass
    
    def unFollowers(self):
        pass
    
    def __del__(self):
        time.sleep(5)
        self.browser.close()
        
app = Instagram(username,password)
app.signIn()
# app.getFollowers('asf')
# app.unFollowers('sdf')
# app.unFollowers('fsd')
        