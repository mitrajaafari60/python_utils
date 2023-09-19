import  re

def validate_email(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}$'

    if re.match(pattern, email):
        return "OK"
    else:
        return "WRONG"

user_email = input()
result = validate_email(user_email)
print(result)