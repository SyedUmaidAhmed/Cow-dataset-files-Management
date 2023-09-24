import os
import hashlib

# Specify the directory where the "cattle" folders are located
base_directory = r"F:\All_Annotated_Final\INDIVIDUAL SUBJECTS Data"

# Create a dictionary to store file hashes and their corresponding paths
file_hashes = {}

# Define a list of common image extensions
image_extensions = [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tif", ".tiff"]

# Function to calculate the hash of a file
def calculate_file_hash(file_path):
    try:
        hasher = hashlib.md5()
        with open(file_path, "rb") as f:
            while True:
                data = f.read(65536)  # Read the file in 64KB chunks
                if not data:
                    break
                hasher.update(data)
        return hasher.hexdigest()
    except Exception as e:
        print(f"Error while calculating hash for {file_path}: {e}")
        return None

# Function to find duplicate image files in a directory and its subdirectories
def find_duplicate_image_files_in_directory(directory):
    for root, _, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            file_extension = os.path.splitext(file_path)[1].lower()
            if file_extension in image_extensions:
                file_hash = calculate_file_hash(file_path)
                if file_hash:
                    if file_hash in file_hashes:
                        # Duplicate image file found
                        print(f"Duplicate image file: {file_path}")
                        print(f"Original image file: {file_hashes[file_hash]}")
                    else:
                        # Store the file hash and path
                        file_hashes[file_hash] = file_path

# Loop through all folders and find duplicate image files
for folder_name in os.listdir(base_directory):
    folder_path = os.path.join(base_directory, folder_name)
    
    if os.path.isdir(folder_path):
        find_duplicate_image_files_in_directory(folder_path)
