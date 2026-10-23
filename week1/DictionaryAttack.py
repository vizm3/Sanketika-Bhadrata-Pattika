# Stored usernames and passwords
users = {
    "anand": "welcome123",
    "rahul": "india123",
    "bob": "password123"
}
# Method 1: Dictionary of common passwords
# dictionary = [
#     "123456",
#     "password",
#     "admin",
#     "welcome123",
#     "india123",
#     "hello123"
# ]
username = input("Enter username: ")
if username in users:
    found = False
    # Method 2: Using a dictionary file
    file = open("dictionary.txt", "r")
    for pwd in file:
        pwd = pwd.strip()
        if pwd == users[username]:
            print("\nPassword Cracked!")
            print("Username:", username)
            print("Password:", pwd)
            found = True
            break
    file.close()
    if found == False:
        print("\nUnable to decrypt password.")
else:
    print("Username not found.")

# SAMPLE OUTPUT:
# PS D:\BTech\1_BTech_Labs\Cyber Lab> py DictionaryAttack.py
# Enter username: bob

# Unable to decrypt password.
# PS D:\BTech\1_BTech_Labs\Cyber Lab> py DictionaryAttack.py
# Enter username: anand

# Password Cracked!
# Username: anand
# Password: welcome123