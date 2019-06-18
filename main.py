# -*- coding: utf-8 -*-
"""
Created on Tue Jun 18 17:54:26 2019

@author: fj3279
"""

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException


#Initiate browser and navigate to sprint
browser = webdriver.Firefox()
url = "https://sprint.tobiipro.com"
browser.get(url)

#Set max time for loading page in seconds
delay = 5

#Try to load page. If not done within delay, throw exception
try:
    login_element = WebDriverWait(browser, delay).until(EC.presence_of_element_located((By.NAME, 'email')))
    
except TimeoutException:
    print("The webpage {} did not load within {} seconds".format(url, delay))
    


#TODO: Log in using the credentials

#TODO: Import credentials from local file

#TODO: Verify that the log in was successful

#TODO: Log out