import os

# a = os.getcwd()
# print(a)
#
'''
makedirs
mkdir
chdir
listdir
'''


# # def soldier(path,file,format):
#
# f = open(file_path, "r")
# list1 = f.readlines()
# for i in list1:
#     print(i.split("\\"))
#     # print(i.split("\\")[1])

def soldier(path,file,format):
    os.chdir(path)
    f = open(file, "r")
    files_text = f.read().split("\n")
    print(files_text)
    files_folder = os.listdir(path)
    print(files_folder)
    i = 1
    for files in files_folder:
        print(os.path.splitext(files))
        if (files+"\n") not in files_text:
            os.rename(files, files.capitalize())
        if os.path.splitext(files)[1] == format:
            os.rename(files, f"{i}{format}")
            i += 1




file_path = "C:\\Users\\admin\Desktop\prettified folder"
os.chdir("C:\\Users\\admin\Desktop")
b = os.getcwd()
print(b)

text_path = os.path.join(b, "akash.txt")

soldier(file_path,text_path,".jpg")



