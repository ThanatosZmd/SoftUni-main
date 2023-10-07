def password_validator(a: str):
    digits_counter = 0
    errors = []
    if 6>len(a)<10:
        errors.append("Password must be between 6 and 10 characters")
    if not a.isalnum():
        errors.append("Password must consist only of letters and digits")
    for char in a:
        if char.isdigit():
            digits_counter+=1
    if digits_counter<2:
        errors.append("Password must have at least 2 digits")
    return errors

string = input()
err = password_validator(string)
if len(err) != 0:
    print("\n".join(err))
else:
    print("Password is valid")