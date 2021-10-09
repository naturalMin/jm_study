import os
import requests
from bs4 import BeautifulSoup
from babel.numbers import format_currency

os.system("clear")

url = "https://www.iban.com/currency-codes"
extract_country = []

print("Hello! Please choose select a country by number:") 
result = requests.get(url)
soup = BeautifulSoup(result.text,"html.parser")  
table = soup.find("table")
tr = table.find_all("tr")

for td in tr[1:]:
  data = td.find_all("td")
  country = data[0].get_text()
  code = data[2].get_text()
  if country and code :
    td_data ={
      'country':country.capitalize(),
      'code':code
    }
    extract_country.append(td_data)

def input_num():
  try:
    print("\n where are you from? Choose a country by number.\n")
    num = int(input("#: "))
    if num < 0 or num >= len(extract_country):
      print("Choose a number from the list.")
      input_num()    
    else:
      country_data = extract_country[num]
      print(country_data['country'])
      print("\nNow choose another country")        
      num2 = int(input("#: "))
      country_data2 = extract_country[num2]
      print(country_data2['country'])
      
      def input_cur():
        print(f"\nHow many {country_data['code']} do you want to convert to {country_data2['code']}??\n")

        data1 = country_data['code'].lower()
        data2 = country_data2['code'].lower()      
        x = int(input())

        w_url = f"https://wise.com/gb/currency-converter/{data1}-to-{data2}-rate?amount={x}"
        result = requests.get(w_url)
        soup = BeautifulSoup(result.text,"html.parser")      
        convert_val = soup.find("span",{"class":"text-success"})
        convert_val = convert_val.string

        amount  = format(x,',d')
        result_currency = format_currency(int(convert_val)*x, "KRW", locale="ko_KR")

        print(f"{country_data['code']} {amount} is {result_currency}")

      input_cur()  
  except ValueError:
    print("That wasn't a number.")       
    input_cur() 
for index, country_data in enumerate(extract_country):
  print(f"#{index} {country_data['country']}")

input_num()
