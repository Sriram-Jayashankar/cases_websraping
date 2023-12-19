# main_operations.py
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from extract_data import extract_and_write_cnr_numbers
from downloadpdf import download_pdf
import time
import requests


def perform_main_operations(driver, num_pages_to_scrape):
    for _ in range(num_pages_to_scrape):
        # ... (the rest of the code for interacting with the main page)
        
        pdf_directory = 'C:/Users/Sriram/Desktop/programming/Webscraping/Webscrape/testpdfs'
        total_height = driver.execute_script("return document.body.scrollHeight")
        #need to click on the button that intern opens a new js file and i want to save that into another html doc
        for button_id in range(10):
            button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, f'link_{button_id}'))
            )


            # Click the button
            time.sleep(10)
            button.click()
            time.sleep(5)
            
            page_source = driver.page_source
            with open('output_page1.html', 'w', encoding='utf-8') as file:
                file.write(page_source)
            print(driver.current_url)
                    # Extract the PDF link directly
            pdf_link = driver.execute_script('return document.querySelector("object").data')

            #donwloading the pdf
            
            download_pdf(pdf_link,f'output_pdf_{button_id}.pdf', pdf_directory)

            close_button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.ID, 'modal_close'))
            )
            time.sleep(5)
            close_button.click()
            time.sleep(5)
            

            # Scroll down by the updated percentage
            
            scroll_distance = total_height * (button_id) / 10
            driver.execute_script(f"window.scrollTo(0, {scroll_distance});")

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