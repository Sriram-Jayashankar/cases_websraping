# extract_data.py

from bs4 import BeautifulSoup
import csv

def extract_and_write_cnr_numbers(html_path, file_path):
    # Read the HTML file
    with open(html_path, 'r', encoding='utf-8') as file:
        html_doc = file.read()

    soup = BeautifulSoup(html_doc, 'html.parser')

    # Find all elements with class 'caseDetailsTD'
    case_details_elements = soup.find_all(class_='caseDetailsTD')

    # Extract data for each entry
    entries_data = []
    for element in case_details_elements:
        print(element)
        # Uncomment and modify these lines for data extraction
        # cnr = element.find('span', style='color:#212F3D').find_next('font', color='green').text.strip()
        # date_of_registration = element.find('span', string='Date of registration :').find_next('font', color='green').text.strip()
        # decision_date = element.find('span', string='Decision Date :').find_next('font', color='green').text.strip()
        # disposal_nature = element.find('span', string='Disposal Nature :').find_next('font', color='green').text.strip()
        # court_name = element.find('span', style='opacity: 0.5;').text.strip()

        # entries_data.append([cnr, date_of_registration, decision_date, disposal_nature, court_name])

    # Write the extracted data to the CSV file
    with open(file_path, 'a', newline='', encoding='utf-8') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerows(entries_data)

# Specify the path to your local HTML file and the desired output CSV file
html_path = 'C:/Users/Sriram/Desktop/programming/Webscraping/output_page1.html'
csv_output_path = 'C:/Users/Sriram/Desktop/programming/Webscraping/cnr_numbers.csv'

# Call the function with the paths
extract_and_write_cnr_numbers(html_path, csv_output_path)
