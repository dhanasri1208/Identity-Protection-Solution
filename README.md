# Identity-Protection-Solution
# 🔒 Password Validator with Data Breach Check

This Python script validates the strength of a password and checks whether it has been compromised in known data breaches using the [Have I Been Pwned API](https://haveibeenpwned.com/API/v3#PwnedPasswords).

---

## ✅ Features

- Ensures password is at least 8 characters long
- Prevents passwords from containing the username
- Checks if the password appears in known data breaches (using the k-Anonymity model)
- Uses SHA-1 hashing (as required by the HIBP API)

---

## 🛠️ Requirements

Install the required Python package:

```bash
pip install requests
