name = input('What is ur name? ')
password = input('Enter password: ')
password_length = len(password)
hide_password = password_length * '*'

print(f"Hi {name}, your password {hide_password} is {password_length} characters long.")
# if didnt create password_length variable, u can use {len(password)} when printing