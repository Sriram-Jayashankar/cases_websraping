from selenium import webdriver
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select


# Replace with your website URL
website_url = 'https://judgments.ecourts.gov.in/pdfsearch/?p=pdf_search/index&state_code=29~3&dist_code=1'

# Launch the browser
driver = webdriver.Chrome()
driver.get(website_url)

try:
    court_type_dropdown = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, 'fcourt_type'))
    )
    court_type_select = Select(court_type_dropdown)
    court_type_select.select_by_value('2')  # '2' corresponds to "High Court"

    # Step 2: Enter "a" in the search text box
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

    time.sleep(5)

    # Step 5: Select 1000 entries
    entries_dropdown = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, 'example_pdf_length'))
    )
    entries_select = Select(entries_dropdown)
    entries_select.select_by_value('1000')

    # Optionally, you can add a delay to wait for the search results to load
    time.sleep(20)

    # Print the current URL (you can modify this to scrape the desired data)
    page_source = driver.page_source    

    # Write the page source to an HTML file
    with open('output_page1.html', 'w', encoding='utf-8') as file:
        file.write(page_source)
    print(driver.current_url)
    # Write the page source to an HTML file (overwrite if the file already exists)

    #  # Example: Clicking the "Next" button
    # next_button = WebDriverWait(driver, 10).until(
    #     EC.presence_of_element_located((By.ID, 'example_pdf_next'))
    # )
    # next_button.click()

    # Click on the "Next" button
    next_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, 'example_pdf_next'))
    )

    # Scroll the element into view
    driver.execute_script("arguments[0].scrollIntoView(true);", next_button)

    # Wait for any overlays to disappear (you might need to adjust the sleep duration)
    time.sleep(5)

    # Click on the "Next" button
    next_button.click()        

    # Optionally, you can add a delay to wait for the next page to load
    time.sleep(20)

finally:
    # Close the browser
    driver.quit()
