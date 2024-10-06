import os

path = input("Enter the path")
folder_names = ['PDf', 'PNG', 'JPEG', 'EXE']
for folder_name in folder_names:
    temp_path = os.join(path, folder_name)
    os.mkdir(temp_path)
