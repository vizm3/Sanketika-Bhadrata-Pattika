import hashlib
import requests

API_KEY = "158c6083766a09559902bcde326e599933113451e291d69299f4ac07cde53a10"

# Generate SHA-256 hash
def generate_hash(filename):

    file = open(filename, "rb")
    data = file.read()
    file.close()

    sha256 = hashlib.sha256()
    sha256.update(data)

    return sha256.hexdigest()

# Query VirusTotal
def check_virustotal(file_hash):

    url = "https://www.virustotal.com/api/v3/files/" + file_hash

    headers = {
        "x-apikey": API_KEY
    }

    response = requests.get(url, headers=headers)

    return response

# Main Program
filename = input("Enter file name: ")
file_hash = generate_hash(filename)

print("\nSHA-256 Hash:")
print(file_hash)

response = check_virustotal(file_hash)

if response.status_code == 200:

    data = response.json()

    stats = data["data"]["attributes"]["last_analysis_stats"]

    print("\nVirusTotal Scan Results")
    print("Malicious :", stats["malicious"])
    print("Suspicious:", stats["suspicious"])
    print("Harmless  :", stats["harmless"])
    print("Undetected:", stats["undetected"])

    if stats["malicious"] > 0:
        print("\nResult : File is MALICIOUS")

    elif stats["suspicious"] > 0:
        print("\nResult : File is SUSPICIOUS")

    else:
        print("\nResult : File appears SAFE")

elif response.status_code == 404:
    print("\nFile hash not found in VirusTotal database.")

else:
    print("\nError:", response.status_code)