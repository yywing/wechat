import os


file_path = os.path.join(os.path.abspath("web-nb"),"zhihu_girls")
file_list = os.listdir(file_path)
print(file_list)
dir_list=[]
for i in file_list :
    if os.path.isdir(i):
        dir_list.append(i)
 
print(len(dir_list))
