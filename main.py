from selenium import webdriver
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Replace with your website URL
website_url = 'https://judgments.ecourts.gov.in/pdfsearch/?p=pdf_search/index&state_code=29~3&dist_code=1'

# Launch the browser
driver = webdriver.Chrome()
driver.get(website_url)

try:
    # Step 1: Enter "a" in the search text box
    search_text_box = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, 'search_text'))
    )
    search_text_box.send_keys('a')

    # Step 2: Display the captcha to the user
    captcha_image_element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, 'captcha_image'))
    )
    
    # You can capture the captcha image here and display it to the user using your preferred method.
    # For simplicity, let's assume you manually solve the captcha and provide the answer.

    # Step 3: Manually input the captcha solution
    captcha_solution = input("Please enter the captcha solution: ")

    # Step 4: Enter the captcha
    captcha_box = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, 'captcha'))
    )
    captcha_box.send_keys(captcha_solution)

    # Step 5: Click on the search button (assuming 'main_search' is the correct ID)
    search_button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, 'main_search'))
    )
    search_button.click()

    # Optionally, you can add a delay to wait for the search results to load
    time.sleep(15)

    # Print the current URL (you can modify this to scrape the desired data)
    print(driver.page_source)

finally:
    # Close the browser
    driver.quit()
