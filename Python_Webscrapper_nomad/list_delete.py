color = ["red", "orange", "yellow", "green", "blue", "indigo", "purple"]

def delete_on_list(a, b):
  return a.remove(b)  

x = input("삭제할 색상을 입력하시오 : ")
delete_on_list(color, x)
print(color)
