import sys
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
import getpass

username = str(sys.argv[1]) if len(sys.argv) > 1 else input('Username:')
password = str(sys.argv[2]) if len(sys.argv) > 2 else getpass.getpass('Password:')

#print(str(sys.argv))

driver = webdriver.Chrome()

driver.get("https://campus.ie.edu/")
driver.find_element_by_id("user_id").send_keys(username)
driver.find_element_by_id("password").send_keys(password)
driver.find_element_by_id("password").send_keys(Keys.ENTER)

base_courses = "https://campus.ie.edu/webapps/osc-BasicLTI-BBLEARN/iframe.jsp?mode=view&id=esyllabus&course_id="

course_codes = ["_114161813_1","_114161804_1"]

for code in course_codes:
    driver.get(base_courses + code)
