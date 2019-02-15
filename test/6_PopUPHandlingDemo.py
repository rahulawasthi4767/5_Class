import time
from selenium import webdriver

browser = 'chrome'

if browser == 'chrome':
    driver = webdriver.Chrome(executable_path="C:/Users/Harish/PycharmProjects/Class_6/drivers/chromedriver.exe")
    # driver = webdriver.Chrome()
    # driver.get("https://www.makemytrip.com/")
elif browser == 'firefox':
    driver = webdriver.Firefox(executable_path="C:/Users/Harish/Documents/drivers/geckodriver.exe")
    # driver = webdriver.Firefox()
    # driver.get("https://www.makemytrip.com/")
elif browser == 'ie':
    driver = webdriver.Ie(executable_path="C:/Users/Harish/Downloads/IEDriverServer_Win32_3.14.0/IEDriverServer.exe")
    # driver = webdriver.Ie()
else:
    print("Error - Provide appropriate browser name")

location = "file:///C:/Users/Harish/Desktop/popup.html"
driver.get(location)

# Click on the "Alert" button to generate the Confirmation Alert
button = driver.find_element_by_name('alert')
button.click()

# Switch the control to the Alert window
obj = driver.switch_to.alert

# Retrieve the message on the Alert window
message = obj.text
print("Alert shows following message: " + message)

time.sleep(2)

# Section 1
# use the accept() method to accept the alert
obj.accept()

# get the text returned when OK Button is clicked.
txt = driver.find_element_by_id('msg')
print(txt.text)

time.sleep(2)

# refresh the webpage
driver.refresh()

# Section 2
# Re-generate the Confirmation Alert
button = driver.find_element_by_name('alert')
button.click()

time.sleep(2)

# Switch the control to the Alert window
obj = driver.switch_to.alert

# Dismiss the Alert using
obj.dismiss()

# get the text returned when Cancel Button is clicked.
txt = driver.find_element_by_id('msg')
print(txt.text)
driver.quit()
