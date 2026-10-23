# * VirusTotal **does not use the file name** to identify a file; it uses the **SHA-256 hash**.
# * A **SHA-256 hash** is a unique digital fingerprint generated from the file's contents.
# * When a file is uploaded, VirusTotal calculates its SHA-256 hash automatically.
# * If another user uploads the **exact same file**, it generates the **same SHA-256 hash**, and VirusTotal returns the existing analysis report instead of scanning it again.
# * If two files have the **same name but different contents**, they produce **different SHA-256 hashes** and are treated as separate files.
# * Even a **single-byte or one-character change** in a file produces a completely different SHA-256 hash.
# * VirusTotal first checks whether the SHA-256 hash already exists in its database:

#   * **Hash found:** Returns the existing threat intelligence report.
#   * **Hash not found:** Uploads and analyzes the file, then stores the report under its new SHA-256 hash.
# * Using SHA-256 avoids duplicate scans, saves bandwidth and processing time, and ensures each unique file is accurately identified.

import hashlib
import requests
import time

API_KEY = "158c6083766a09559902bcde326e599933113451e291d69299f4ac07cde53a10"

headers = {
    "x-apikey": API_KEY
}

# Generate SHA-256 Hash
def generate_hash(filename):

    file = open(filename, "rb")
    data = file.read()
    file.close()

    sha256 = hashlib.sha256()
    sha256.update(data)

    return sha256.hexdigest()

# Check Hash in VirusTotal
def check_hash(file_hash):

    url = "https://www.virustotal.com/api/v3/files/" + file_hash

    response = requests.get(url, headers=headers)

    return response

# Upload File
def upload_file(filename):

    files = {
        "file": open(filename, "rb")
    }

    response = requests.post(
        "https://www.virustotal.com/api/v3/files",
        headers=headers,
        files=files
    )

    files["file"].close()

    return response

# Display Scan Results
def display_report(stats):

    print("\nVirusTotal Scan Results")
    print("----------------------------")
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

# ---------------- Main Program ----------------

filename = input("Enter file name: ")

file_hash = generate_hash(filename)

print("\nSHA-256 Hash:")
print(file_hash)

print("\nChecking VirusTotal database...")

response = check_hash(file_hash)

# ---------------- Hash Found ----------------

if response.status_code == 200:

    print("Hash found in VirusTotal database.")

    data = response.json()

    stats = data["data"]["attributes"]["last_analysis_stats"]

    display_report(stats)

# ---------------- Hash Not Found ----------------

elif response.status_code == 404:

    print("Hash not found.")
    print("Uploading file to VirusTotal...")

    upload = upload_file(filename)

    if upload.status_code == 200:

        analysis_id = upload.json()["data"]["id"]

        print("File uploaded successfully.")
        print("Waiting for analysis...\n")

        time.sleep(15)

        url = "https://www.virustotal.com/api/v3/analyses/" + analysis_id

        result = requests.get(url, headers=headers)

        if result.status_code == 200:

            report = result.json()

            stats = report["data"]["attributes"]["stats"]

            display_report(stats)

        else:
            print("Unable to retrieve analysis report.")

    else:
        print("File upload failed.")

else:
    print("Error:", response.status_code)