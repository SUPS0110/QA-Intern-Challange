from selenium import webdriver
from selenium.webdriver.common.by import By
driver=webdriver.Edge()
driver.maximize_window()
driver.get("https://demoqa.com/automation-practice-form")
from selenium.webdriver.support.ui import WebDriverWait
wait=WebDriverWait(driver,10)
#nameField
firstName=driver.find_element(By.XPATH,"//input[@id='firstName']")
firstName.send_keys("abc")
lastName=driver.find_element(By.XPATH,"//input[@id='lastName']")
lastName.send_keys("xyz")
