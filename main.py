# project 1- curd operation


from pathlib import Path
import os
def readfileandfolder():

    try:
        P = Path("")
        items = list(P.rglob("*"))
        for index , file in enumerate(items):
            print(f"{index+1} - {file} ")
    except Exception as e:
        print(e)

def create_file():
    try:
        readfileandfolder()
        file_name = input("enter your file name: ")
        p = Path(file_name)
        if p.exists():
            print("FILE ALREADY EXIST")
        else:
            with open(file_name,'w') as file:
                content = input("enter your file content:")
                file.write(content)
                print('FILE ADDED!')
    except Exception as e:
        print(e)




def read_file():
    try:
        readfileandfolder()
        file_name = input("enter your file name: ")
        p = Path(file_name)
        if p.exists():
            with open(file_name,'r') as file:
                print(file.read())
        else:
            print('FILE NOT FOUND!')
    except Exception as e:
        print(e)

def update_file():
    try:
        readfileandfolder()
        file_name = input("enter your file name: ")
        p = Path(file_name)
        if p.exists():
            print('press 1 to overwrite the content')
            print('press 2 to append new content')
            
            option = int(input('enter your choice for updating a file'))
            if option == 1:
                with open(file_name,'w') as file:
                    content = input('enter your content')
                    file.write(content)
                    print('CONTENT CHANGED...')
            elif option == 2:
                with open(file_name,'a') as file:
                    content = input('enter your content')
                    file.write(content)
                    print('CONTENT CHANGED...')
            else:
                print('INVALID INPUT')
        else:
            print('FILE DOES NOT EXIST! ')    
    except Exception as e:
        print(e)

def delete_file():
    try:
        readfileandfolder()
        file_name = input("enter your file name: ")
        p = Path(file_name)
        if p.exists():
            os.remove(p)# os is delete the path of the file for thr system
            print('FILE DELETED...')
        else:
            print('FILE DOES NOT EXISTS!..')
    except Exception as e:
        print(e)

def rename_file():
    try:
        readfileandfolder()
        file_name = input("enter your file name: ")
        p = Path(file_name)
        if p.exists():
            new_file = input('enter new name of your file:')
            p.rename(new_file)
            print('FILE RENAME')
        else:
            print('FILE NOT FOUND!')
    except Exception as e:
        print(e)

def create_folder():
    try:
        readfileandfolder()
        folder_name = input('enter name of your folder')
        p = Path(folder_name)
        if p.exists():
            print('FOLDER ALREADY EXIST!')
        else:
            p.mkdir()
            print('FOLDER CREATED!')
    except Exception as e:
        print(e)

def delete_folder():
    try:
        readfileandfolder()
        folder_name = input('enter name of your folder')
        p = Path(folder_name)
        if p.exists():
            p.rmdir()
            print('FOLDER DELETED!')
        else:
            print('FOLDER NOT FOUND!')
    except Exception as e:
        print(e)

def create_file_in_folder():
    try:
        folder_name = input('enter your folder name')
        file_name = input('enter your file name')
        p = Path(folder_name/file_name)
        if p.exists:
            print('FILE ALREADY EXIST')
        else:
            p.mkdir()
            print('CREATED SUCCESSFULLY')
            with open(file_name,'w') as file:
                content = input('enter your file content')
                file.write(content)
                print('created successfully')
    except Exception as e:
        print(e)

while True:
    print("press 1 for creating a file")
    print("press 2 for reading a file")
    print("press 3 for updating a file")
    print("press 4 for deleting a file")
    print("press 5 for rename a file")
    print("press 6 for creating a folder")
    print("press 7 for deleting a folder")
    print('pres 8 for creating file in folder ')
    print("press 0 for exiting .......")

    option = int(input("entre your choice"))
    if option == 1:
        create_file()
        
    elif option == 2:
        read_file()

    elif option == 3:
        update_file()

    elif option == 4:
        delete_file()
    
    elif option == 5:
        rename_file() 
    
    elif option == 6:
        create_folder()
    
    elif option == 7:
        delete_folder()
    
    elif option == 8:
        create_file_in_folder()       

    elif option == 0:
        break

