age=input("enter age")
if age.isdigit():
    age=int(age)
    print("valid age")
else:
    print("invalid age")
n=int(input("enter a number"))
if 1<n<15:
    print("valid")
else:
        print("invalid")
p=input("enter password")
if len(p)>=6:
  print("strong")
else:
    print("too weak")
email=input("enter mail")
if '@' in email and'.'in email:
    print("valid mail")

else:
    print("invalid password")






    
