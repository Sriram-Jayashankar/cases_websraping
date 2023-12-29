from PyPDF2 import PdfReader,PdfWriter

def get_pdf_metadata(file_path):
    with open(file_path, 'rb') as file:
        reader = PdfReader(file)
        metadata = reader.metadata
    return metadata

def add_pdf_metadata(file_path, metadata):
    reader = PdfReader(file_path)
    writer = PdfWriter()

    for page in reader.pages:
        writer.add_page(page)

    writer.add_metadata(metadata)

    with open(file_path, 'wb') as file:
        writer.write(file)

# Use the function
#29-06-2047
#convert the above date into %d-%m-%Y and then add it to the metadata "decisiondate"
#write a fucntion to take input as date and convert it into %d-%m-%Y
def convert_date(date):
    date=date.split('-')
    date=date[::-1]
    date='-'.join(date)
    return date
#can you give an example of how to use the function
# date='29-06-2047'
# date=convert_date(date)
# print(date)
# metadata = {"/decisiondate":date}
# # Use the function
# pdf_metadata = get_pdf_metadata('C:/Users/Sriram/Desktop/programming/Webscraping/Webscrape/testpdfs/WPA_28047_2023 of DIPTENDU CHATTERJEE Vs UNION OF INDIA AND ORS..pdf')
# metadata.update(pdf_metadata)

# add_pdf_metadata('C:/Users/Sriram/Desktop/programming/Webscraping/Webscrape/testpdfs/WPA_28047_2023 of DIPTENDU CHATTERJEE Vs UNION OF INDIA AND ORS..pdf', metadata)
# pdf_metadata_final = get_pdf_metadata('C:/Users/Sriram/Desktop/programming/Webscraping/Webscrape/testpdfs/WPA_28047_2023 of DIPTENDU CHATTERJEE Vs UNION OF INDIA AND ORS..pdf')
# print(pdf_metadata_final)