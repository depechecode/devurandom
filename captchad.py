from selenium import webdriver
import time, sys, os
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()
#need to create a file in the same directory with "user,password" combinations
with open("creds.txt") as pw:
	for line in pw:
		lineValues = [x.strip() for x in line.split(',')]
		username = lineValues[0]
		password = lineValues[1]
		print "trying: " + username + " / " + password
		#need to enter the endpoint
		driver.get("https://www.targetapp123.com/account/login")
		time.sleep(4)
		#change the css selectors to match the fields of the endpoints login form
		driver.find_element_by_css_selector("input[type='email']").send_keys(username)
		driver.find_element_by_css_selector("input[type='password']").send_keys(password)
		#shouldn't need to change this
		login_attempt = driver.find_element_by_xpath("//*[@type='submit']")
		login_attempt.submit()
		#if the captcha "recaptcha" is in source code of the page then we've triggered it?
		if ("recaptcha" in driver.page_source):
			print "Captcha Triggerd"
		else:
			print "No Captcha....sadface"
