# 1(b) Brute Force Attack:
# A Brute Force Attack is a password-cracking technique in which the attacker tries every possible password combination until
# the correct one is found. Unlike a dictionary attack, it does not rely on a list of common passwords. 
# Instead, it systematically checks all possible passwords one by one.
#  If the password is outside the search range, the program prints that it is unable to decrypt the password.

# Characteristics:
# Tries all possible password combinations.
# Guarantees success if the correct password is within the search range.
# Slower than a dictionary attack because it checks every possibility.
# Does not require a password dictionary 

# Approach: The simplest way is to use a Caesar Cipher, where the encryption key is just a shift value. 
# The brute force attack simply tries all possible shifts (0 to 25).

# In this program, we assume that both the original (decrypted) message and the encrypted message are already stored in the code. 
# The algorithm does not know the original message initially. It starts trying different possible keys one by one to decrypt the encrypted message.
# After each attempt, it compares the decrypted result with the original message stored in the program. If they match, the correct key has been found, 
# and the program prints the decrypted message and the key. If no key produces the correct result, it prints "Unable to decrypt the message."
# This simulates a brute force attack, where every possible key is tried until the correct one is found.
# It demonstrates the concept without using complex cryptography.

# Original and encrypted messages
# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
original = "HELLO"
encrypted = "LIPPS"      # HELLO shifted by 3

found = False

# Try all possible keys
for key in range(26):

    decrypted = ""

    # Decrypt each character
    for ch in encrypted:

        decrypted += chr((ord(ch) - ord('A') - key) % 26 + ord('A'))

    # Check if message is correct
    if decrypted == original:
        print("Message Cracked!")
        print("Key:", key)
        print("Encrypted Message:", encrypted)
        print("Decrypted Message:", decrypted)
        found = True
        break

if found == False:
    print("Unable to decrypt message.")