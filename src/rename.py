import os

def rename_files(input_folder):
    # Sort the files in the folder based on their names
    files = sorted(os.listdir(input_folder))
    # Iterate over the sorted files and rename them sequentially
    for i, filename in enumerate(files):
        # Extract the file extension
        ext = os.path.splitext(filename)[1]
        # Create the new filename with a sequential number
        new_filename = f"vi4_{i+1}{ext}"
        # Rename the file
        os.rename(os.path.join(input_folder, filename), os.path.join(input_folder, new_filename))

# Example usage
input_folder = '/home/anchidta/wk_law/selected_frames_vi4'
rename_files(input_folder)
