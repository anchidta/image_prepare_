import os
from tkinter import *
from tkinter import filedialog
from tkinter.ttk import Combobox
from PIL import Image, ImageTk

class ImageBrowserApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Image Browser App")
        
        self.folder_path = None
        self.img_paths = []
        self.current_img_index = 0
        self.img_label = None
        self.selected_subfolder = StringVar()
        self.current_size_label = None
        self.prev_btn = None
        self.next_btn = None
        
        self.create_widgets()
    
    def create_widgets(self):
        # Button to select image folder
        select_folder_btn = Button(self.root, text="Select Image Folder", command=self.select_folder)
        select_folder_btn.pack(pady=10)
        
        # Frame to display image
        self.img_frame = Frame(self.root)
        self.img_frame.pack()
        
        # Button to navigate to previous image
        self.prev_btn = Button(self.root, text="Previous", command=self.prev_image, state=DISABLED)
        self.prev_btn.pack(side=LEFT, padx=5)
        
        # Button to navigate to next image
        self.next_btn = Button(self.root, text="Next", command=self.next_image, state=DISABLED)
        self.next_btn.pack(side=LEFT, padx=5)
        
        # Dropdown menu for selecting subfolder
        subfolder_options = ["back", "front", "license", "motorbike", "with human", "none"]
        self.subfolder_combo = Combobox(self.root, values=subfolder_options, textvariable=self.selected_subfolder)
        self.subfolder_combo.pack(pady=5)
        self.subfolder_combo.current(0)  # Set default value to "back"
        
        # Button to add selected image to data folder
        self.add_to_data_btn = Button(self.root, text="Add to Data", command=self.add_to_data, state=DISABLED)
        self.add_to_data_btn.pack(pady=5)
        
        # Entry for resizing image
        self.resize_entry = Entry(self.root)
        self.resize_entry.pack(pady=5)
        self.resize_entry.insert(0, "Enter size (e.g., 100x100)")
        
        # Button to resize image
        resize_btn = Button(self.root, text="Resize Image", command=self.resize_image, state=DISABLED)
        resize_btn.pack(pady=5)
        
        # Button to save resized image
        self.save_btn = Button(self.root, text="Save Resized Image", command=self.save_resized_image, state=DISABLED)
        self.save_btn.pack(pady=5)
        
        # Label to display current image size
        self.current_size_label = Label(self.root, text="Current Size: ")
        self.current_size_label.pack(pady=5)
    
    def select_folder(self):
        self.folder_path = filedialog.askdirectory()
        self.load_images()
    
    def load_images(self):
        self.img_paths = [os.path.join(self.folder_path, f) for f in os.listdir(self.folder_path) if f.endswith(('.jpg', '.jpeg', '.png'))]
        
        if self.img_paths:
            self.show_image(0)
        else:
            print("No images found in the selected folder.")
    
    def show_image(self, index):
        img_path = self.img_paths[index]
        img = Image.open(img_path)
        img.thumbnail((400, 400))  # Adjust thumbnail size as needed
        img = ImageTk.PhotoImage(img)
        
        if self.img_label:
            self.img_label.destroy()
        
        self.img_label = Label(self.img_frame, image=img)
        self.img_label.image = img
        self.img_label.pack()
        
        self.current_img_index = index
        self.update_navigation_buttons()
        self.show_image_size(img_path)
    
    def update_navigation_buttons(self):
        num_images = len(self.img_paths)
        
        if num_images > 1:
            if self.current_img_index == 0:
                self.prev_btn.config(state=DISABLED)
            else:
                self.prev_btn.config(state=NORMAL)
            
            if self.current_img_index == num_images - 1:
                self.next_btn.config(state=DISABLED)
            else:
                self.next_btn.config(state=NORMAL)
        else:
            self.prev_btn.config(state=DISABLED)
            self.next_btn.config(state=DISABLED)
        
        self.add_to_data_btn.config(state=NORMAL)
        self.resize_entry.config(state=NORMAL)
        self.save_btn.config(state=DISABLED)
        self.subfolder_combo.config(state=NORMAL)
    
    def prev_image(self):
        if self.current_img_index > 0:
            self.show_image(self.current_img_index - 1)
    
    def next_image(self):
        if self.current_img_index < len(self.img_paths) - 1:
            self.show_image(self.current_img_index + 1)
    
    def add_to_data(self):
        selected_img = self.img_paths[self.current_img_index]
        subfolder = self.selected_subfolder.get()
        data_folder = "/home/anchidta/wk_law/image_1"  # Replace with your data folder path
        destination = os.path.join(data_folder, subfolder, os.path.basename(selected_img))
        os.rename(selected_img, destination)
        self.load_images()  # Refresh images after moving
    
    def resize_image(self):
        size_input = self.resize_entry.get()
        try:
            width, height = map(int, size_input.split('x'))
            img_path = self.img_paths[self.current_img_index]
            img = Image.open(img_path)
            resized_img = img.resize((width, height))
            resized_img.thumbnail((400, 400))  # Thumbnail for display purposes
            resized_img = ImageTk.PhotoImage(resized_img)
            
            # Display resized image
            if self.img_label:
                self.img_label.destroy()
            self.img_label = Label(self.img_frame, image=resized_img)
            self.img_label.image = resized_img
            self.img_label.pack()
            
            # Update buttons
            self.save_btn.config(state=NORMAL)
            self.add_to_data_btn.config(state=NORMAL)
        except ValueError:
            print("Invalid size format. Please enter size in format 'widthxheight' (e.g., 100x100)")


    
    def save_resized_image(self):
        if self.img_label:
            # Get the resized image from the label
            img = self.img_label.image
            if img:
                # Ask for the directory to save the resized image
                save_folder = filedialog.askdirectory()
                if save_folder:
                    # Save the resized image
                    img_path = self.img_paths[self.current_img_index]
                    img_name = os.path.basename(img_path)
                    save_path = os.path.join(save_folder, img_name)
                    img.write(save_path)
                    print("Resized image saved successfully.")
                else:
                    print("No folder selected to save the resized image.")
            else:
                print("No resized image to save.")
        else:
            print("No image to save.")

    
    def show_image_size(self, img_path):
        img = Image.open(img_path)
        width, height = img.size
        self.current_size_label.config(text=f"Current Size: {width}x{height}")

if __name__ == "__main__":
    root = Tk()
    app = ImageBrowserApp(root)
    root.mainloop()
