import requests
import os

def download_pdf(url, filename, download_directory):
    response = requests.get(url)
    if response.status_code == 200:
        full_path = os.path.join(download_directory, filename)
        with open(full_path, 'wb') as pdf_file:
            pdf_file.write(response.content)
        print(f"PDF downloaded successfully to: {full_path}")
    else:
        print(f"Failed to download PDF. Status code: {response.status_code}")

# Example usage:
pdf_url = 'https://judgments.ecourts.gov.in/judgments_lib/tmp/dd09a5a321fcd41cd6cd37527da858373050f3e2ce15d3c1d48a518ec192c3931703007136.pdf'
pdf_filename = 'custom_name.pdf'
pdf_directory = 'C:/Users/Sriram/Desktop/programming/Webscraping/Webscrape/testpdfs'

download_pdf(pdf_url, pdf_filename, pdf_directory)
