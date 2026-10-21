
import os

file_path = r'C:\Users\IIINeonIII\Desktop\Data Processing\content.txt'
# print(os.path.abspath(file_path))
# print(os.path.exists(file_path))
#
# print(os.path.exists("C:/Users"))
# print(os.path.exists("C:/Users/IIINeonIII"))
# print(os.path.exists("C:/Users/IIINeonIII/Desktop"))
# print(os.path.exists("C:/Users/IIINeonIII/Desktop/Data Processing"))
#


with open(file_path, 'r') as f:
    content_extras = f.read()
    print(content_extras)
    print(type(content_extras))

with open(file_path, 'r') as f:
    content_extras_2 = f.readlines()
    print(content_extras_2)
    print(type(content_extras_2))


path_img = r'C:\Users\IIINeonIII\Desktop\Data Processing\cerc.jpg'
with open(path_img, 'rb') as f:
    content_extras_4 = f.read()
    # print(content_extras_4)


path_exemplu = r'C:\Users\IIINeonIII\Desktop\Data Processing\exemplu.txt'

with open(path_exemplu, 'w', encoding='utf-8') as f:
    f.write("Hello World\n")
    f.write("\nSecond line\n")

with open(path_exemplu, 'a', encoding='utf-8') as f:
    f.write("\nThis is an extra line I have added afterwards.\n")

with open(path_exemplu, 'r+') as f:
    print("Initial text:\n",f.read())
    f.write("\nThis is the last line.")

with open(path_exemplu, 'r') as f:
    f.seek(6)
    text=f.read(13)
    print(text)


with open(path_exemplu, 'r') as f:
    lines = f.readlines()
    if len(lines) > 5:
        print("The 6th line is :", lines[6])
    else:
        print("Less than 5 lines detected.")









