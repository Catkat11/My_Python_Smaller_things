import sheety

print("Welcome to Catkat's Flight Club.")
print("We find  the best deals and email you.")
fist_name = input("What's your first name?\n")
last_name = input("What's your last name?\n")
email = input("What is your email?\n")
email_check = input("Type your email again.\n")
if email == email_check:
    print("You're in the club!")
    sheety.post_new_row(fist_name, last_name, email)