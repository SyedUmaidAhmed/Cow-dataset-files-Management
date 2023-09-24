import os

# Specify the directory where the "cattle" folders are located
base_directory = r"F:\All_Annotated_Final\INDIVIDUAL SUBJECTS Data"

# Function to rename the folders to a perfect sequence
def rename_folders_to_perfect_sequence(directory):
    # Get a list of folders in the directory
    folders = [folder for folder in os.listdir(directory) if os.path.isdir(os.path.join(directory, folder))]
    folders.sort()  # Sort the folders alphabetically

    # Iterate through the sorted folders and rename them
    for index, folder_name in enumerate(folders, start=1):
        new_folder_name = f"cattle-{str(index).zfill(3)}"
        old_folder_path = os.path.join(directory, folder_name)
        new_folder_path = os.path.join(directory, new_folder_name)

        # Rename the folder
        os.rename(old_folder_path, new_folder_path)
        print(f"Renamed: {old_folder_path} -> {new_folder_path}")

# Rename the folders in the base directory to a perfect sequence
rename_folders_to_perfect_sequence(base_directory)
