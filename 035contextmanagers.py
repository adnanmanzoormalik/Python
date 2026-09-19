# Context manager: is a Python mechanism that manages a resource for you.
# Common resources include: Files, Database connections, Network connections, Locks, Other resources that need cleanup

file = open("035data.txt", "r")
content = file.read()
print(content)
file.close() #if something goes wrong before this, it will never be executed and file resource wont be cleaned up

#>>> Before context managers, you could make cleanup more reliable with
file = open("035data.txt", "r")
try:
    content = file.read()
    print(content)
    print(file.closed)
finally: #finally is used for cleanup that must happen regardless of whether an exception occurs.
    file.close()
    print(file.closed)


    print()

#with block >>> creates a context in which the resource is being used. When the block ends, Python performs the necessary cleanup.
#with is not used only with files but with db_connections or any other resource
with open("035data.txt","r") as file:
    content = file.read()
print(content)

print(file.closed) #this way we can check whether file resource is closed or not


#context manager + exception

try:
    with open("035data.txt", "r") as file:
        content = file.read()
        print(10/0) #this will throw an error but file resource will also be closed due to with block
except ZeroDivisionError:
    print("Cant be divided by zero")


#Managing multiple context managers: Python allows you to use multiple context managers in a single with statement.
with open("035data.txt", "r") as file1, open("035data1.txt", "r") as file2:
    print(file1.read())
    print(file2.read())

with open("035data.txt", "r") as file1: #we can write multiple context managers like this but the above is a cleaner version
    with open("035data1.txt", "r") as file2:
        print(file1.read())
        print(file2.read())


#reading and writing a file using with
with open("035data.txt", "r") as file1, open("035data1.txt", "w") as file2:
    data = file1.read()
    file2.write(data)

#order of cleanup >>> happens in a reverse order - works like a stack i.e file2 will be cleaned up first and then file1




#realistic example
try:
    with open("035data.txt", "r") as file:
        data = file.read()
        print(data)
    if not data:
        raise ValueError("config data not found.")

except FileNotFoundError:
    print("Config file not found")

except ValueError as e:
    print("Error: ", e)


## Q1 — Read a File with Context Manager
# 1. Open "data.txt" in read mode using with open().
# 2. Read the complete file.
# 3. Print the file content.
# 4. Handle FileNotFoundError.
# 5. If the file doesn't exist, print: "File not found."
# 6. Do NOT use file.close() manually.

try:
    with open("data.txt","r") as file:
        data = file.read()
        print(data)
except FileNotFoundError:
    print("File not found.")


# Q2 — File Copying using Multiple Context Managers
# 1. Open "source.txt" in read mode.
# 2. Open "destination.txt" in write mode.
# 3. Use TWO context managers in the SAME with statement.
# 4. Read the contents of source.txt.
# 5. Write the contents into destination.txt.
# 6. Print: "File copied successfully."
# 7. Handle FileNotFoundError.
# 8. If source.txt does not exist, print: "Source file not found."
# 9. Use else to print: "Copy operation completed."
# 10. Use finally to print: "Program finished."

try:
    with open("source.txt","r") as file1, open("destinaton.txt", "w") as file2:
        data = file1.read()
        file2.write(data)
        print("File copied successfully")
except FileNotFoundError:
    print("Source file not found")
else:
    print("Copy operation completed")
finally:
    print("Program finished")