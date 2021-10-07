import os

#시작-종료 구현
def start_over():
  q = input("Do you want to restart? y or n ")
  if q == "y":
    os.system('clear')
    get_bts()
  elif q == "n":
    print("Ok, bye")
  else:
    print("Incorrect Answer. choose y or n")  
    start_over()

def get_bts():  
  print("Enter the member's name in BTS")
  bts = input("").replace(" ","").split(",") 
  for member in bts:
    print(member)
  start_over()
  
get_bts()
