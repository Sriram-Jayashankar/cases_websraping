import requests
import os
from PyPDF2 import PdfReader,PdfWriter
from test import get_pdf_metadata, add_pdf_metadata
def download_pdf(url, filename, download_directory,metadata):
    response = requests.get(url)
    if response.status_code == 200:
        filename = filename.replace('/', '_')
        full_path = os.path.join(download_directory, filename)
        with open(full_path, 'wb') as pdf_file:
            pdf_file.write(response.content)
        #add metadata to the pdf
        pdf_metadata = get_pdf_metadata(full_path)
        metadata.update(pdf_metadata)
        add_pdf_metadata(full_path, metadata)
        # print(get_pdf_metadata(full_path))
        # print(f"PDF downloaded successfully to: {full_path}")
    else:
        print(f"Failed to download PDF. Status code: {response.status_code}")

# Example usage:
pdf_url = 'https://judgments.ecourts.gov.in/judgments_lib/tmp/dd09a5a321fcd41cd6cd37527da858373050f3e2ce15d3c1d48a518ec192c3931703007136.pdf'
pdf_filename = 'custom_name.pdf'
pdf_directory = 'C:/Users/Sriram/Desktop/programming/Webscraping/Webscrape/testpdfs'

download_pdf(pdf_url, pdf_filename, pdf_directory,metadata={'/decisiondate':'29-06-2047'})
