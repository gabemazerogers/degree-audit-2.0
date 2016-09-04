from selenium import webdriver
import pickle
from selenium.webdriver.common.keys import Keys


def get_html(username,password):
	driver = webdriver.Firefox()
	# pickle.dump( driver.get_cookies() , open("cookies.pkl","wb"))
	driver.get("https://act.ucsd.edu/studentDars/select")
	username = driver.find_element_by_name("urn:mace:ucsd.edu:sso:username")
	username.send_keys(username)
	password = driver.find_element_by_name("urn:mace:ucsd.edu:sso:password")
	password.send_keys(password)
	password.send_keys(Keys.RETURN)
	get_report = driver.find_element_by_name("reportbutton").click()
	driver.switch_to_window(driver.window_handles[-1])
	html_source = driver.page_source
	return html_source
	driver.close()