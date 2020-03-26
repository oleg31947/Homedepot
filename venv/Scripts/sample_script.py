from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

# init driver
driver = webdriver.Chrome(executable_path='Chromedriver')

# open the url
driver.get("https://www.amazon.com/gp/help/customer/display.html")

search = driver.find_element(By. XPATH, "//input[@type='search'and @id='helpsearch']")
search.clear()
search.send_keys('Cancel order')

sleep(1)
search=driver.find_element(By.XPATH, "//input[@class='a-button-input']").click()
sleep(2)

driver.quit()
