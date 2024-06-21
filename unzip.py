import os
import zipfile

def unzip_files_in_directory(directory):
    # Change to the specified directory
    os.chdir(directory)

    # List all files in the directory
    files = os.listdir(directory)

    # Iterate over each file
    for file in files:
        # Check if the file is a zip file
        if file.endswith('.zip'):
            # Create a folder name from the zip file name (without the .zip extension)
            folder_name = file[:-4]

            # Create the directory if it doesn't exist
            if not os.path.exists(folder_name):
                os.makedirs(folder_name)

            # Unzip the file into the corresponding folder
            with zipfile.ZipFile(file, 'r') as zip_ref:
                zip_ref.extractall(folder_name)

            print(f"Unzipped {file} into {folder_name}")

if __name__ == "__main__":
    # Specify the directory containing the zip files
    directory = "/home/alessioc/UNIS_hydrographic_data_to_cfnetcdf/data/original_data" 
    unzip_files_in_directory(directory)
