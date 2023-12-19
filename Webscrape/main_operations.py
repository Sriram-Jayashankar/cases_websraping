# main_operations.py

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from extract_data import extract_and_write_cnr_numbers
import time
import requests


def perform_main_operations(driver, num_pages_to_scrape):
    for _ in range(num_pages_to_scrape):
        # ... (the rest of the code for interacting with the main page)
        

        #need to click on the button that intern opens a new js file and i want to save that into another html doc

        #the id changes from 0to 10 for button so we can enter that in a for loop and automate that ig
        button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, 'link_0'))
        )

        # Click the button
        button.click()
        time.sleep(10)
        page_source = driver.page_source
        with open('output_page1.html', 'w', encoding='utf-8') as file:
            file.write(page_source)
        print(driver.current_url)
        time.sleep(10)

        pdf_url = driver.find_element(By.TAG_NAME, 'object').get_attribute('data')
        print(pdf_url)
        #provide code to add "https://judgments.ecourts.gov.in/" before the pdf url and then download it
        #proivde code to download the pdf file
        download_pdf(pdf_url,'output_pdf.pdf')

def download_pdf(pdf_url, pdf_path):
    # Download the PDF
    response = requests.get(pdf_url)
    with open(pdf_path, 'wb') as pdf_file:
        pdf_file.write(response.content)

    print(f"PDF downloaded to {pdf_path}")





        # # Extract and write CNR numbers to the file
        # extract_and_write_cnr_numbers(page_source, 'cnr_numbers.csv')

        # # Click on the "Next" button
        # next_button = WebDriverWait(driver, 10).until(
        #     EC.element_to_be_clickable((By.ID, 'example_pdf_next'))
        # )

        # # Scroll the element into view
        # driver.execute_script("arguments[0].scrollIntoView(true);", next_button)

        # # Wait for any overlays to disappear (you might need to adjust the sleep duration)
        # time.sleep(5)

        # # Click on the "Next" button
        # next_button.click()

        # # Optionally, you can add a delay to wait for the next page to load