#map() >>> applies a function to every element in an iterable such as a list.

numbers = [1,2,3,4,5,6]
def sq(num):
    return num**2
result = map(sq, numbers)
print(list(result))


names = ["adnan", "asrar", "zaira"]
result = list(map(lambda x: x.upper(), names))
print(result)

double1 = list(map(lambda x: x*2, numbers))
print(double1)

# Q1. Given: numbers = [1, 2, 3, 4, 5] Use map() and a lambda function to create a new list where every number is squared.
numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(lambda x: x**2, numbers))
print(squared_numbers)

#Q2: One more map() practice - Given: names = ["adnan", "python", "developer", "srinagar"] Use map() and lambda to create a new list containing the length of each word.
names = ["adnan", "python", "developer", "srinagar"]
len_names = list(map(lambda x: len(x), names))
print(len_names)



#filter()

numbers = [1,2,3,4,5,6]
even_nums = list(filter(lambda x: x%2==0, numbers))
print(even_nums)

#Q2. Filter Names by Length - Given: names = ["ali", "adnan", "ahmad", "python", "developer"] Use filter() and lambda to create a new list containing only names/words with more than 5 characters.
names = ["ali", "adnan", "ahmad", "python", "developer"]
long_names = list(filter(lambda x:len(x)>5, names))
print(long_names)


#reduce() >>> any items → one final value
from functools import reduce #necessary for reduce
numbers = [1,2,3,4,5,6]
sum1 = reduce(lambda x,y: x+y, numbers)
print(sum1)

# Q1. Find the Product of All Numbers Given: numbers = [2, 3, 4, 5] Use reduce() and a lambda function to multiply all the numbers together.
numbers = [2, 3, 4, 5]
mul = reduce(lambda a,b: a*b, numbers)
print(mul)

#Q2. Find the Largest Number - Given: numbers = [12, 45, 7, 89, 34, 100, 23] Use reduce() and a lambda function to find the largest number in the list.
numbers = [12, 45, 7, 89, 34, 100, 23]
largest = reduce(lambda a,b: a if a>b else b, numbers)
print(largest)