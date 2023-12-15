from bs4 import BeautifulSoup

html = '''
<strong class="caseDetailsTD">
    <span style="color:#212F3D"> CNR :</span>
    <font color="green"> CGHC010304072023</font>
    <span style="color:#212F3D"> | Date of registration :</span>
    <font color="green"> 12-09-2023</font>
    <span style="color:#212F3D"> | Decision Date :</span>
    <font color="green"> 13-12-2023</font>
    <span style="color:#212F3D"> | Disposal Nature :</span>
    <font color="green"> DISPOSED OFF</font>
    <br>
    <span style="opacity: 0.5;">Court : High Court Of Chhattisgarh</span>
</strong>
'''

soup = BeautifulSoup(html, 'html.parser')

# Extract values
cnr_span = soup.find('span', string='CNR :')
cnr = cnr_span.find_next('font', color='green').text.strip() if cnr_span else None

date_of_registration_span = soup.find('span', string='Date of registration :')
date_of_registration = date_of_registration_span.find_next('font', color='green').text.strip() if date_of_registration_span else None

decision_date_span = soup.find('span', string='Decision Date :')
decision_date = decision_date_span.find_next('font', color='green').text.strip() if decision_date_span else None

disposal_nature_span = soup.find('span', string='Disposal Nature :')
disposal_nature = disposal_nature_span.find_next('font', color='green').text.strip() if disposal_nature_span else None

court_name_span = soup.find('span', style='opacity: 0.5;')
court_name = court_name_span.text.strip() if court_name_span else None

print("CNR:", cnr)
print("Date of Registration:", date_of_registration)
print("Decision Date:", decision_date)
print("Disposal Nature:", disposal_nature)
print("Court Name:", court_name)
