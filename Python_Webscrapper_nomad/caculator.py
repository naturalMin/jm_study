a = int(input("숫자를 입력해주세요 : "))
b = int(input("숫자를 입력해주세요 : "))

def plus(a, b):
  print("1. 덧셈")
  return a + b
def minus(a, b):
  print("2. 뺄셈")
  return a - b
def times(a, b):
  print("3. 곱셈")
  return a * b
def division(a, b):
  print("4. 나눗셈")
  return a / b
def negation(a):
  print("5. 부정")
  return -a
def power(a, b):
  print("6. 거듭제곱")
  return a ** b  
def remainder(a, b):
  print("7. 나머지")
  return a % b

print(plus(a, b))        
print(minus(a, b))
print(times(a, b))
print(division(a, b))
print(negation(a))
print(power(a, b))
print(remainder(a, b))
