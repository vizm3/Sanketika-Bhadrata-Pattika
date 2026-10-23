import requests
import time

# API_KEY = "YOUR_API_KEY"
API_KEY = "158c6083766a09559902bcde326e599933113451e291d69299f4ac07cde53a10"

filename = input("Enter file name: ")

headers = {
    "x-apikey": API_KEY
}

# Upload the file
files = {
    "file": open(filename, "rb")
}

print("\nUploading file to VirusTotal...")

response = requests.post(
    "https://www.virustotal.com/api/v3/files",
    headers=headers,
    files=files
)

files["file"].close()

if response.status_code == 200:

    data = response.json()

    analysis_id = data["data"]["id"]

    print("File uploaded successfully.")
    print("Waiting for analysis...\n")

    time.sleep(15)

    # Get analysis report
    url = "https://www.virustotal.com/api/v3/analyses/" + analysis_id

    result = requests.get(url, headers=headers)

    if result.status_code == 200:

        report = result.json()

        stats = report["data"]["attributes"]["stats"]

        print("VirusTotal Scan Results")
        print("-----------------------")
        print("Malicious :", stats["malicious"])
        print("Suspicious:", stats["suspicious"])
        print("Harmless  :", stats["harmless"])
        print("Undetected:", stats["undetected"])

        if stats["malicious"] > 0:
            print("\nResult: File is MALICIOUS")

        elif stats["suspicious"] > 0:
            print("\nResult: File is SUSPICIOUS")

        else:
            print("\nResult: File appears SAFE")

    else:
        print("Could not retrieve analysis report.")

else:
    print("Upload Failed")
    print("Error Code:", response.status_code)