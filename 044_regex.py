#Regular Expressions: Regular Expression (Regex) is a pattern used to search, find, extract, replace, or validate text. A Regex pattern is a combination of:
# * normal characters
# * special characters
# * character classes
# * quantifiers
# * groups

#Python provides Regex functionality through the built-in re module.


#Raw Strings: r"\d+" >>> this e means that "\d+" is a raw string. Using raw strings avoids unnecessary conflicts between Python’s string escaping and Regex escaping.

import re
text = "My name is Adnan. My age is 25 and my id is 12213125 and 000000"

# search() >>> check the whole string and return the first found value
result = re.search(r"\d+", text)
print(result) # this will print >>> <re.Match object; span=(28, 30), match='25'>
print(result.group()) #this will print >>> 25


# match() >>> checks only th beginning
result_m = re.match(r"\d+", text)
result_m1 = re.match(r"M", text)
print(result_m)
print(result_m1)
print(result_m1.group())



#findall() >>> finds all matches and returns them as a list.
result_fa = re.findall(r"\d+", text)
print(result_fa) #prints all the matches as a list



#finditer() >>> finds all the matches inside an iterator
result_fi = re.finditer(r"\d+", text)
print(result_fi) # >>> this will print >>> <callable_iterator object at 0x1022bcf70>
for i in result_fi:
    print(i,"-----", i.group())
    #advantage of finditer() is that Match objects contain additional information.
    print(i.start())  #Returns the index where the match begins (inclusive).
    print(i.end()) #Returns the index where the match ends (exclusive, following Python slicing rules).



#sub() >>> substitute >>> It replaces matching text with something else.
text1 = "This is my number 1234567890"
result = re.sub(r"\d+", "xxxxxxxxxx", text1)
print(result)

text2 = "My name is Adnan"
result = re.sub(r"Adnan", "Adnan Manzoor", text2)
print(result)


#split() >>> re.split() splits a string based on a Regex pattern. without re text.split(",") can use only one seperator but using re we can use many
text = "Adnan,Zaira;Asrar|Rayhan:Adnan Saad"
result = re.split(r"[,;:| ]", text)  # ,;:| <space> are seperators here
print(result) #will return a list
print(type(result))


#Regex patterns >>> Think of a Regex pattern as instructions.
text = "This is a cat, cot, cart, cut, c9t"

# 1. Literal character >>> Match exactly this character.
result = re.search(r"cat", text)
print(result.group())

# 2. . >>> Any character >>> . is a special Regex character.
result = re.findall(r"c.t", text) #this will find cat, cot, cut but not cart becox there is only one .
print(result) 

# 3. ^ >>> start of string
result = re.search(r"^This", text)
print(result.group())
result1 = re.search(r"^is", text)
print(result1)

# 4. $ >>> end of string
result = re.search(r"c9t$", text)
print(result.group())

# 5. * >>> zero or more
text_t = "a ab abb abbbbb a b b"
result = re.findall(r"ab*", text_t) #this will retun a, ab, abb etc
print(result)

# 6. + >>> one or more
result = re.findall(r"ab+", text_t) #this will return ab, abb, abbb etc
print(result)

# 7. ? >>> Zero or One >>> ? means the previous character is optional, but can occur only once.
txt = "color colour colouur"
result = re.findall(r"colou?r", txt)
print(result)

# 8. {n} >>> exactly n time
txt = "aa a aaa aabaa"
result = re.findall(r"a{3}", txt)
print(result)

num = "1133 12342 123 34 5 987625"
result = re.findall(r"\d{4}", num) # It found four digits, even though the string contains 5 or 6 or 7.
print(result)
result = re.findall(r"\d{4}$", num) # It will find only those numbers which have 4 digits only
print(result)

# 9. {n, m} >>> between n and m 
txt = "aa aaaa aaa aaaaa"
result = re.findall(r"a{2,4}", txt)
print(result)

# 10. [] >>> Character Class means match one character from the bracket and [.] inside the brackets the dot loses its special status
txt = "abc agf bar bhu jyt wwt"
result = re.findall(r"[abc]", txt) # >>> find one character from the bracket
print(result) # >>> ['a', 'b', 'c', 'a', 'b', 'a', 'b']

#we can also use it with range
txt = "Adnan 123 Manzoor"
print(re.findall(r"[A-Z]", txt))
print(re.findall(r"[a-z]", txt))
print(re.findall(r"[0-9]", txt))

# 11. [^] >>> Negated Character Class means donot match any of these characters
txt = "abc123"
result = re.findall(r"[^0-9]", txt)
print(result)
result = re.findall(r"[^a-z]", txt)
print(result)

# 12. \d >>> digit
txt = "I am 22"
result = re.findall(r"\d", txt)
print(result) # >>> this will print ['2', '2']
result = re.findall(r"\d+", txt)
print(result) #>>> this will print ['22']

# 13. \D >>> opposite of digit >>>> means it will match everything that is not a digit even spaces
txt = "I am Adnan 2345 12 32"
result = re.findall(r"\D+", txt)
print(result)

# 14. \w >>> matches a word character i.e letters, digits, _ >>> simply [A-Za-z0-9_]
txt = "I am Adnan 0123 _ ! * ^"
result = re.findall(r"\w", txt)
print(result)

# 15. \W >>> no a word character i.e matches anything except letters, digits, _ (NOTE: will find spaces also)
result = re.findall(r"\W", txt)
print(result) 

# 16. \s >>> matches whitespace characters. i.e space, \t, \n
txt = "Adnan Manzoor        Malik"
print(re.findall(r"\s+", txt))

# 17. \S >>> matches everything except whitespace characters
txt = "Adnan Manzoor        Malik"
print(re.findall(r"\S+", txt))

#NOTE: In Python's re module, Unicode behavior means that special character classes (like \w, \d, \s) match all characters defined by the Unicode standard, not just standard English ASCII characters.



#Capturing groups >>> A capturing group is created using parentheses. It tells Regex: Treat this part as a group and remember what it matched (...)

txt = "1234567890"
pattern = r"(\d{3})(\d{4})(\d{3})"
result = re.search(pattern, txt)
print(result.group())
print(result.group(1))
print(result.group(2))
print(result.group(3))

#use case
number = "+91-1234567890"
pattern = r"(\+\d{2})-(\d{10})"
result = re.search(pattern, number)
country_code = result.group(1)
ph_number = result.group(2)
print(country_code)
print(ph_number)



#Non capturing groups >>> Sometimes you need parentheses to group things together, but you don’t want Regex to save the group. (?:...)
txt = "Mr. Adnan"
pattern = r"(?:Mr.|Mrs.|Ms.) (Adnan)"
result = re.search(pattern, txt)
name = result.group(1) #since the first group is non capturing it wont remember that
print(name)



# () >>> grouping >>> paranthesis are not used only for capturing They allow us to apply Regex operations to an entire sequence. ab+ means ab or abb or abbb etc but (ab)+ means ab abab abababa. Also we can use | in the paranthesis >>> (cat | dog)

txt = "ab abb aab abab ababab"
print(re.findall(r"(?:ab)+", txt))

#NOTE: re.findall() prioritizes capture groups

txt = "cat dog rat"
print(re.findall(r"(cat|dog)", txt))


# group + quantifier
txt = "ab abb aab abab ababab"
print(re.findall(r"(?:ab){3}", txt))


#Named Groups >>> we can name our groups >>> adv : easy to remember
txt = "+91-1234567890"
pattern = r"(?P<c_code>\+\d{2})-(?P<num>\d{10})"
result = re.search(pattern, txt)
print(result.group("c_code"))
print(result.group("num"))


#groupdict() >>> Named groups can also be converted into a dictionary.
txt = "+91-1234567890"
pattern = r"(?P<c_code>\+\d{2})-(?P<num>\d{10})"
result = re.search(pattern, txt)
dict1 = result.groupdict()
print(dict1)



#Email Extraction >>> Basic pattern r"[\w.-]+@[\w.-]+\.\w+"
msg = "Contact me at adnan@gmail.com or adnan-manzoor@gmail.com"
pattern = r"[\w.-]+@[\w.-]+\.\w+"
emails = re.findall(pattern, msg)
print(emails)


#Phone number extraction >>> Basic pattern r"\d{10}"
msg = "Contact me at 0123456789 or 0987654321"
pattern = r"\d{10}"
numbers = re.findall(pattern, msg)
print(numbers)

#URL extraction >>> Basic Patter r"https?://\S+"
msg = "links are https://google.com and https://google.com/users?id=100"
pattern = r"https?://\S+"
urls = re.findall(pattern, msg)
print(urls)

#Date Extraction >>> Basic patter r"\d{2}[-/.]\d{2}[-/.]\d{4}"
msg = "DOB: 14/04/2000      Today: 29.09.2026"
pattern = r"\d{2}[-./]\d{2}[-./]\d{4}"
dates = re.findall(pattern, msg)
print(dates)
#NOTE: it just checks whether it has the patter of a date not that if it is an actual date, datetime helps in that


#ID Extraction >>> Regex can be used to find structured identifiers inside unstructured text.
#suppose an institute has id like EMP-12213125-22 or STU-12232123-25 , we can create a regex pattern to find it
info = "STU-1223214-21 EMP-3221342-17 ACC-3445431-12"
pattern = r"[A-Z]{3}-\d{7}-\d{2}"
ids = re.findall(pattern, info)
print(ids)


#WhiteSpace cleaning
name = """Adnan     Manzoor
            Malik"""
clean_name = re.sub(r"\s+", " ", name).strip()
print(clean_name)


#Text Extraction
info = """Name: Adnan
          Age: 25
          
          Name: Asrar
          Age: 30"""
name_names = re.findall(r"Name:\s*\w+", info)
print(name_names)
names = re.finditer(r"(?:Name:\s*)(\w+)", info)
for name in names:
    print(name.group(1))


#Validation
ids = ['EMP-2000', 'STU_2111', 'EMP-STU-2000', 'EMP-21111', 'STU-ABC-2111']
pattern = r"^EMP-\d{4}$"
for id in ids:
    if re.fullmatch(pattern, id):
        print("Valid id: ", id)
    else:
        print("Invalid id: ", id)

#Cleaning messy text data
data = "Adnan,    Manzoor.       Malik    !!! +"
name = re.sub(r"\s+", " ", data)
name = name.strip()
name = re.sub(r"[^\s\w]","", name)
print(name)



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