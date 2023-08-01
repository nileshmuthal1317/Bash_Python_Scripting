# Importing the os and shutil lib to use in this script

import os
import shutil

# Defining function to get the source and target dir from the user as parameter

def organize_files(source_dir, target_dir):
   # Create the target directory if it doesn't exist
    if not os.path.exists(target_dir):
        os.makedirs(target_dir)

    # Listing and Iterate thrugh each file
    for filename in os.listdir(source_dir):
        # Getting the source file path ex. /sourcedir/sourcefile1.txt
        source_file_path = os.path.join(source_dir, filename)

        # Skip directories
        if os.path.isdir(source_file_path):
            # continue to check the next file
            continue

        # Get the file extension (including the dot), the os.path.splitext split the file into two part 
        # 0 means path to the file /path/filenamenoext, 1 means the ext only, 
        # lower() will convert the ext in lower case 
        file_extension = os.path.splitext(filename)[1].lower()

        # Define categories and their corresponding folders
        categories = {
            '.txt': 'TextFiles',
            '.doc': 'WordDocuments',
            '.docx': 'WordDocuments',
            '.pdf': 'PDFs',
            '.png': 'Images',
            '.jpg': 'Images',
            '.jpeg': 'Images',
            '.gif': 'Images',
            '.mp3': 'Music',
            '.mp4': 'Videos',
            '.avi': 'Videos',
            '.exe': 'Executables',
            '.zip': 'Archives',
        }

        # Choose 'Others' if the extension is not in the categories dictionary
        # get function will put the key file into value directory exp nilesh.txt to Text folder
        # dictionary.get(key, default_value) the get() function is primarily used with dictionaries in Python.
        # get function used when we unsure if the key exists in the dictionary
        category = categories.get(file_extension, 'Others')

        # Create the category folder if it doesn't exist
        # category_dir = "/path/to/target_directory/Image"
        category_dir = os.path.join(target_dir, category)
        if not os.path.exists(category_dir):
            os.makedirs(category_dir)

        # Move the file to the corresponding category folder
        target_file_path = os.path.join(category_dir, filename)
        shutil.move(source_file_path, target_file_path)
        # The f-string syntax allows you to embed expressions or variables within curly braces {} inside a string.
        print(f"Moved: {filename} -> {target_file_path}")

#  the __name__ variable is set to "__main__". This allows you to determine whether the script is being run as the main program or if it is being imported as a module into another program.
if __name__ == "__main__":
    source_directory = "/root/notsorted"  # Replace with the source directory path
    target_directory = "/root/sorted"  # Replace with the target directory path

    organize_files(source_directory, target_directory)
