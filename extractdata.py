from bs4 import BeautifulSoup



with open("output_page1.html","r",encoding="utf-8")as f:
    html_doc=f.read()

soup = BeautifulSoup(html_doc, 'html.parser')
print(soup.title.string)

# Find all elements with class 'caseDetailsTD'
case_details_elements = soup.find_all(class_='caseDetailsTD')

# Extract CNR numbers from each element
cnr_numbers = [element.find('font', color='green').text.strip() for element in case_details_elements]

file_path = 'cnr_numbers.txt'

# Write the extracted CNR numbers to the file
with open(file_path, 'a') as file:
    for cnr_number in cnr_numbers:
        file.write(f"CNR Number: {cnr_number}\n")
