import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
import re
# -------------------------------
# Function to detect phishing URLs
# -------------------------------
def check_url(url):
    reasons = []

    # 1. Check HTTP instead of HTTPS
    if url.startswith("http://"):
        reasons.append("Uses HTTP (Not Secure)")

    # 2. Check IP address in domain
    domain = urlparse(url).netloc

    ip_pattern = r"^(\d{1,3}\.){3}\d{1,3}$"
    if re.match(ip_pattern, domain):
        reasons.append("Contains IP Address")

    # 3. Check @ symbol
    if "@" in url:
        reasons.append("Contains @ Symbol")

    # 4. Check suspicious keywords
    keywords = [
        "login", "verify", "bank", "secure",
        "account", "update", "password",
        "signin", "confirm"
    ]

    lower_url = url.lower()

    found = [word for word in keywords if word in lower_url]
    if found:
        reasons.append("Suspicious Keywords: " + ", ".join(found))

    # 5. Too many hyphens
    if url.count("-") > 3:
        reasons.append("Too Many Hyphens")

    # 6. Too many underscores
    if url.count("_") > 2:
        reasons.append("Too Many Underscores")

    return reasons


# -------------------------------
# Extract hyperlinks
# -------------------------------
website = input("Enter Website URL: ")

try:
    response = requests.get(website, timeout=10)
    soup = BeautifulSoup(response.text, "html.parser")

    print("\nExtracted Hyperlinks:\n")

    links = set()

    for tag in soup.find_all("a", href=True):
        link = urljoin(website, tag["href"])

        if link not in links:
            links.add(link)

            print(link)

            issues = check_url(link)

            if issues:
                print("  Suspicious Indicators:")
                for issue in issues:
                    print("   -", issue)
            else:
                print("  Safe URL")

            print("-" * 60)

except Exception as e:
    print("Error:", e)