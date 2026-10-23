import bcrypt

filename = input("Enter filename to read hashed password: ")
def verify_password(password, filename=filename):
    with open(filename, "rb") as f:
        stored_hash = f.read()
    if bcrypt.checkpw(password.encode(), stored_hash):
        print("Login successful")
    else:
        print("Login failed")

# Example run
pwd = input("Enter login password: ")
verify_password(pwd)
