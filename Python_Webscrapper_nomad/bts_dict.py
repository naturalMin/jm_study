
#insert deta

def insert_dict(a_list = {}, key = None, val = None):
  if type(a_list) != dict:
    print("Invalid type. You need to enter a dictionary type. you entered",type(a_list))
  elif key == None or val == None:
    print("Please enter a name and birth date.")
  elif key in a_list:
    print(f"{key} has been already inserted.")
  else:
    a_list[key] = val
    print("Successful inserted!!")
    select_dict(a_list, key)

#select data

def select_dict(a_list = {}, key = None):
  if type(a_list) != dict:
    print("Invalid type. You need to enter a dictionary type. you entered",type(a_list))
  elif key == None:
    print("Please enter data to search for.")
  elif key not in a_list:
    print(f"{key} is not found.")
  else:
    print(f"{key} : ",a_list[key])

#update data

def update_dict(a_list = {}, key = None, val = None):
  if type(a_list) != dict:
    print("Invalid type. You need to enter a dictionary type. you entered",type(a_list))
  elif key == None or val == None:
    print("Please enter name and birth date to update.")
  elif key not in a_list:
    print(f"{key} is not found and can't update." )
  else:
    a_list[key] = val
    print("Successful updated!")
    select_dict(a_list, key)

#delete data    

def delete_dict(a_list = {}, key = None):
  if type(a_list) != dict:
    print("Invalid type. You need to enter a dictionary type. you entered",type(a_list))
  elif key == None:
    print("Please enter name to delete.")
  elif key not in a_list:
    print(f"{key} is not found and can't delete." )
  else:
    del a_list[key]
    print("Successful deleted!")
    select_dict(a_list, key)


bts = {  
  "jin" : 921204,
  "suga" : 930309,
  "J-hope" : 940218,
  "RM" : 9409,
  "jimin" : 951013,
  "v" : 951230,
  "abc" : 123456
}

print(bts)
print()
insert_dict("jungkook",970901)
insert_dict(bts,"jungkook")
insert_dict(bts,"jungkook",970901)
insert_dict(bts,"jungkook",970901)
print()
select_dict("v")
select_dict(bts)
select_dict(bts,"v")
select_dict(bts,"rm")
print()
update_dict("RM",940912)
update_dict(bts,"RM")
update_dict(bts,"RM",940912)
update_dict(bts,"rm",940912)
print()
delete_dict("abc")
delete_dict(bts)
delete_dict(bts,"abc")
delete_dict(bts,"abc")
print()
print(bts)
