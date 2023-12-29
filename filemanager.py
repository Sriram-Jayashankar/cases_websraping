import os
import shutil
from datetime import datetime
from PyPDF2 import PdfReader
import time

def organize_pdfs(pdf_folder):
    # Get a list of all PDF files in the folder
    pdf_files = [f for f in os.listdir(pdf_folder) if f.endswith('.pdf')]

    # Create a directory for each year
    for pdf_file in pdf_files:
        file_path = os.path.join(pdf_folder, pdf_file)

        # Extract DecisionDate from the PDF metadata
        with open(file_path, 'rb') as file:
            pdf_reader = PdfReader(file)
            decision_date = pdf_reader.metadata.get('/decisionDate', None)

            if decision_date:
                try:
                    decision_date = datetime.strptime(decision_date, '%d-%m-%Y')
                    year_folder = os.path.join(pdf_folder, str(decision_date.year))
                    
                    # Create the year folder if it doesn't exist
                    if not os.path.exists(year_folder):
                        os.makedirs(year_folder)

                    # Copy the PDF to the corresponding year folder while preserving metadata
                    try:
                        shutil.copy2(file_path, os.path.join(year_folder, pdf_file))
                        print(f'Moved {pdf_file} to {decision_date.year}')
                    except Exception as copy_error:
                        print(f'Error copying {pdf_file}: {copy_error}')

                except Exception as e:
                    print(f'Error processing {pdf_file}: {e}')
            else:
                print(f'Skipping {pdf_file} as DecisionDate metadata is missing')

# Replace 'path/to/pdfs' with the actual path to your PDFs folder
pdf_folder_path = 'C:/Users/Sriram/Desktop/programming/Webscraping/Webscrape/testpdfs'
organize_pdfs(pdf_folder_path)


#we do this as move may not presesrve the metadata of the pdf file