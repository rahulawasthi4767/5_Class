import time

from selenium import webdriver

browser = 'ie'

if browser == 'chrome':
    driver=webdriver.Chrome(executable_path="C:/Users/rahul/PycharmProjects/5_Class/drivers/chromedriver.exe")
elif browser =='firefox':
    drive r=webdriver.Firefox(executable_path="C:/Users/rahul/PycharmProjects/5_Class/drivers/geckodriver.exe")
elif browser == 'ie':
    driver=webdriver.Ie(executable_path="C:/Users/rahul/PycharmProjects/5_Class/drivers/IEDriverServer.exe")
else:
    print("Provide appropriate browser name")

driver.get("http://makemytrip.com")
time.sleep(5)
driver.implicitly_wait(30)
driver.find_element_by_id("header_tab_hotels").click()
driver.back()
driver.refresh()
