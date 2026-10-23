# Sanketika Bhadrata Pattika (Cyber Lab) 🛡️

This repository contains the laboratory programs and records for the **B.Tech Cyber Security / Cryptography Lab** course. It includes implementation code for cryptography basics, malware analysis, spam detection, password hashing, and phishing identification.

## 📋 Course Information
* **Institution:** B.Tech (Computer Science & Engineering / Cyber Security)
* **Lab Name:** Cyber Lab / Cyber Security Laboratory
* **Syllabus Reference:** CS LAB 22CS11S5

---

## 📂 Project Structure

```text
Cyber Lab/
│
├── week1/                  # Cryptography & Password Cracking
│   ├── BruteForce.py       # Basic mathematical/string brute force implementation
│   ├── DictionaryAttack.py # Script to test passwords against a wordlist
│   └── dictionary.txt      # Wordlist used for the dictionary attack
│
├── week2/                  # Malware Analysis (Static)
│   ├── Exp2_StaticMalware.py # Script extracting hashes/strings without executing files
│   ├── toCheck.png         # Sample image for file verification
│   ├── toCheck.zip         # Sample archive for analysis
│   ├── toCheck1.pdf        # Target PDF file 1
│   ├── toCheck1.txt        # Text export / analysis notes 1
│   ├── toCheck2.pdf        # Target PDF file 2
│   └── toCheck2.txt        # Text export / analysis notes 2
│
├── week3/                  # Email Security
│   ├── EmailSpamCheck.py   # Text-based email filter utilizing keyword matching
│   ├── spam.txt            # Dataset containing verified spam phrases
│   └── notspam.txt         # Dataset containing legitimate email phrases
│
├── week4/                  # Authentication & Password Security
│   ├── password_setup.py   # Registration script to hash and store new credentials
│   ├── password_verify.py  # Login simulator to verify inputs against stored hashes
│   └── stored_hash.txt     # Secure data file housing cryptographic hashes
│
├── week5/                  # Threat Intelligence & API Integration
│   ├── virustotal.py       # Automated script to query file hashes against VirusTotal
│   ├── virustotal2.py      # Expanded VirusTotal checker (URL/IP lookup variants)
│   ├── virustotal3.py      # Refined implementation with robust API error handling
│   └── Example2.txt        # Mock report / hash manifest file
│
├── week6/                  # Social Engineering & Phishing
│   └── hyperlink-phishing.py # Tool analyzing URLs for suspicious redirects/masks
│
└── Documents/
    ├── CS LAB 22CS11S5.pdf # Official course syllabus and lab guidelines
    └── ML2_record.pdf      # Associated machine learning / structural lab record
```

---

## 🛠️ Getting Started

### Prerequisites
Make sure you have **Python 3.x** installed on your system. You will also need `pip` to install specific libraries for modules like VirusTotal API integration (`requests`).

### Setup & Installation
1. Clone the repository:
   ```bash
   git clone https://github.com
   cd Sanketika-Bhadrata-Pattika
   ```

2. Install dependencies (required for Week 5):
   ```bash
   pip install requests
   ```

### Running the Programs
Navigate into any week's directory and execute the desired script via your terminal. For example, to run the password verification script:
```bash
cd week4
python password_verify.py
```

---

## 📄 License
This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.
