from selenium import webdriver
import pickle
from selenium.webdriver.common.keys import Keys


def get_html(user_str,pass_str):
	driver = webdriver.PhantomJS()
	pickle.dump( driver.get_cookies() , open("cookies.pkl","wb"))
	driver.get("https://act.ucsd.edu/studentDars/select")
	username = driver.find_element_by_name("urn:mace:ucsd.edu:sso:username")
	username.send_keys(user_str)
	password = driver.find_element_by_name("urn:mace:ucsd.edu:sso:password")
	password.send_keys(pass_str)
	password.send_keys(Keys.RETURN)
	try:
		get_report = driver.find_element_by_name("reportbutton").click()
	except:
		get_report = driver.find_element_by_id("unReport").click()
	driver.switch_to_window(driver.window_handles[-1])
	html_source = driver.page_source
	driver.close()
	driver.switch_to_window(driver.window_handles[-1])
	driver.close()
	return html_source
