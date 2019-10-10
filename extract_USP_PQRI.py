import sys
import csv
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
import getpass

#print(str(sys.argv))

driver = webdriver.Chrome()

driver.get("https://apps.usp.org/app/USPNF/columnsDB.html")
driver.find_element_by_id("edit-submit").click()
# driver.find_element_by_partial_link_text('app/USPNF/columnsDB').click()
driver.get("https://apps.usp.org/app/USPNF/columnsDB.html")

column_ids = ["psn", "psvh", "psvs", "psva", "psvb", "psvc28", "psvc70", "pst", "psd", "psm"]
csv_file = [["Column", "H value", "S value", "A value", "B value", "C2.8 value", "C7.0 value", "Type", "USP", "Manufactorer"]]

row = []
for column_id in column_ids:
    row.append(driver.find_element_by_id(column_id + str(0)).text)

csv_file.append(row)

for i in range(1,74):
    for i in range(1,11):
        row = []
        for column_id in column_ids:
            row.append(driver.find_element_by_id(column_id + str(i)).text)
        csv_file.append(row)
    driver.find_element_by_xpath('//a[contains(@onclick,"incrementPqriStart(10)")]').click()

wtr = csv.writer(open ('out.csv', 'w'), delimiter=',', lineterminator='\n')
for x in csv_file:
    row_str = ",".join(str(s) for s in x)
    wtr.writerow (x)
