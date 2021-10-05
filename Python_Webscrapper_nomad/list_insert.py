color = ["red", "orange", "yellow", "green", "blue", "indigo", "purple"]

def input_on_list(a, b):
  return a.append(b)
  
x = input("추가할 색상을 입력하시오 : ")
input_on_list(color, x)
print(color)
