from selenium import webdriver

driver = webdriver.Firefox()
driver.get('https://www.example.com')
userid = driver.find_element_by_id('USER')
userid.send_keys('12345678')
psw = driver.find_element_by_id('PASSWORD')
psw.send_keys('myp@ssw@rd')
psw.submit()