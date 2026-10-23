# 🔍 What the Task Means
# Input: The program takes an email body (plain text string).
# Keyword Matching: It scans for common spam indicators — words or phrases often used in fraudulent or promotional emails.
# Decision Rule: If any of those keywords are found, the program flags the email as spam.
# Output: A simple verdict like “Spam detected” or “Not spam”.

# 🎯 Purpose in the Lab
# This experiment helps students understand:
# How rule-based spam filters work.
# Why keyword detection is a first step, but not sufficient against modern spam (which uses obfuscation and machine learning evasion).
# The importance of combining simple checks with more advanced techniques (like Bayesian filtering or ML classifiers).
# So, in the syllabus context, this is a starter exercise in email security — teaching the basics of spam detection 
# before moving on to more complex defenses.
# spam_check.py

def check_spam(filename):
    spam_keywords = ["lottery", "free", "click here", "winner", "prize"]
    
    with open(filename, "r", encoding="utf-8") as f:
        email_body = f.read().lower()
    
    for keyword in spam_keywords:
        if keyword in email_body:
            print("Spam detected")
            return
    print("Not spam")

# Run the check on saved file
name = input("Enter the filename: ")
check_spam("week3/" + name)
