



# 16. DEBUGGING API CALLS
# API debugging means checking each stage of the API request.

# Common problems:
# - Wrong URL
# - Wrong HTTP method
# - Wrong parameters
# - Missing headers
# - Invalid authentication
# - Wrong API key
# - Server error
# - Timeout
# - Unexpected JSON structure

# Example:
import requests
url = "https://google.com"
response = requests.get(url)
# Debug:
# print(response.status_code)
# print(response.text)
# print(response.headers)

# If response contains JSON:
data = response.json()
print(data)
print(type(data))

# You can inspect:
# print(data.keys())

# Common HTTP status codes:
# 200 → Success
# 400 → Bad Request
# 401 → Unauthorized
# 403 → Forbidden
# 404 → Not Found
# 500 → Server Error

# Example problem:
data = response.json()
print(data["name"])

# If: KeyError: 'name'

don't assume the API is wrong.

First inspect:

print(data)

The actual response may have:

{
    "username": "Adnan"
}

instead of:

{
    "name": "Adnan"
}


17. DEBUGGING DATA PROCESSING SCRIPTS
-------------------------------------

Typical data-processing pipeline:

Read
 ↓
Validate
 ↓
Clean
 ↓
Transform
 ↓
Calculate
 ↓
Save

The most important rule:

Find the point where the data FIRST becomes incorrect.

Example:

numbers = [10, 20, 30, 40]

total = sum(numbers)
print("Total:", total)

average = total / 2
print("Average:", average)

If the expected average is 25 but the program gives 50:

Check each step:

print("Numbers:", numbers)
print("Total:", total)
print("Count:", len(numbers))
print("Average:", average)

The problem is:

average = total / 2

It should be:

average = total / len(numbers)

Debugging data processing is about checking intermediate results, not just the final result.


18. DEBUGGING DATA TYPE PROBLEMS
--------------------------------

A data type problem happens when a variable has a different type than expected.

Common types:

int
float
str
list
tuple
set
dict
bool
None

Always check:

print(variable)
print(type(variable))

Example:

age = input("Enter age: ")

print(type(age))

input() always returns a string.

So:

age = input("Enter age: ")

gives:

"20"

not:

20

Correct:

age = int(input("Enter age: "))

Another example:

numbers = "12345"

print(sum(numbers))

Problem:

numbers is a string.

Check:

print(numbers)
print(type(numbers))

For a list:

numbers = [1, 2, 3, 4, 5]

print(sum(numbers))

Important example:

def calculate_total(a, b):
    total = a + b

result = calculate_total(10, 20)

print(result)

Output:

None

Why?

The function doesn't have return.

Correct:

def calculate_total(a, b):
    total = a + b
    return total

Important:

None means there is no returned value.

Debug unexpected types using:

print(variable)
print(type(variable))


19. DEBUGGING MISSING DATA
--------------------------

Missing data can appear as:

None
""
[]
{}
missing dictionary keys
missing file lines
missing values in data

Example:

name = None

print(name.upper())

Error:

AttributeError

Debug:

print(name)
print(type(name))

Output:

None
<class 'NoneType'>

Handle it:

if name is not None:
    print(name.upper())
else:
    print("Name is missing")


MISSING DICTIONARY KEY
----------------------

Example:

user = {
    "name": "Adnan",
    "age": 22
}

print(user["email"])

Error:

KeyError

Debug:

print(user)
print(user.keys())

Safer method:

email = user.get("email")

If missing:

email = None

Can provide a default:

email = user.get("email", "Not provided")


MISSING FILE DATA
-----------------

If you expect:

Name
Age
Country

but the file contains only:

Name

Check:

print(lines)
print(len(lines))

This helps identify missing data.

Important difference:

None → No value / missing value

0 → Numeric value zero

"" → Empty string

[] → Empty list


20. DEBUGGING UNEXPECTED RESULTS
--------------------------------

An unexpected result is usually a logical error.

The program:

- Runs successfully
- Produces no exception
- But gives the wrong result

Example:

numbers = [10, 20, 30, 40]

total = sum(numbers)
average = total / 2

print(average)

Output:

50.0

Expected:

25.0

Debug:

print("Numbers:", numbers)
print("Total:", total)
print("Count:", len(numbers))
print("Average:", average)

The problem:

average = total / 2

Correct:

average = total / len(numbers)


CHECK CONDITIONS
----------------

Example:

age = 18

if age > 18:
    print("Adult")
else:
    print("Minor")

If the requirement is:

18 and above = Adult

Then the condition should be:

if age >= 18:


CHECK LOOP RANGES
-----------------

Example:

for i in range(1, 5):
    print(i)

Output:

1
2
3
4

range() stops BEFORE the ending value.

To include 5:

for i in range(1, 6):
    print(i)


FIND WHERE THE RESULT BECOMES WRONG
------------------------------------

Don't only inspect the final result.

Check every stage:

Input
 ↓
Read
 ↓
Clean
 ↓
Transform
 ↓
Calculate
 ↓
Output

Example:

numbers = [10, 20, 30]

print("Original:", numbers)

numbers = [x * 2 for x in numbers]
print("After multiplication:", numbers)

numbers = [x + 5 for x in numbers]
print("After addition:", numbers)

total = sum(numbers)
print("Total:", total)

The goal is to find:

"At which step did the data FIRST become wrong?"


IMPORTANT DEBUGGING TOOLS
-------------------------

Print a value:

print(variable)

Check its type:

print(type(variable))

Check length:

print(len(variable))

Check dictionary keys:

print(data.keys())

Check file existence:

os.path.exists("file.txt")

Use breakpoint:

breakpoint()

PDB commands:

p variable  → inspect variable
n            → step over
s            → step into
r            → step out
c            → continue
l            → show source
q            → quit debugger


DEBUGGING MINDSET
-----------------

When something goes wrong:

1. Reproduce the problem.
2. Read the error or observe the unexpected result.
3. Find where the problem occurs.
4. Inspect variables.
5. Check variable types.
6. Check intermediate values.
7. Find where the value first becomes wrong.
8. Identify the cause.
9. Fix the code.
10. Test again.

MOST IMPORTANT RULE:

Don't ask only:

"Why is the final result wrong?"

Ask:

"At which step did the value first become wrong?"
