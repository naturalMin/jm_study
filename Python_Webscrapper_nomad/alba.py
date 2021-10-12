import os
import csv
import requests
from bs4 import BeautifulSoup

os.system("clear")

def save_to_file(name):  
  name = company_list['company'].replace("/","")     
  file = open(f"{name}.csv", mode="w")
  writer = csv.writer(file)
  writer.writerow(['place','title','time','pay','date'])  
  for job in company_list['jobs']:
    writer.writerow(list(job.values()))    
  print(f"Successful Completed...{company_list['company']}")

alba_url = "http://www.alba.co.kr"
all_result = requests.get(alba_url)
all_soup = BeautifulSoup(all_result.text, "html.parser")
superbrand = all_soup.find("div",{"id" : "MainSuperBrand"})
s_list = superbrand.find_all("a",{"class":"goodsBox-info"})    
        
for s in s_list:     
  link = s['href']
  s_item = s.find("span",{"class":"company"})    
  company = s_item.text    
  if link and company:
    company_list = {
      'company':company, 
      'jobs':[]
      }

  job_result = requests.get(link)
  job_soup = BeautifulSoup(job_result.text, "html.parser")
  job_table = job_soup.find("table")
  rows = job_table.find_all("tr")[1:]  

  for row in rows:  
    local = row.find("td",{"class":"local first"})
    title = row.find("span",{"class":"company"})  
    data = row.find("td",{"class":"data"})
    pay = row.find("td",{"class":"pay"})
    regDate = row.find("td",{"class":"regDate last"})
    if local and title and data and pay and regDate:
      c_items = {
        "place" : local.text,
        "title" : title.text,
        "time" : data.text,
        "pay" : pay.text,
        "date" : regDate.text
      }
      company_list['jobs'].append(c_items)
  save_to_file(company_list['company'])   
