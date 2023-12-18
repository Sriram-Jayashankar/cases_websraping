from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import time

#url

#always enclose the main part of the program in a try catch block for error handling

def solve_captcha(driver):
    #step 1-high court
    court_type_dropdown=WebDriverWait(driver,10).until(
        EC.presence_of_element_located((By.ID,'fcourt_type'))
    )#waits for element to get located 
    court_type_select=Select(court_type_dropdown)#selects the dropdown menu
    court_type_select.select_by_value('2')#selects 2 which corresponds to high court


    #step 2-types 'a'
    search_text_box=WebDriverWait(driver,10).until(
        EC.presence_of_element_located((By.ID,'search_text'))
    )
    search_text_box.send_keys("a")#sends a value of a to that search text box element

    #step 3-captcha solving 
    captcha_image_element=WebDriverWait(driver,10).until(
        EC.presence_of_element_located((By.ID,'captcha_image'))
    )
    captcha_solution=input("enter captcha")
    captcha_box=WebDriverWait(driver,10).until(
        EC.presence_of_element_located((By.ID,'captcha'))
    )
    captcha_box.send_keys(captcha_solution)

    #step 4 click on search button
    search_button=WebDriverWait(driver,10).until(
        EC.presence_of_element_located((By.ID,'main_search'))
    )
    search_button.click()

    # # Step 5: Select 1000 entries
    # entries_dropdown = WebDriverWait(driver, 10).until(
    #     EC.presence_of_element_located((By.NAME, 'example_pdf_length'))
    # )
    # entries_select = Select(entries_dropdown)
    # entries_select.select_by_value('1000')

    # Optionally, you can add a delay to wait for the search results to load
    time.sleep(5)
