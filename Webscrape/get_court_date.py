from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from solve_captcha import solve_captcha
from tinker import ScrollableFormDialog
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver import ActionChains
import os
import sys






def extract_court_names(driver):
    page_source = driver.page_source
    soup = BeautifulSoup(page_source, 'html.parser')

    button = driver.find_element(By.CSS_SELECTOR, 'button[data-bs-toggle="modal"][data-bs-target="#MoreModal2"]')
    button.click()
    time.sleep(5)
    div = soup.find("div", attrs={"class": "modal-body"})
    # btn=soup.find("button",attrs={"class":"btn-close","data-bs-dismiss":"modal"})
    court_names = []
    ul_tag = div.find('ul')
    
    if ul_tag:
        for li_tag in ul_tag.find_all('li'):
            a_tag = li_tag.find('a')
            if a_tag:
                court_name = a_tag.text.strip()
                court_names.append(court_name)
    # Close the modal
    
    try:
        close_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//button[@data-bs-dismiss="modal"]'))
        )

# Scroll to the close button
        driver.execute_script("arguments[0].scrollIntoView();", close_button)

# Click the close button
        close_button.click()
    except :
        # Perform another click using x and y coordinates
        x = 1875  # Replace with the desired x coordinate
        y = 328  # Replace with the desired y coordinate
        actions = ActionChains(driver)
        actions.move_by_offset(x, y).click().perform()
    return court_names

website_url='https://judgments.ecourts.gov.in/pdfsearch/?p=pdf_search/index&state_code=29~3&dist_code=1'

#launch teh driver in particular web 
driver=webdriver.Chrome()
driver.maximize_window()
driver.get(website_url)
solve_captcha(driver)

court_names = extract_court_names(driver)
Dialog=ScrollableFormDialog(None,court_names)
result=Dialog.result
# Locate and click the element by its class name
# Wait for the "Decision Date" element to be clickable
decision_date_element = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/nav/div/div/ul/li[4]/a'))
)
# //*[@id="other_filter"]

# /html/body/div[2]/nav/div/div/ul/li[4]/a
# Click the "Decision Date" element
decision_date_element.click()

radio_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.ID, 'exampleRadios5'))
)

# Click the radio button
radio_button.click()

# Find the date input element by ID
date_input = driver.find_element("id", "from_date")

# Input a date (replace 'dd-mm-yyyy' with the actual date you want to input)
date_input.send_keys(result[1])

# Find the date input element by ID
date_input = driver.find_element("id", "to_date")

# Input a date (replace 'dd-mm-yyyy' with the actual date you want to input)
date_input.send_keys(result[2])
time.sleep(5)
# Print the extracted court names
print(result)
