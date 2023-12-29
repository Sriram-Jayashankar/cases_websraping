from bs4 import BeautifulSoup

html_doc='''<strong class="caseDetailsTD"><span style="color:#212F3D"> CNR :</span>
<font color="green"> JKHC020066642003</font><span style="color:#212F3D"> | Date of registration
                          :</span>
<font color="green"> 08-04-2003</font><span style="color:#212F3D"> | Decision Date :</span>
<font color="green"> 16-12-2023</font><span style="color:#212F3D"> | Disposal Nature :</span>
<font color="green"> Disposed Off</font><br/><span style="opacity: 0.5;">Court : High Court of
                          Jammu and Kashmir</span>
</strong>
<strong
                        class="caseDetailsTD"><span style="color:#212F3D"> CNR :</span>
                        <font color="green"> JKHC020015112020</font><span style="color:#212F3D"> | Date of registration
                          :</span>
                        <font color="green"> 12-03-2020</font><span style="color:#212F3D"> | Decision Date :</span>
                        <font color="green"> 16-12-2023</font><span style="color:#212F3D"> | Disposal Nature :</span>
                        <font color="green"> Disposed Off</font><br><span style="opacity: 0.5;">Court : High Court of
                          Jammu and Kashmir</span>
                      </strong>'''
soup =BeautifulSoup(html_doc,"html.parser")

elements=soup.find_all("font",attrs={"color": "green"})
courts=soup.find_all("span",attrs={"style":"opacity: 0.5;"})
print(courts)

elements_text=[element.get_text(strip=True)for element in elements]
courts_text = [court.get_text(strip=True) for court in courts]
courts_text = [court.get_text(strip=True).replace("Court :", "") for court in courts]
values = elements_text + courts_text

print(values)