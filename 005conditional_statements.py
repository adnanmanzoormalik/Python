#if, if_else, if_elif_else

age = 20
if age>=18:
    print("You can vote")

age1 = 17
if age1 >= 18:
    print("You can vote")
else:
    print("You cant vote")

marks = 75
if marks > 90:
    print("Excellent")
elif marks > 80:
    print("Very good")
elif marks > 70:
    print("Good")
elif marks > 60:
    print("Okay")
else:
    print("Less")

is_raining = False
if is_raining:
    print("You cant go outside")
else:
    print("You can go outside")

age = 20
if age>=18 and age<=30:
    print("young adult")
else:
    print("dont know")

has_license=False
if age >= 18:
    if has_license:
        print("Can drive")
    else:
        print("Needs DL")
else:
    print("Cant drive")

name = "adnan"
if name == "adnan":
    print("name matches")


#match and case (only works in python 3.10 or newer)>>> python doesnt have switch case like C, java etc
day = 6
match day:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case 4|5|6|7:
        print("thur, fri, sat, sun")
    case _:
        print("Invalid day")