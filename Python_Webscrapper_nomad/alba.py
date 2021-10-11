import os
import csv
import requests
from bs4 import BeautifulSoup

os.system("clear")

jobs = []

alba_url = "http://www.alba.co.kr"
all_result = requests.get(alba_url)
all_soup = BeautifulSoup(all_result.text, "html.parser")
superbrand = all_soup.find("div",{"id" : "MainSuperBrand"})
s_list = superbrand.find_all("a",{"class":"goodsBox-info"})

def get_jobs(job_url):  
  job_result = requests.get(job_url)
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
      jobs.append(c_items)


def save_to_file(name):  
  name = name.replace("/","")     
  file = open(f"{name}.csv", mode="w")
  writer = csv.writer(file)
  writer.writerow(['place','title','time','pay','date'])  
  for job in jobs:
    writer.writerow(list(job.values()))    
  return             

for s in s_list:
  link = s['href']
  s_item = s.find("span",{"class":"company"})    
  company = s_item.text
  if link and company:
    s_items ={
      'link' : link,
      'company': company
    }
  get_jobs(s_items['link'])    
  save_to_file(s_items['company'])

 


   
