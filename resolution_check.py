import os
from PIL import Image

# Specify the directory where the "cattle" folders are located
base_directory = r"F:\All_Annotated_Final\INDIVIDUAL SUBJECTS Data"

# Create a set to store unique image resolutions
unique_resolutions = set()

# Function to get the resolution of an image
def get_image_resolution(image_path):
    try:
        with Image.open(image_path) as img:
            width, height = img.size
            return f"{width}x{height}"
    except Exception as e:
        print(f"Error while processing {image_path}: {e}")
        return None

# Function to find unique resolutions in a directory and its subdirectories
def find_unique_resolutions_in_directory(directory):
    for root, _, files in os.walk(directory):
        for file in files:
            # Check if the file has a recognized image extension
            file_extension = os.path.splitext(file)[1].lower()
            if file_extension in {".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tif", ".tiff"}:
                image_path = os.path.join(root, file)
                resolution = get_image_resolution(image_path)
                if resolution:
                    unique_resolutions.add(resolution)

# Loop through all folders and find unique resolutions
for folder_name in os.listdir(base_directory):
    folder_path = os.path.join(base_directory, folder_name)
    
    if os.path.isdir(folder_path):
        find_unique_resolutions_in_directory(folder_path)

# Print the unique resolutions
print("Unique Resolutions:")
for resolution in sorted(unique_resolutions):
    print(resolution)
