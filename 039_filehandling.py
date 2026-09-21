# # FILE HANDLING: File handling means using Python to create, read, write, modify, and manage files stored on your computer. python can work on files like .txt, .csv, .json, .log, .dat

# #variables can store data temporarily (till the program runs) while files can store data permenantly

# #File Path >>> tells python where a file is located
# # there are 2 main types >>> 1. Relative path 2. Absolute path

# #Relative path >>> where a file is located as relative to the current python programs location e.g "035data.txt" (same folder as the python file) or "calculator/advance.py"
# # open("035data.txt", "r")

# #Absolute path >>> complete location of the file "C:\Users\Adnan\Documents\data.txt"
# # open("~Adnan/Documents/data.txt", "r")

# #NOTE: Relative paths are generally more portable than hard-coded absolute paths.


# #open() >>> used to open a file
# file1 = open("039_data.txt","r")
# data = file1.read()
# print(data)
# file1.close()

# #File modes >>> r - read, w - write, a - append, x - create, rb - read binary, wb - write binary


# # r -> read >>> used to read an existing file
# file1 = open("039_data.txt","r")
# data = file1.read()
# print(data)
# file1.close()

# try:
#     file2 = open("data.txt", "r") #>>> this will throw an error since the file doesnt exist
# except Exception as e:
#     print(e)



# # w -> write >>> used to write on a file >>> will replace eveything on the file and overwrites with the new content and if the new_file doesnt exist it will create a new file

# file = open("039_data.txt", "w")
# file.write("This is being written from python program")
# file.close()

# file3 = open("039_new_file.txt", "w")
# file3.write("Hello new_file")
# file3.close()

# # a - append >>> Adds data to the end of an existing file.
# file = open("039_data.txt", "a") #can create a new file if the file doesnt exist
# file.write("\nThis is new line appended by python program")
# file.close()


# # x - creates a new file and if the file already exists it ll throw and error
# try:
#     file = open("039_data3.txt","x")
# except Exception as e:
#     print(e)


# # rb, wb _ read binary, write binary >>> used for images, pdfs, audios etc



# #Reading files
# #python provides three ways for this

# #read() >>> reads the entire file
# file = open("039_data.txt", "r")
# print(file.read())
# # print(file.read(5)) # or we can mention the number of characters we want to print
# file.close()


# print("------------")

# # readline() >>> reads one line at a time
# file = open("039_data.txt", "r")
# print(file.readline())
# print(file.readline())


# # readlines() >>> returns all the lines as list of strings
# file = open("039_data.txt", "r")
# lines = file.readlines()
# print(lines)
# file.close()




# #read write append etc using "with open" >>> this will close the file resources even if an error occurs
# with open("039_data.txt", "r") as file:
#     data = file.read()
# print(data)

# with open("039_data.txt", "a") as file:
#     file.write("\This is new line using append --- ")

# #working with multiple files
# with open("039_data.txt","r") as file1:
#     with open("039_data1.txt", "r") as file2:
#         data1 = file1.read()
#         data2 = file2.read()

# #cleaner way
# with open("039_data.txt","r") as file1, open("039_data1.txt", "r") as file2:
#         data1 = file1.read()
#         data2 = file2.read()



# # os Module >>> The os module allows Python to interact with the operating system.
import os
# os.mkdir("new_dir0") #to create a new directory

# os.makedirs("new_dir1/sub_dir") #to create nested dirs

# print(os.listdir("new_dir1")) #tells us what is in the directory

# os.rmdir("new_dir0") #removes one dir if the directory is empty

# os.removedirs("new_dir1/sub_dir")

# os.rename("039_new_file.txt","039newFile.txt" ) #change file name

folder = "new"
subfolder = "sub_new"
filename = "file.txt"
fullpath = os.path.join(folder, subfolder, filename)
dir_path = os.path.dirname(fullpath)
if not os.path.exists(dir_path):
    os.makedirs(dir_path)
    print(f"{dir_path}")
if not os.path.isfile(fullpath):
    with open(fullpath, 'w') as file:
        file.write("This is my file.txt")
        print(f"{fullpath}")

