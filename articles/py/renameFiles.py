import os

def rename_files_in_folder(folder_path):
    try:
        # List all files in the directory
        files = os.listdir(folder_path)
        
        for file in files:
            # Ignore directories, only process files
            if os.path.isfile(os.path.join(folder_path, file)):
                # Split the filename into the base name and extension
                file_name, file_extension = os.path.splitext(file)
                
                # Generate the new file name using the first 3 characters
                new_name = file_name[:3] + "_JohnEraHistory" + file_extension
                
                # Create full paths
                old_file = os.path.join(folder_path, file)
                new_file = os.path.join(folder_path, new_name)
                
                # Rename the file
                os.rename(old_file, new_file)
                print(f'Renamed: {old_file} -> {new_file}')
                
        print("All files have been successfully renamed!")
    except Exception as e:
        print(f"An error occurred: {e}")

# Specify the folder path
folder_path = "source\\articles\\pdfs"  # Replace this with your folder path
rename_files_in_folder(folder_path)
