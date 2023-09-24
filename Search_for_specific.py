import os

# Specify the directory where the "cattle" folders are located
base_directory = r"F:\All_Annotated_Final\INDIVIDUAL SUBJECTS Data"

# Prompt the user for the filename to search for
file_to_search = input("Enter the filename to search for: ")

# Function to search for a file by name in a directory and its subdirectories
def search_file_by_name(directory, filename):
    matching_files = []
    for root, _, files in os.walk(directory):
        for file in files:
            if file == filename:
                matching_files.append(os.path.join(root, file))
    return matching_files

# Loop through all folders and search for the file by name
for folder_name in os.listdir(base_directory):
    folder_path = os.path.join(base_directory, folder_name)

    if os.path.isdir(folder_path):
        matching_files = search_file_by_name(folder_path, file_to_search)

        if matching_files:
            print(f"Files matching '{file_to_search}' in {folder_path}:")
            for file_path in matching_files:
                print(file_path)

if not matching_files:
    print(f"No files matching '{file_to_search}' found.")
