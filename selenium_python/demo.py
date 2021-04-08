
"""The webdriver class will connect you to a browser’s instance, which we will shortly cover. The Keys class lets you emulate the stroke of keyboard keys, including special keys like “Shift” and “Return”"""
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

"""create an instance of Chrome"""
driver = webdriver.Chrome(executable_path="D:\Driver\chromedriver.exe")

"""use the .get() method of the driver to load a website"""
driver.get("https://www.python.org")

"""print the title of the page"""
print(driver.title)

"""Finding Xpath of Searchbar and sending some value to search"""
""" Other ways searching the elements are:
CSS ID: .find_element_by_id(“id-search-field”)
DOM Element: .find_element_by_name(“q”)
CSS class: .find_element_by_class_name(“search-field”)
"""

search_bar = driver.find_element_by_xpath("//*[@id='id-search-field']")

search_bar.clear()
search_bar.send_keys("getting started with python")
search_bar.send_keys(Keys.RETURN)

"""To confirm the current URL of the window"""
print(driver.current_url)

driver.close()