import os
from collections import defaultdict

# Specify the directory where the "cattle" folders are located
base_directory = r"F:\All_Annotated_Final\INDIVIDUAL SUBJECTS Data"

# Define a list of common image extensions
image_extensions = [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tif", ".tiff"]

# Create a dictionary to store counts for each image extension
image_counts = defaultdict(int)

# Function to count images in a directory and its subdirectories
def count_images_in_directory(directory):
    for root, _, files in os.walk(directory):
        for file in files:
            # Check if the file has a recognized image extension
            file_extension = os.path.splitext(file)[1].lower()
            if file_extension in image_extensions:
                image_counts[file_extension] += 1

# Loop through all folders and count images in each of them
for folder_name in os.listdir(base_directory):
    folder_path = os.path.join(base_directory, folder_name)
    print(folder_path)
    
    if os.path.isdir(folder_path):
        count_images_in_directory(folder_path)

# Print the image counts for each extension
for ext, count in image_counts.items():
    print(f"Total {ext} images: {count}")

# Print the total count of all recognized image extensions
total_images = sum(image_counts.values())
print(f"Total images in all folders: {total_images}")
