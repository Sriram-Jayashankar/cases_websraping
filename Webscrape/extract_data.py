# extract_data.py

from bs4 import BeautifulSoup
import csv

def extract_and_write_cnr_numbers(html_doc, file_path):
    soup = BeautifulSoup(html_doc, 'html.parser')

    # Find all elements with class 'caseDetailsTD'
    case_details_elements = soup.find_all(class_='caseDetailsTD')

    # Extract data for each entry
    entries_data = []
    for element in case_details_elements:
        print(element)
        # cnr = soup.find('span', style='color:#212F3D').find_next('font', color='green').text.strip()
        # date_of_registration = soup.find('span', string='Date of registration :').find_next('font', color='green').text.strip()
        # decision_date = soup.find('span', string='Decision Date :').find_next('font', color='green').text.strip()
        # disposal_nature = soup.find('span', string='Disposal Nature :').find_next('font', color='green').text.strip()
        # court_name = soup.find('span', style='opacity: 0.5;').text.strip()

        # entries_data.append([cnr, date_of_registration, decision_date, disposal_nature, court_name])

    # Write the extracted data to the CSV file
    with open(file_path, 'a', newline='', encoding='utf-8') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerows(entries_data)

# <strong
#                         class="caseDetailsTD"><span style="color:#212F3D"> CNR :</span>
#                         <font color="green"> JKHC020059062023</font><span style="color:#212F3D"> | Date of registration
#                           :</span>
#                         <font color="green"> 07-11-2023</font><span style="color:#212F3D"> | Decision Date :</span>
#                         <font color="green"> 16-12-2023</font><span style="color:#212F3D"> | Disposal Nature :</span>
#                         <font color="green"> Dismissed</font><br><span style="opacity: 0.5;">Court : High Court of Jammu
#                           and Kashmir</span>
#                       </strong>
html_doc='./'
extract_and_write_cnr_numbers