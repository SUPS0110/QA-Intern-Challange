from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import  expected_conditions as EC
from selenium.webdriver.support.ui import Select
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
#DOBField
dob=wait.until(EC.element_to_be_clickable((By.XPATH,"//input[@id='dateOfBirthInput']")))
dob.click()
dob_year=Select(driver.find_element(By.CLASS_NAME,"react-datepicker__year-select"))
dob_year.select_by_visible_text("2025")
dob_month=Select(driver.find_element(By.CLASS_NAME,"react-datepicker__month-select"))
dob_month.select_by_value("3")
dob_date=driver.find_element(By.XPATH,"//div[@class='react-datepicker__day react-datepicker__day--011 react-datepicker__day--weekend']")
dob_date.click()
#submitField
submitBtn=driver.find_element(By.XPATH,"//button[text()='Submit']")
submitBtn.submit()
