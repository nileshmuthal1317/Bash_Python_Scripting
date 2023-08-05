import os
import subprocess
import re

# Function to get user's choice for various options
def get_user_choice():
    while True:
        # Prompt user for input and convert to lowercase
        choice = input("\nDo you want to (r)un the file, (v)iew its content, (e)dit it, (s)kip, or (q)uit? (r/v/e/s/q): ").lower()
        if choice in ('r', 'v', 'e', 's', 'q'):
            # Return the user's choice if it is valid
            return choice
        # Inform user about invalid choice and continue the loop
        print("Invalid choice. Please try again.")

# Function to process Python files in a directory
def process_python_files(directory):
    # Create a list of Python script files in the specified directory
    files_list = [filename for filename in os.listdir(directory) if filename.endswith('.py')]

    # Sort the list of files based on their numeric prefix (if present) in filenames
    files_list.sort(key=lambda x: int(re.search(r'^\d+', x).group()) if re.search(r'^\d+', x) else float('inf'))

    # Display the list of available files along with their indices
    print("\nList of available files:\n")
    for i, filename in enumerate(files_list, start=1):
        print(f"{i}. {filename}")

    # Ask user to enter the filename to skip to
    target_file = input("\nEnter the filename to skip to (e.g., 01_<File_Name>.py): ")
    if target_file in files_list:
        # If the specified file is found in the list, set the current_file_index to its index
        current_file_index = files_list.index(target_file)
    else:
        # If the specified file is not found, inform the user and start processing from the beginning
        print(f"\nFile '{target_file}' not found. Starting from the beginning.")
        current_file_index = 0

    # Get the total number of files in the list
    total_files = len(files_list)

    # Loop through each file from the current_file_index until all files are processed
    while current_file_index < total_files:
        # Get the filename from the files_list using the current_file_index
        filename = files_list[current_file_index]
        # Create the full path to the file using the directory and filename
        file_path = os.path.join(directory, filename)
        print(f"\nProcessing {filename}...")

        # Read the original content of the file
        with open(file_path, 'r') as file:
            original_content = file.read()

        # Get user choice for each step
        user_choice = get_user_choice()

        if user_choice == 'r':
            try:
                # Execute the Python code and capture the output
                output = subprocess.check_output(['python3', file_path], universal_newlines=True)
                print(f"\nOutput:\n{output}")

                # Ask for user confirmation to add the output to the file
                add_output = input("Do you want to add the output to the file? (y/n): ").lower()
                if add_output == 'y':
                    # Add the output as a comment block at the end of the file
                    updated_content = original_content + f'\n\n"""\nOutput:\n{output}"""'

                    # Write the updated content back to the file
                    with open(file_path, 'w') as file:
                        file.write(updated_content)
                    print(f"\nOutput added to {filename}.")
                else:
                    print("\nOutput not added to the file.")

            except Exception as e:
                # Handle any exceptions that occur during execution
                print(f"\nError processing {filename}: {e}")

        elif user_choice == 'v':
            # Display the content of the file
            print(f"\nContent of {filename}:\n{original_content}")

        elif user_choice == 'e':
            print(f"\nOpening {filename} for manual update...")
            try:
                # Open the file in the default text editor (e.g., Vim) for manual updates
                subprocess.run(['vim', file_path])

                # Wait for the user to press Enter after saving changes in the file
                input("\nPress Enter after saving changes in the file.")
            except Exception as e:
                # Handle any exceptions that occur during file opening or editing
                print(f"\nError opening {filename}: {e}")

        elif user_choice == 's':
            # Skip to the next file
            current_file_index += 1

        elif user_choice == 'q':
            # Quit the script
            print("\nExiting the script...")
            return

        # Inform the user that processing of the current file is completed
        print(f"\nDone processing {filename}...")
        print("-" * 50)

# Entry point of the script
if __name__ == "__main__":
    # Get the current directory and process Python files in it
    current_directory = os.getcwd()
    process_python_files(current_directory)
