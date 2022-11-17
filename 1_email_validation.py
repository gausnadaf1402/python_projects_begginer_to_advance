import re

email_cindition = "^[a-z]+[\._]?[a-z 0-9]+[@]\w+[.]\w{2,3}$"

user_email = input("Enter your email:")

if re.search(email_cindition,user_email):
    print("Right email")
else:
    print("wrong email")