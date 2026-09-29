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
