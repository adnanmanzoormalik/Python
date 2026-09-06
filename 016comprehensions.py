#LIST COMPREHENSIONS >>>shorter way to create a list using a loop

#NORMALLY WE DO THIS
nums = [1,2,3,4,5]
sq = []
for num in nums:
    sq.append(num**2)
print(sq)

#but in list comprehension we do this
squares = [num**2 for num in nums]
print(squares)

#another example
names = ["adnan", "asrar", "zaira"]
cap_names = [name.upper() for name in names]
print(cap_names)

#we can also use range in this
sq_nums = [i ** 2 for i in range(0,6)]
print(sq_nums)



#using if and loop
#normally
nums_a = [1,2,3,4,5,6]
even_nums = []
for num in nums_a:
    if num%2==0:
        even_nums.append(num)
print(even_nums)

#comprehensional way
even_nums1 = [num for num in nums_a if num%2==0]
print(even_nums1)

#filtering with comprehension
names = ["adnan", "asrar", "saad", "ali", "zaira"]
names_filtered = [name for name in names if len(name)>4]
print(names_filtered)

nums_1 = [1,2,3,4,5,6]
fig_nums1 = [f"{num} is even" if num%2 == 0 else f"{num} is odd" for num in nums_1]
print(fig_nums1)

#nested loop

matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
#normal way
result=[]
for row in matrix:
    for num in row:
        result.append(num)
print(result)

#comprehension
result1 = [num for row in matrix for num in row]
print(result1)

#combine 2 lists
numbers = [1, 2, 3]
letters = ["a", "b"]
combined_list = [(number, letter) for number in numbers for letter in letters]
print(combined_list)

# One loop: [expression for item in iterable]
# One loop with filtering: [expression for item in iterable if condition]
# Conditional transformation: [value_if_true if condition else value_if_false for item in iterable]
# Nested loops: [expression for outer in outer_iterable for inner in outer]



#DICTIONARY COMPREHENSION
numbers = [1,2,3,4,5,6,7,8]
dict_1 = {num : num**2 for num in numbers}
print(dict_1)

dict_2 = {num:num**2 for num in numbers if num%2==0}
print(dict_2)



#SET COMPREHENSION >>>diff between set and dict comprehension is ":"
nums_set = {i for i in range(0,6)}
print(nums_set)


#Q1. Number Analyzer - Given: numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] Using list comprehensions only: Create a list containing the squares of all even numbers. Create a list where each number is replaced with "Even" or "Odd".
numbers = [1,2,3,4,5,6,7,8,9,10]
sq_nums = [num**2 for num in numbers if num%2==0]
even_odd = ["Even" if num%2==0 else "Odd" for num in numbers]

#Q2. Matrix and Nested Comprehension Given: matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9] ]Using a nested list comprehension: Convert the matrix into a single flat list. Bonus: Create a flat list containing only the even numbers.
matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
flat_list = [num for row in matrix for num in row]
even_flat_list = [num for row in matrix for num in row if num%2==0]

#Q3. Dictionary and Set Comprehensions - Given: names = ["adnan", "ali", "john", "adnan", "sara"] 
# Part A — Dictionary Comprehension Create a dictionary where: Each name is the key The length of the name is the value  Notice that the duplicate "adnan" will appear only once because dictionary keys must be unique.
#Part B — Set Comprehension - Create a set containing the uppercase versions of all names. The duplicate should automatically be removed because sets only store unique values.
names = ["adnan", "ali", "john", "adnan", "sara"]

names_len = {name:len(name) for name in names }
names_upper = {name.upper() for name in names}