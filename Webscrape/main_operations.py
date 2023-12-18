# main_operations.py

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from extract_data import extract_and_write_cnr_numbers
import time

def perform_main_operations(driver, num_pages_to_scrape):
    for _ in range(num_pages_to_scrape):
        # ... (the rest of the code for interacting with the main page)
        page_source = driver.page_source
        with open('output_page1.html', 'w', encoding='utf-8') as file:
            file.write(page_source)
        print(driver.current_url)
        time.sleep(10)

        # Extract and write CNR numbers to the file
        extract_and_write_cnr_numbers(page_source, 'cnr_numbers.csv')

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