# main_operations.py
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from extract_data import extract_and_write_cnr_numbers
from downloadpdf import download_pdf
import time
import requests
from bs4 import BeautifulSoup
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random

num = 25
keys = ['/cnr', '/dateOfRegistration', '/decisionDate', '/disposalNature', '/Court']

def perform_main_operations(driver, num_pages_to_scrape):
    while True:
        time.sleep(10)

        pdfdownloaded = 0

        try:
            page_source = driver.page_source
            with open('output_page1.html', 'w', encoding='utf-8') as file:
                file.write(page_source)
            # print(driver.current_url)
            # ... (the rest of the code for interacting with the main page)

            pdf_directory = 'C:/Users/Sriram/Desktop/programming/Webscraping/Webscrape/testpdfs'
            total_height = driver.execute_script("return document.body.scrollHeight")
            # need to click on the button that intern opens a new js file and i want to save that into another html doc
            soup = BeautifulSoup(page_source, 'html.parser')

            td_elements = soup.find_all('td')
            filtered_td_elements = [td for td in td_elements if 'sorting_1' not in td.get('class', [])]

            for td in filtered_td_elements:
                font_data = td.find('font', {'size': '3'})
                elements = td.find_all("font", attrs={"color": "green"})
                courts = td.find_all("span", attrs={"style": "opacity: 0.5;"})
                elements_text = [element.get_text(strip=True) for element in elements]
                courts_text = [court.get_text(strip=True).replace("Court :", "") for court in courts]
                values = elements_text + courts_text
                metadata = dict(zip(keys, values))

                # print(values)

                # print(font_data.text)
                button = td.find('button')
                # print(button)
                onclick_js = button.get('onclick')
                driver.execute_script(onclick_js)

                # button_id = button.get('id')

                # button = WebDriverWait(driver, 10).until(
                # EC.element_to_be_clickable((By.ID, f'link_{button_id}'))
                # )

                # # Click the button
                # time.sleep(5)
                # button.click()
                # ...

                # Wait until the object tag is present
                object_tag = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.TAG_NAME, 'object'))
                )

                # Wait for a random time between 1 and 5 seconds
                # random_time = random.randint(1, 5)
                # time.sleep(random_time)
                # Extract the PDF link directly
                pdf_link = driver.execute_script('return document.querySelector("object").data')

                # donwloading the pdf

                download_pdf(pdf_link, f'{font_data.text}.pdf', pdf_directory, metadata)
                pdfdownloaded += 1
                close_button = WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((By.ID, 'modal_close'))
                )
                try:
                    close_button.click()
                except TimeoutException:
                    # Perform another click using x and y coordinates
                    x = 1875  # Replace with the desired x coordinate
                    y = 328  # Replace with the desired y coordinate
                    actions = ActionChains(driver)
                    actions.move_by_offset(x, y).click().perform()

                # Scroll down by the updated percentage

                scroll_distance = total_height * (pdfdownloaded) / int(num)
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

            # # Optionally, you can add a delay to wait for the next page to load

        except Exception as e:
            print(f"An error occurred: {str(e)}")
            time.sleep(30)
