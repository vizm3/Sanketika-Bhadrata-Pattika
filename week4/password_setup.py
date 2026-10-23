import re
import bcrypt

def check_strength(password):
    conditions = [
        re.search(r"[A-Z]", password),
        re.search(r"[a-z]", password),
        re.search(r"[0-9]", password),
        re.search(r"[^A-Za-z0-9]", password),
        len(password) >= 8
    ]
    if all(conditions):
        return "Strong"
    elif sum(bool(c) for c in conditions) >= 3:
        return "Medium"
    else:
        return "Weak"
    
filename = input("Enter filename to save hashed password: ")
def save_hashed_password(password, filename=filename):
    hashed = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
    with open(filename, "wb") as f:
        f.write(hashed)
    print("Password hashed and saved.")

# Example run
pwd = input("Enter a password: ")
print("Strength:", check_strength(pwd))
save_hashed_password(pwd)

# Sample Output:
# PS D:\BTech\1_BTech_Labs\Cyber Lab\week4> python password_setup.py
# Enter filename to save hashed password: hashed
# Enter a password: Anand@123
# Strength: Strong
# Password hashed and saved.
# PS D:\BTech\1_BTech_Labs\Cyber Lab\week4> python password_setup.py
# Enter filename to save hashed password: hashed2
# Enter a password: anand123
# Strength: Medium
# Password hashed and saved.
# PS D:\BTech\1_BTech_Labs\Cyber Lab\week4> python password_setup.py
# Enter filename to save hashed password: asd
# Enter a password: anand87
# Strength: Weak
# Password hashed and saved.