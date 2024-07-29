# Using Python Selenium Automation and the URL https://www.instagram.com/guviofficial/ kindly do the following mentioned tasks :-
# 1) Use either Relative or Absolute XPATH only for the task.
# 2) Extract the total number of Followers and Following from the URL mentioned above.

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time

driver=webdriver.Chrome()
driver.maximize_window()

# Open Instagram profile
profile_url = 'https://www.instagram.com/guviofficial/'
driver.get(profile_url)

# Allow some time for the page to load
time.sleep(5)
# Extract Followers and Following counts using relative XPath
followers_element = driver.find_element(By.XPATH,"//div//div[3]//ul//li[2]//div//button//span")
following_element = driver.find_element(By.XPATH,"//div//div[3]//ul//li[3]//div//button//span")

followers_count = followers_element.text
following_count = following_element.text

# Print the counts
print(f"Followers: {followers_count}")
print(f"Following: {following_count}")

# Close the WebDriver
driver.quit()
