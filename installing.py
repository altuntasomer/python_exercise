from selenium import webdriver
from selenium.webdriver.common import keys
import time
nametext = "omer"
lastnametext = "altuntas"
random = ".qkdn23i523tp109273"

driver = webdriver.Chrome()
url = "http://google.com"

driver.get(url)

time.sleep(1)
search_input = driver.find_element_by_id("gb_70")
search_input.click()
time.sleep(1)
createAccount = driver.find_element_by_xpath("//span/span")
createAccount.click()
time.sleep(1)
forMe = driver.find_element_by_xpath("//div[2]/div[2]/div/div/span[1]/div[2]")
forMe.click()
time.sleep(1)
name = driver.find_element_by_id("firstName")
name.send_keys("omer")
lastName = driver.find_element_by_id("lastName")
lastName.send_keys("altuntas")
username = driver.find_element_by_id("username")
username.send_keys(nametext+lastnametext+random)
password = driver.find_element_by_xpath("//*[@id='passwd']/div[1]/div/div[1]/input")
password.send_keys("1qA_2w389e4rQ")
password2 = driver.find_element_by_xpath("//*[@id='confirm-passwd']/div[1]/div/div[1]/input")
password2.send_keys("1qA_2w389e4rQ")
next = driver.find_element_by_id("accountDetailsNext")
next.click()
