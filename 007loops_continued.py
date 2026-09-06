# #nested loop
# for i in range(10):
#     for j in range(10):
#         print(i,j)

#using else with loop
for i in range(5):
    print(i)
else:
    print("loop completed")

print()

#if there is a break in loop the else statement wont run
for i in range(5):
    if i==4:
        break
    print(i)
else:
    print("loop completed")

print()

# combining loops and conditionals
for i in range(1,11):
    if i%2==0:
        print(i)
