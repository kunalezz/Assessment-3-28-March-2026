# Import required Selenium libraries
from selenium import webdriver                              # Main Selenium WebDriver
from selenium.webdriver.chrome.service import Service       # To manage ChromeDriver service
from selenium.webdriver.common.by import By                 # Locator strategies (ID, XPath, etc.)
from selenium.webdriver.support.ui import WebDriverWait     # Explicit wait
from selenium.webdriver.support import expected_conditions as EC  # Conditions for explicit wait
from webdriver_manager.chrome import ChromeDriverManager    # Auto-download ChromeDriver
import time                                                 # For static waits (sleep)

#  SETUP BROWSER

# Create Chrome options (can add headless, disable notifications, etc.)
options = webdriver.ChromeOptions()

# Initialize Chrome driver using WebDriver Manager (no manual driver setup needed)
driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install()),
    options=options
)

try:
    # Maximize browser window
    driver.maximize_window()

    # Apply implicit wait (global wait for element search)
    driver.implicitly_wait(10)

    # Create explicit wait object (for specific conditions)
    wait = WebDriverWait(driver, 20)

    #  OPEN WEBSITE

    print("Opening ShoppersStack...")
    driver.get("https://www.shoppersstack.com/")

    # Wait until loader disappears (ensures page is fully loaded)
    print("Waiting for homepage loader...")
    wait.until(
        EC.invisibility_of_element_located((By.CSS_SELECTOR, "[class^='loader']"))
    )

    #  SELECT PRODUCT

    print("Locating iPhone product...")

    # Locate product using XPath (searching for text containing 'iphone')
    apple_element = wait.until(
        EC.presence_of_element_located((By.XPATH, "//span[contains(text(),'iphone')]"))
    )

    # Scroll the element into view (important if element is not visible on screen)
    driver.execute_script(
        "arguments[0].scrollIntoView({block: 'center'});",
        apple_element
    )

    # Small delay to ensure smooth scrolling
    time.sleep(1)

    # Click the element using JavaScript (helps avoid click interception issues)
    driver.execute_script("arguments[0].click();", apple_element)

    #  WAIT FOR PRODUCT PAGE

    print("Waiting for product page to load...")

    # Wait again for loader to disappear on product page
    wait.until(
        EC.invisibility_of_element_located((By.CSS_SELECTOR, "[class^='loader']"))
    )

    #  ENTER PINCODE

    print("Entering Pincode...")

    # Wait until pincode input field is visible
    pincode_field = wait.until(
        EC.visibility_of_element_located((By.ID, "Check Delivery"))
    )

    # Clear existing text (if any) and enter new pincode
    pincode_field.clear()
    pincode_field.send_keys("560010")   # Example pincode

    #  CLICK CHECK BUTTON

    print("Clicking Check button...")

    # Wait until Check button is clickable
    check_button = wait.until(
        EC.element_to_be_clickable((By.ID, "Check"))
    )

    # Click the Check button
    check_button.click()

    print("Process completed successfully.")

    # Wait for few seconds to observe result
    time.sleep(5)

#  EXCEPTION HANDLING

except Exception as e:
    # Print error if any step fails
    print(f"An error occurred: {e}")

#  CLEANUP

finally:
    # Close the browser
    driver.quit()
    print("Browser closed.")