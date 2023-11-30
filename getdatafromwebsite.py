from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from bs4 import BeautifulSoup
import csv

# Function to extract and write CNR numbers to the file
def extract_and_write_cnr_numbers(html_doc, file_path):
    soup = BeautifulSoup(html_doc, 'html.parser')
    print(soup.title.string)

    # Find all elements with class 'caseDetailsTD'
    case_details_elements = soup.find_all(class_='caseDetailsTD')

    # Extract data for each entry
    entries_data = []
    for element in case_details_elements:
        cnr = element.find('font', color='green').text.strip()
        date_of_registration = get_element_text(element, ' Date of registration :')
        decision_date = get_element_text(element, ' Decision Date :')
        disposal_nature = get_element_text(element, ' Disposal Nature :')
        court_name = element.find('span', style='opacity: 0.5;').text.strip()

        entries_data.append([cnr, date_of_registration, decision_date, disposal_nature, court_name])

    # Write the extracted data to the CSV file
    with open(file_path, 'a', newline='', encoding='utf-8') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerows(entries_data)

# Function to get the text of the next sibling with the specified string
def get_element_text(element, target_string):
    target_element = element.find('span', string=target_string)
    if target_element:
        next_element = target_element.find_next('font', color='green')
        if next_element:
            return next_element.text.strip()
    return None

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

    # Set the number of pages to loop through
    num_pages_to_scrape = 1

    for _ in range(num_pages_to_scrape):
        # Extract data from the current page
        page_source = driver.page_source
        with open('output_page1.html', 'w', encoding='utf-8') as file:
            file.write(page_source)
        print(driver.current_url)

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

finally:
    # Close the browser
    driver.quit()
