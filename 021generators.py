#GENERATORS >>> A generator is a special type of iterator that produces values one at a time, only when they are needed. Instead of creating and storing all values in memory at once, a generator generates each value when requested. The biggest advantage is memory efficiency.

# yield returns a value but pauses the function instead of completely ending it.

def nums():
    yield 1
    yield 2
    yield 3

gen = nums()
print(next(gen))
print(next(gen))
print(next(gen))

def yield_check():
    print("Start")
    yield 1

    print("Mid")
    yield 2

    print("End")
    yield 3

gen1 = yield_check()
print(next(gen1))
print(next(gen1))
print(next(gen1))


#using a generator with loop
def numbers():
    yield 1
    yield 2
    yield 3

for num in numbers():
    print(num)


numbers = (num for num in range(0,5)) #this is generator expression and we can loop through it one by one using iteration NOTE: it wont work with list comprehension etc
print(next(numbers))
print(next(numbers))
print(next(numbers))
for num in numbers: #the next() was already at 2
    print(num) #this will print 3 and 4

#Question 1: Basic Generator - Create a generator function called count_numbers() that generates the numbers from 1 to 5 using yield. Then: Store the generator object in a variable. Use next() to print the first two values. Use a for loop to print the remaining values.
def count_numbers():
    yield 1
    yield 2
    yield 3
    yield 4
    yield 5
gen_obj = count_numbers()
print(next(gen_obj))
print(next(gen_obj))
for num in gen_obj:
    print(num)

#Question 2: Generator Expression - Given: numbers = [1, 2, 3, 4, 5, 6] Create a generator expression that generates the squares of only the even numbers. Then use a for loop to print the generated values.
numbers = [1, 2, 3, 4, 5, 6]
even_sq = (num**2 for num in numbers if num%2==0)
for num in even_sq:
    print(num)

