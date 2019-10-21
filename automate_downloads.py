import sys
from selenium import webdriver
import time
import getpass
import csv
import logging
# from urlparse import urljoin
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait # available since 2.4.0
from selenium.webdriver.support import expected_conditions as EC # available since 2.26.0

username = str(sys.argv[1]) if len(sys.argv) > 1 else input('Username:')
password = str(sys.argv[2]) if len(sys.argv) > 2 else getpass.getpass('Password:')

#print(str(sys.argv))

driver = webdriver.Chrome() #C:\ProgramData\Anaconda3\chromedriver.exe

driver.get("https://campus.ie.edu/")
driver.find_element_by_id("user_id").send_keys(username)
driver.find_element_by_id("password").send_keys(password)
driver.find_element_by_id("password").send_keys(Keys.ENTER)

# logger = logging.getLogger(__name__)
# logger.info("Entered campus") #logger.findCaller()

# base_courses = "https://campus.ie.edu/webapps/osc-BasicLTI-BBLEARN/iframe.jsp?mode=view&id=esyllabus&course_id="
base_courses = "https://campus.ie.edu/webapps/osc-BasicLTI-BBLEARN/window.jsp?&mode=view&id=esyllabus&if=true&course_id="

course_names = ["FINANCIAL REPORTING AND ANALYSIS",
                "ECONOMIC ENVIRONMENT & COUNTRY ECONOMIC ANALYSIS",
                "LEADING PEOPLE & TEAMS",
                "STRATEGY",
                "MANAGING PEOPLE IN ORGANIZATIONS",
                "MANAGEMENT ACCOUNTING", #End of term 1
                "MARKETING MANAGEMENT",
                "CORPORATE FINANCE",
                "CREATING VALUE THROUGH OPERATIONS",
                "START-UP CREATION",
                "CORPORATE ENTREPRENEURSHIP", #End of term 2
                "DIGITAL TRANSFORMATION",
                "DIGITAL MARKETING, SOCIAL, MOBILE & ANALYTICS",
                "DATA ANALYTICS FOR DECISION MAKING",
                "GLOBAL SUPPLY CHAIN MANAGEMENT",
                "ADVANCED CORPORATE FINANCE",
                "MANAGEMENT CONTROL",
                "NON MARKET STRATEGY" #End of term 3
                ]
course_codes = ["_114127046_1", "_114126989_1", "_114127019_1", "_114126995_1", "_114127009_1", "_114127022_1", #End of term 1
                "_114161814_1", "_114161822_1", "_114161804_1", "_114161813_1", "_114242906_1", #End of term 2
                "_114242913_1", "_114161811_1", "_114228333_1", #"_114228339_1", "_114161820_1", "_114242907_1", "_114242914_1" #End of term 3
                ]
csv_file = []

for code in course_codes:
    driver.get(base_courses + code)
    # logger.info("Entered course " + code)
    # wtr.writerow("Entered course " + code)
    # iframe_list = driver.find_elements_by_tag_name("iframe")
    # logger.info(iframe_list)
    # i = 0
    # while not driver.find_elements_by_tag_name("iframe") and driver.find_element_by_id("osc_if"):
    #     logger.info("while loop " + str(i))
    #     driver.implicitly_wait(1) # seconds
    #     iframe_list = driver.find_elements_by_tag_name("iframe")
    #     logger.info(len(iframe_list))
    #     i += 1
    # driver.implicitly_wait(5) # seconds
    # src = driver.find_element_by_id("iframe_name").get_attribute("src")
    # url = urljoin(base_url, src)
    #
    # driver.get(url)
    # print(driver.page_source)
    #
    # try:
    #     wait = WebDriverWait(driver, 10)
    #     iframe = wait.until(EC.frame_to_be_available_and_switch_to_it((By.ID, 'osc_if')))
    # finally:
    #     pass
    # try:
    #     driver.switch_to.frame("osc_if")
    #     driver.find_element_by_tag_name("body").click()
    # finally:
    #     driver.implicitly_wait(5) # seconds
    #     driver.switch_to.frame("osc_if")
    #     driver.find_element_by_tag_name("body").click()
    # try:
    # #     element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "ESyllabus_Main")))
    #     wait = WebDriverWait(driver, 10)
    #     element = wait.until(EC.element_to_be_clickable((By.ID, 'emaillink'))) #By.XPATH, '//a[@title="Open the PDF version"]')))
    # finally:
    #     logger.info('syllabus not loaded')
    #     driver.quit()
    # driver.implicitly_wait(5) # seconds
    # i = 0
    # while not driver.find_elements_by_class_name("clase") and driver.find_element_by_id("todas_clases"): # "sistemaEvaluacion"
    #     logger.info("while loop " + str(i))
    #     driver.implicitly_wait(1) # seconds
    #     i += 1
    #     if i > 15:
    #         break
    # driver.implicitly_wait(3) # seconds
    element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "todas_clases")))
    # try:
    #     driver.switch_to.frame("osc_if")
    # finally:
    #     driver.implicitly_wait(5) # seconds
    #     driver.switch_to.frame("osc_if")
    sessions = driver.find_elements_by_xpath('//div[@class="clase"]')
    # materials = driver.find_elements_by_xpath('//div[@class="clase"]//ul[@class="materiales"]')
    course = driver.find_element_by_id("tituloAsignatura")
    email = driver.find_element_by_id("emaillink").text
    name = driver.find_element_by_id("CV_nombre_datosProfesor").text
    # driver.find_element_by_xpath('//a[contains(@title,"Open the PDF")]').click()
    # logger.info("sessions: " + str(len(sessions)))
    csv_file.append([course.text, str(len(sessions)) + " sessions", email, name, base_courses + code])
    # wtr.writerow(course.text + ": " + str(len(sessions)) + " sessions" + ", " + base_courses + code)
    for session in sessions:
    #     print(session)
    # for material in materials:
        session_id = session.get_attribute("id")
        session_name = driver.find_element_by_xpath(f'//div[@id="{session_id}"]/p[@class="tituloClase"]').text
        material = driver.find_element_by_xpath(f'//div[@id="{session_id}"]//ul[@class="materiales"]')
        material_id = material.get_attribute("id")
        content = driver.find_elements_by_xpath(f'//ul[@id="{material_id}"]/li')
        for x in content:
            # print(x)
            try:
                hyperlink = x.find_element_by_xpath(f'.//a').get_attribute('href') #.// search only children
            except:
                hyperlink = ''
            csv_file.append([session_name, session_id, material_id, x.text, hyperlink])
            # wtr.writerow("Session" + str(session_counter) + ", " + material_id + ", " + x.text + ", " + hyperlink)
        # break
    # break

wtr = csv.writer(open('courses.csv', 'w'), delimiter=',', lineterminator='\n')
for x in csv_file:
    # row_str = ",".join(str(s) for s in x)
    wtr.writerow(x)
