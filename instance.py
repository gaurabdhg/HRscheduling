import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class session:
    
    def __init__(self,url):
        self.path="chromedriver.exe"
        self.service=Service(executable_path=self.path)
        self.uname="akdagarif49@gmail.com"
        self.passkey=112
        self.url=url
        self.driver=webdriver.Chrome(service=self.service)
        
    
    def __wait__(self):
        time.sleep(10)
    
    def __login__(self):
        unamef=WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.CSS_SELECTOR,"input[id='email'] ")))
        passf=WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.CSS_SELECTOR,"input[id='password'] ")))
        unamef.clear()
        passf.clear()
        unamef.send_keys(self.uname)        
        passf.send_keys(self.passkey)     
        try:
            #login
            WebDriverWait(self.driver,3).until(EC.element_to_be_clickable((By.CSS_SELECTOR,"button"))).click()
            #set language
            WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.XPATH,'/html/body/app-root/mainpage/mat-sidenav-container/mat-sidenav-content/mat-toolbar/div/div[2]/i[1]'))).click()
            self.driver.find_element(By.XPATH,'//*[@id="mat-menu-panel-2"]/div/div/div[2]').click()
            return True
        
        except:
            raise SystemError("Login Failed")
            return False
    
    
    def start(self):
        self.driver.get(self.url)
        listen= self.__login__()
        return listen
    
    
    def download(self,tabpath,filepath):
        try:
            self.driver.find_element(By.XPATH,tabpath).click()
            self.driver.find_element(By.XPATH,filepath).click() 
            print("File Download Complete")
            return True
        
        except:
            raise RuntimeWarning ('File Not Downloaded')
            return False
    
    def post(self,individual,timeslot):    
    # upload schedule
        return 
    
    def kill(self):
        self.driver.quit()
        