# Version 0.1
# Author Nilesh Muthal
# script to automate the process of renaming files in a directory

import os # impoerted the lib

def rename_files(): # define the function
    # taking input from user and storing it in variable
    folder_path = input("Enter the folder path where the files are located: ")
    prefix = input("Enter the prefix you want to add to the filenames: ")

    # List all files in the directory
    # storing the folder path var value along with os.function in another variable
    files = os.listdir(folder_path)

    # Iterate through each file and rename it
    # using for loop because we want to repete the operation on multiple file names, here using index of file_name 0 1 2 ... in one of
    for index, file_name in enumerate(files):
        # Get the file extention
        file_extention = os.path.splitext(file_name)[1]

        # New filename with the specified prefix and index
        new_name = f"{prefix}_(index + 1){file extention}"

        # Join the old and new paths
        old_path = os.path.join(folder_path, file_name)
        new_path = os.path.join(folder_path, new_name)

        # Rename the file
        os.rename(old_path, new_path)

    print("File renamed successfully!")

def menu():
    print("File Renamer Script")
    print("1. Rename Files")
    print("2. Exit")

    choice = input("Enter your choice (1/2): ")

    if choice == '1':
        rename file()
    elif choice == '2':
        print("Goodbye!")
        exit()
    else:
        print("Invalide choise. Please try again.")
        menu()

    if __name__ == "__main__":
        while True:
            menu()# Version 0.1
# Author Nilesh Muthal
# script to automate the process of renaming files in a directory

import os # impoerted the lib

def rename_files(): # define the function
    # taking input from user and storing it in variable
    folder_path = input("Enter the folder path where the files are located: ")
    prefix = input("Enter the prefix you want to add to the filenames: ")

    # List all files in the directory
    # storing the folder path var value along with os.function in another variable
    files = os.listdir(folder_path)

    # Iterate through each file and rename it
    # using for loop because we want to repete the operation on multiple file names, here using index of file_name 0 1 2 ... in one of
    for index, file_name in enumerate(files):
        # Get the file extention
        file_extention = os.path.splitext(file_name)[1]

        # New filename with the specified prefix and index
        new_name = f"{prefix}_(index + 1){file extention}"

        # Join the old and new paths
        old_path = os.path.join(folder_path, file_name)
        new_path = os.path.join(folder_path, new_name)

        # Rename the file
        os.rename(old_path, new_path)

    print("File renamed successfully!")

def menu():
    print("File Renamer Script")
    print("1. Rename Files")
    print("2. Exit")

    choice = input("Enter your choice (1/2): ")

    if choice == '1':
        rename file()
    elif choice == '2':
        print("Goodbye!")
        exit()
    else:
        print("Invalide choise. Please try again.")
        menu()

    if __name__ == "__main__":
        while True:
            menu()
