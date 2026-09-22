dir1_name = "main"
dir1_1name = "sub"
filename = "file.txt"

import os
full_path = os.path.join(dir1_name, dir1_1name, filename)
dir_path = os.path.dirname(full_path)

if not os.path.exists(dir_path):
    os.makedirs(dir_path)
    print(dir_path)

if not os.path.isfile(full_path):
    with open(full_path, "w") as file:
        file.write("This is made using os")
        print(full_path)