color = ["red", "orange", "yellow", "green", "blue", "indigo", "purple"]

# 데이터 검색 및 검색위치 반환
def is_on_list_color(a, b):
  return b in a
def index_of_list(a, b):
  return a.index(b)

x = input("검색할 색상을 입력하시오 : ")

if is_on_list_color(color, x) == True:
  print(f"{x} index number is ", index_of_list(color, x),)
else:
  print(f"sorry, {x} is not exist")
  
