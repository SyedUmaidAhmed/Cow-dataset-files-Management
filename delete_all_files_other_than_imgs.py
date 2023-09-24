import os

# Specify the directory where you want to delete files
base_directory = r"F:\All_Annotated_Final\INDIVIDUAL SUBJECTS Data"

# Function to delete files with specified extensions in a directory and its subdirectories
def delete_files_with_extensions(directory, extensions):
    for root, _, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            file_extension = os.path.splitext(file_path)[1].lower()
            if file_extension in extensions:
                try:
                    # Delete the file
                    os.remove(file_path)
                    print(f"Deleted: {file_path}")
                except Exception as e:
                    print(f"Error deleting {file_path}: {e}")

# Specify the extensions of files to delete
extensions_to_delete = [".xml", ".txt"]

# Delete files with specified extensions in all folders
delete_files_with_extensions(base_directory, extensions_to_delete)
