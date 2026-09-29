#Q1: Write a Python program using re to:
# 1. Extract all email addresses.
# 2. Extract all phone numbers, including both 98765-43210 and 91234 56789 formats.
# 3. Extract all URLs.
# 4. Extract all dates in DD/MM/YYYY format.
# 5. Print each result separately.
import re
text = """
Name: Adnan Malik
Email: adnan.malik@gmail.com
Phone: 98765-43210
Website: https://example.com
DOB: 15/08/2002

Contact: test@example.com
Phone: 91234 56789
"""

email_pattern = r"[\w.-]+@\w+\.\w+"
emails = re.findall(email_pattern, text)

phone_pattern = r"(\d{5}[- ]\d{5})"
numbers = re.findall(phone_pattern, text)

url_pattern = r"https?://\S+"
urls = re.findall(url_pattern, text)

date_pattern = r"\d{2}/\d{2}/\d{4}"
dates = re.findall(date_pattern, text)

print(emails)
print(numbers)
print(urls)
print(dates)



#Q2: Write a program that processes these ids ids = [
#     "EMP-2026-001",
#     "EMP-2026-045",
#     "STU-2026-123",
#     "EMP-20265-001",
#     "EMP-2026-12",
#     "ABC-2026-001",
#     "EMP-2026-999"
# ]
# An Employee ID must follow exactly this format: EMP-YYYY-NNN
# * EMP must be exactly uppercase.
# * YYYY must contain exactly 4 digits.
# * NNN must contain exactly 3 digits.
# * Nothing extra is allowed before or after the ID.

# Your program must:
# 1. Check every ID.
# 2. Print whether it is Valid or Invalid.
# 3. Extract the year and number from every valid Employee ID using capturing groups.
# 4. Print valid IDs like: EMP-2026-001 → Year: 2026, Number: 001

ids = [
    "EMP-2026-001",
    "EMP-2026-045",
    "STU-2026-123",
    "EMP-20265-001",
    "EMP-2026-12",
    "ABC-2026-001",
    "EMP-2026-999"
]

pattern = r"^EMP-(?P<year>\d{4})-(?P<number>\d{3})$"
for id in ids:
    if re.fullmatch(pattern, id):
        result = re.search(pattern, id)
        print(id," -> Year: " ,result.group(1), ", Number: ", result.group(2))