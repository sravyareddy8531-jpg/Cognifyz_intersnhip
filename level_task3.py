import re  

def validate_email(email):
    pattern = r'^\S+@\S+\.\S+$'
    
    if re.match(pattern, email):
        return True
    else:
        return False

email_input = input("Enter email address: ")
if validate_email(email_input):
    print("Valid Email")
else:
    print("Invalid Email")