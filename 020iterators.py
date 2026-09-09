#ITERATORS: An iterator is an object that allows us to go through elements one at a time. An iterable is an object that can be looped through. e.g list, tuple, set, string etc


numbers = [1,2,3,4,5]

iterator = iter(numbers)
print(next(iterator)) #it remembers the item number 
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator)) #when the list in over next() causes Stopiteration

#a for loop: Calls iter() to create an iterator. Calls next() repeatedly. Stops when StopIteration occurs.
for num in numbers:
    print(num)

# For an object to behave as an iterator, it needs two important methods:
# __iter__() inside works like object.__iter__()
# Returns the iterator object.
# __next__() inside works like iterator.__next__()
# Returns the next value.

#Question 1: Basic Iterator - Given: numbers = [10, 20, 30, 40, 50] Convert numbers into an iterator. Use next() to print the first three values. Use a for loop to print the remaining values from the same iterator.
numbers = [10,20,30,40,50]
iterator = iter(numbers)
print(next(iterator))
print(next(iterator))
print(next(iterator))

for num in iterator:
    print(num)

#Question 2: Iterator with a String - Given: name = "Python" Create an iterator from name. Use next() to print the first three characters. Then use a for loop to print the remaining characters from the same iterator.
name = "Python"
it = iter(name)
print(next(it))
print(next(it))
print(next(it))

for name in it:
    print(name)