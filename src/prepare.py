import os
from PIL import Image

# Function to delete duplicate images
def delete_duplicates(folder_path):
    seen_images = set()
    for filename in os.listdir(folder_path):
        filepath = os.path.join(folder_path, filename)
        if os.path.isfile(filepath):
            with open(filepath, 'rb') as f:
                file_hash = hash(f.read())
            if file_hash in seen_images:
                os.remove(filepath)
                print(f"Deleted duplicate: {filename}")
            else:
                seen_images.add(file_hash)

# Function to rename images to numeric order
def rename_images(folder_path):
    i = 1
    for filename in os.listdir(folder_path):
        filepath = os.path.join(folder_path, filename)
        if os.path.isfile(filepath):
            new_filename = str(i) + ".jpg"
            os.rename(filepath, os.path.join(folder_path, new_filename))
            print(f"Renamed {filename} to {new_filename}")
            i += 1

# Function to find minimum image size in folder
def min_image_size(folder_path):
    min_width = float('inf')
    min_height = float('inf')
    for filename in os.listdir(folder_path):
        filepath = os.path.join(folder_path, filename)
        if os.path.isfile(filepath):
            with Image.open(filepath) as img:
                width, height = img.size
                min_width = min(min_width, width)
                min_height = min(min_height, height)
    return min_width, min_height

# Function to resize images to minimum size
def resize_images(folder_path, target_size):
    for filename in os.listdir(folder_path):
        filepath = os.path.join(folder_path, filename)
        if os.path.isfile(filepath):
            with Image.open(filepath) as img:
                img_resized = img.resize(target_size)
                img_resized.save(filepath)
                print(f"Resized {filename} to {target_size}")

# Main function
if __name__ == "__main__":
    folder_path = "/home/anchidta/wk_law/image_1"
    
    # Task 1: Delete duplicate images
    delete_duplicates(folder_path)
    
    # Task 2: Rename images to numeric order
    rename_images(folder_path)
    
    # Task 3: Check minimum image size
    min_width, min_height = min_image_size(folder_path)
    print(f"Minimum image size: {min_width}x{min_height}")
    
    # Task 4: Resize images to minimum size
    min_size = (min_width, min_height)
    resize_images(folder_path, min_size)
