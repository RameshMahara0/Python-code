import re
#check mail validity
def valid_mail_or_not(mail):
    pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"
    return re.match(pattern, mail) is not None
#check Password Strength
def password_strength(password):
    score = 0
    if len(password) >= 8:
        score += 1
    if re.search(r"[A-Z]", password):
        score += 1
    if re.search(r"[a-z]", password):
        score += 1
    if re.search(r"[0-9]", password):
        score += 1
    if re.search(r"[!@#$%^&*()_+}{}\|;:'/?.>,<]", password):
        score += 1
    return score
#Give Feedback For Weak password
def password_feedback(password):
    print("Password must include:")
    if len(password) < 8:
        print("- At least 8 characters")
    if not re.search(r"[A-Z]", password):
        print("- An uppercase letter")
    if not re.search(r"[a-z]", password):
        print("- A lowercase letter")
    if not re.search(r"[0-9]", password):
        print("- A number")
    if not re.search(r"[!@#$%^&*()_+}{}\|;:'/?.>,<]", password):
        print("- A special character")
#Email enter loop unti get valid email
while True:
    mail = input("Enter your E-mail id: ")
    if not valid_mail_or_not(mail):
        print("Invalid Email! Please re-enter.")
        continue
    else:
        print("Valid Email!")
        break
# password strength Loop
while True:
    password = input("Enter Password: ")
    score = password_strength(password)

    if score <= 3:
        print("Too Weak Password!")
        password_feedback(password)
        print("Please enter a stronger password.\n")
        continue
    elif score == 4:
        print("MEDIUM Password")
        break
    else:
        print("STRONG Password")
        break
