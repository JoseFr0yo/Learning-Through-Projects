import re

pattern2 = re.compile(
    r"^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[#?!@$%^&*-]).{8,}$")
password = 'fdbhjs321@123!A'

check = pattern2.fullmatch(password)
print(check)
# At least 8 char long
# At least 1 upper case
# At least 1 lower case
# At least 1 digit
# At least 1 special character
