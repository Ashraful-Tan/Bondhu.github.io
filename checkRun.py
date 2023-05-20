from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Set up the Selenium WebDriver
driver = webdriver.Chrome()  # Assuming you have Chrome WebDriver installed

# Open the web page
driver.get("URL_OF_THE_PAGE")  # Replace "URL_OF_THE_PAGE" with the actual URL

# Wait for the modal to appear
modal = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.CSS_SELECTOR, ".bd-example-modal-lg"))
)

# Click the "Admin" button in the modal
admin_button = modal.find_element(By.CSS_SELECTOR, "a[href*='sign_in_admin']")
admin_button.click()

# Perform other interactions as needed...

# Close the web page
driver.quit()
