import json
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


with open("account.json") as json_file :
	account = json.load(json_file)


driver = webdriver.Firefox(executable_path=r'C:\Users\iH6576\Downloads\geckodriver\geckodriver.exe')
# driver = webdriver.Chrome(executable_path=r'C:\Users\iH6576\Downloads\chromedriver\chromedriver.exe')
driver.get("https://aipo.i-hayabusa.com")
login = driver.find_element_by_name("member_username").send_keys(account['user'])
password = driver.find_element_by_name("password")
password.send_keys(account['password'])
password.send_keys(Keys.RETURN)

# driver.implicitly_wait(10)
# element = driver.find_element_by_xpath("//input[@value='退勤']")
# element.click()

# driver.quit()
element = WebDriverWait(driver, 20).until(
	EC.element_to_be_clickable((By.XPATH, "//input[@value='退勤']"))
)
button = driver.find_element_by_xpath("//input[@value='退勤']")
driver.execute_script("arguments[0].click();", button)