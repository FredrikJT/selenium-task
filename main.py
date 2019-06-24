# -*- coding: utf-8 -*-
"""
Created on Tue Jun 18 17:54:26 2019

@author: fj3279
"""

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from credentials import Credentials


#Initiate browser and navigate to sprint
browser = webdriver.Chrome()
url = "https://sprint.tobiipro.com"
browser.get(url)

#Set max time for loading page in seconds
delay = 5

#Try to load page. If not done within delay, throw exception
try:
    email_element = WebDriverWait(browser, delay).until(EC.presence_of_element_located((By.NAME, 'email')))
    
except TimeoutException:
    print("The webpage {} did not load within {} seconds".format(url, delay))
    

#Import credentials from local file
myCredentials = Credentials()

#Wait until field is ready to be clickable
WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.NAME, 'email')))

#Enter credentials into fields
email_element.send_keys(myCredentials.username)
password_element = browser.find_element_by_name('password')
password_element.send_keys(myCredentials.password)

#Click login
submit_button = browser.find_element_by_name('submit')
submit_button.click()

#Verify that the log in was sucessful by checking that the correct page name exist
assert "Tobii Pro Sprint" in browser.title

#Find userbar    
try:
    userbar = WebDriverWait(browser, delay).until(EC.visibility_of_element_located((By.CLASS_NAME, 'gs-userbar__username'))) 
    
except TimeoutException:
    print("The userbar element did not load within {} seconds".format(delay))
    
#Click to show dropdown
userbar.click()

#Find logout element
try:
    logout_element = WebDriverWait(browser, delay).until(EC.visibility_of_element_located((By.CLASS_NAME, 'gs-dropdown__item-btn-logout')))
    
except TimeoutException:
    print("The logout element did not load within {} seconds".format(delay))

#Click logout button
logout_element.click()



































