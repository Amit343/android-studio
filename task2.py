from selenium import webdriver
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome(executable_path="./driver/chromedriver.exe")


driver.get("https://www.atg.party/")
driver.maximize_window() #it is used to maximize the window

#it is used to upload the files
driver.switch_to_frame()
driver.find_element_by_id("profile_channel").send_keys("C:\Users\amit singh\Pictures\2019-10/amit")




print(driver.title)


