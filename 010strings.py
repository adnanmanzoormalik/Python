#STRINGS

name = "adnan"
age = "20"

print(name[0])
print(name[2])
print(name[-1]) #negative indexing is from the end

#string slicing
text = "abcdefg"
print(text[0:3])
print(text[1:5])
print(text[:3]) #it is the same as [0:3]
print(text[4:]) #it means from 4th index to last

#checking length of a string
print(len(text))


#strings are immutable we cnt directly change an value in it, this is how we 
name1 = "adnan" 
name1 = "A" + name1[1:]
print(name1)
name1 = name1[:2] + "N" + name1[3:]
print(name1)



#string methods
text1 = "abCde fgHij"
print(text1.upper()) #makes all the alphabets capital
print(text1.lower()) #makes all the alphabets small
print("adnan malik".capitalize()) #makes the first letter capital
print("adnan malik".title()) #capitalizes first letter of every word
print("   adnan   ".strip()) #trims the spaces in front and end
print(text1.replace("abCde","ABCDE")) #replaces the text
print(text1.find("a")) #returns the starting index number of the characters -- returns -1 if the character isnt found
print("ababdcaeufeawhi".count("ab")) #returns number of times something appears


#string concatenantion
first_name = "Adnan"
last_name = "Manzoor"
full_name = first_name + " " + last_name
print(full_name)


#string membership >>> we can check whether something exists in the string or not...returns a boolean
text2 = "I am learning Python"
res = "Python" in text2
res1 = "am" not in text2
print(res)
print(type(res))
print(res1)


# SUMMARY
# String → text inside quotes
# Indexing → accessing individual characters
# Slicing → accessing part of a string
# len() → length of a string
# Strings → immutable
# Methods → upper(), lower(), title(), strip(), replace(), find(), count()
# + → joining strings
# in → checking whether text exists

#PRACTICE QUESTIONS

#Q1. Name Analyzer: Ask the user to enter their full name. Then:, Remove unnecessary spaces from the beginning and end. Print the name in title case, Print the total number of characters. Print the first and last character.
name = input("Enter your full name: ")
name = name.strip()
print(name.title())
print(len(name))
print(name[0] + " " + name[-1])

#Q2. Word Modifier: Create a program that asks the user to enter a sentence. Then: Convert it to lowercase. Replace "python" with "Python". Count how many times the letter "a" appears. Check whether "learn" exists in the sentence.
sentence = input("Enter a sentence: ")
sentence = sentence.lower()
print(sentence.replace("python","Python"))
print(sentence.count("a"))
exists = "learn" in sentence
if exists:
    print("learn exists in sentence")
else:
    print("learn doesnt exist in sentence")


#Q3. String Slicing Challenge: Given: text = "Programming" Print: The first 4 characters. The last 3 characters. Everything except the first 3 characters. The string in uppercase. The position where "gram" starts.
text = "Programming"
print(text[:4])
print(text[-3:])
print(text[3:])
print(text.upper())
print(text.find("gram"))