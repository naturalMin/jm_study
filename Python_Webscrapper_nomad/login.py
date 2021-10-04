id = input("아이디를 입력해주세요 : ")
pw = input("비밀번호를 입력해주세요 : ")

current_id = "ketty"
current_pw = "1111"

if id == current_id and pw == current_pw:
  print(f"환영합니다 {id}님")
else:
  print("로그인이 실패하였습니다. 아이디, 비밀번호를 확인해주세요.")
