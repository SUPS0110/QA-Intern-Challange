from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import  expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
driver=webdriver.Edge()
driver.maximize_window()
driver.get("https://demoqa.com/automation-practice-form")
wait=WebDriverWait(driver,10)
#submitField
submitBtn=driver.find_element(By.XPATH,"//button[text()='Submit']")
submitBtn.submit()
