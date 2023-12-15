from bs4 import BeautifulSoup

# Load the HTML file
with open('output_page1.html', 'r', encoding='utf-8') as file:
    html_content = file.read()

# Create BeautifulSoup object
soup = BeautifulSoup(html_content, 'html.parser')

# Find the target element (e.g., based on ID)
target_element = soup.find('tr', {"role":"row" ,"class":"odd"})  # Replace with the actual ID or other identifying attribute

# Find all parents of the target element
parents = list(target_element.parents)

# Print the parents
for parent in parents:
    print(parent.prettify())  # You can use .prettify() to print the HTML structure nicely
    print('\n' + '-'*50 + '\n')  # Separation line for better readability
