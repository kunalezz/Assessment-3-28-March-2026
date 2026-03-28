# Import required libraries
from time import sleep                                          # For static wait
from selenium.webdriver import Chrome, ChromeOptions            # Chrome browser and options
from selenium.webdriver.common.keys import Keys                 # Keyboard actions
from selenium.webdriver.common.by import By                     # Locator strategies (XPath, ClassName, etc.)
from selenium.webdriver.common.action_chains import ActionChains # For mouse hover actions
from selenium.webdriver.support.ui import WebDriverWait         # Explicit wait
from selenium.webdriver.support import expected_conditions as EC # Expected conditions for waits

#  SETUP BROWSER

# Create Chrome options
o = ChromeOptions()

# Keep browser open even after script execution (useful for debugging)
o.add_experimental_option("detach", True)

# Initialize Chrome driver
driver = Chrome(options=o)

# Maximize browser window
driver.maximize_window()

# Create explicit wait object (20 seconds timeout)
wait = WebDriverWait(driver, 20)

#  OPEN WEBSITE

# Open Myntra website
driver.get("https://www.myntra.com/")

# Small static wait for initial load (can be avoided with better waits)
sleep(2)

#  HOVER ON GenZ CATEGORY

# Wait until 'GenZ' menu is visible
genZ = wait.until(
    EC.visibility_of_element_located((By.XPATH, "//a[text()='Genz']"))
)

# Perform mouse hover on 'GenZ' to reveal dropdown
ActionChains(driver).move_to_element(genZ).perform()

#  CLICK SUB-CATEGORY

# Wait for 'Jackets Under...' option and click it
wait.until(
    EC.element_to_be_clickable((By.XPATH, "//a[contains(text(),'Jackets Under')]"))
).click()

#  APPLY FILTERS

# Locate all filter checkboxes
filters = wait.until(
    EC.presence_of_all_elements_located((By.CLASS_NAME, "common-customCheckbox"))
)

# Select first two filters (example: Brand/Category/etc.)
filters[0].click()
filters[1].click()

#  SORT PRODUCTS

# Click on 'Sort by' dropdown
wait.until(
    EC.element_to_be_clickable((By.XPATH, "//div[contains(text(),'Sort by')]"))
).click()

# Select 'Popularity' sorting option
wait.until(
    EC.element_to_be_clickable((By.XPATH, "//label[contains(text(),'Popularity')]"))
).click()

#  OPEN PRODUCT

# Click on first product from the list
wait.until(
    EC.element_to_be_clickable((By.CLASS_NAME, "product-base"))
).click()

#  SWITCH TO NEW TAB

# Switch control to newly opened product tab
driver.switch_to.window(driver.window_handles[1])

#  SELECT SIZE

# Wait and select available size option
wait.until(
    EC.element_to_be_clickable((By.CLASS_NAME, "size-buttons-size-button"))
).click()

#  ADD TO BAG

# Click on 'ADD TO BAG' button
wait.until(
    EC.element_to_be_clickable((By.XPATH, "//div[text()='ADD TO BAG']"))
).click()

#  END

# Wait for a few seconds to observe result
sleep(5)

# Close browser
driver.quit()