from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
driver=webdriver.Edge()
driver.maximize_window()
driver.get("https://demoqa.com/automation-practice-form")
wait=WebDriverWait(driver,10)
#nameField
firstName=driver.find_element(By.XPATH,"//input[@id='firstName']")
firstName.send_keys("abc")
lastName=driver.find_element(By.XPATH,"//input[@id='lastName']")
lastName.send_keys("xyz")
#emailField
email=driver.find_element(By.XPATH,"//input[@id='userEmail']")
email.send_keys("abc@gmail.com")
#genderField
gender=driver.find_element(By.XPATH,"//label[text()='Female']")
gender.click()
#mobileField
mobile=driver.find_element(By.XPATH,"//input[@id='userNumber']")
mobile.send_keys("9876543210")

#submitField
submitBtn=driver.find_element(By.XPATH,"//button[text()='Submit']")
submitBtn.submit()
