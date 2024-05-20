# def znajdzliczby(x,y):
#     wynik=[]
#     for liczba in range(x,y+1):
#         if liczba %7==0 and liczba %5 !=0:
#             wynik.append(str(liczba))
#     return ", ".join(wynik)
# x=1000
# y=2101
# print(znajdzliczby(x,y))
import re
def validate_password(to_check_password):
    """
    checks if to_check_password is correct or not:
         1. At least 1 letter between [a-z]
         2. At least 1 number between [0-9]
         3. At least 1 letter between [A-Z]
         4. Minimum length of transaction password: 4
         5. Maximum length of transaction password: 8
    Args:
        to_check_password (str): password  to validate

    Returns:
        bool: True if to_check_password is correct else False

    """
    if len(to_check_password) < 4 or len(to_check_password) > 8:
        print("Password must be at least 4 characters long or less than 8 characters")
        return False
    if not re.search("[a-z]", to_check_password):
        print("Password must contain at least one lowercase letter")
        return False
    elif not re.search("[A-Z]", to_check_password):
        print("Password must contain at least one uppercase letter")
        return False
    elif not re.search("[0-9]", to_check_password):
        print("Password must contain at least one number")
        return False
    return True


password = input("Enter your password: ")
while True:
    if validate_password(password):
        print("Password is correct")
        with open("validate_password.txt", "w") as t:
            t.write(f"Podane haslo jest poprawne")
        break
    else:
        password = input("Enter a correct password: ")
        continue
