# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# import time
# path="/home/rohanailoni/Desktop/scripts/chromedriver_linux64/chromedriver"

# driver = webdriver.Chrome(path)
# url="http://phc.prontonetworks.com/cgi-bin/authlogin?URI=http://www.gstatic.com/generate_204"
# driver.get(url)
# search =driver.find_element_by_name("19BCE2086")
# search.send_keys("")
# password=driver.find_element_by_name("Y775LL")
# password.send_keys("");
# enter=driver.find_element_by_name("Submit22")
# enter.send_keys(Keys.RETURN)


# driver.quit();
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
path="/home/rohanailoni/Desktop/scripts/chromedriver_linux64/chromedriver"

driver = webdriver.Chrome(path)
url="http://phc.prontonetworks.com/cgi-bin/authlogin?uri=http://www.gstatic.com/generate_204"
driver.get(url)
search =driver.find_element_by_name("userId")
search.send_keys("19BCE2086")
password=driver.find_element_by_name("password")
password.send_keys("Y775LL");
enter=driver.find_element_by_name("Submit22")
enter.send_keys(Keys.RETURN)


