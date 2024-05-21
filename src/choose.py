import os
import shutil
import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk

class ImageSelector:
    def __init__(self, root):
        self.root = root
        self.root.title("Image Selector")

        self.input_folder = ""
        self.output_folder = ""

        self.images = []
        self.selected_images = []

        self.current_image_index = 0

        self.create_widgets()

    def create_widgets(self):
        self.label = tk.Label(self.root, text="Select Input Folder:")
        self.label.pack()

        self.input_button = tk.Button(self.root, text="Browse", command=self.browse_input_folder)
        self.input_button.pack()

        self.prev_button = tk.Button(self.root, text="Previous", command=self.prev_image)
        self.prev_button.pack()

        self.next_button = tk.Button(self.root, text="Next", command=self.next_image)
        self.next_button.pack()

        self.save_button = tk.Button(self.root, text="Save", command=self.save_selected_images)
        self.save_button.pack()

        self.canvas = tk.Canvas(self.root)
        self.canvas.pack(expand=True, fill=tk.BOTH)

    def browse_input_folder(self):
        self.input_folder = filedialog.askdirectory()
        self.load_images()

    def load_images(self):
        self.images = []
        self.selected_images = []
        for filename in os.listdir(self.input_folder):
            if filename.endswith('.jpg'):
                image = Image.open(os.path.join(self.input_folder, filename))
                self.images.append(image)
        self.show_image()

    def show_image(self):
        if self.images:
            image = self.images[self.current_image_index]
            width, height = image.size
            aspect_ratio = width / height
            # Calculate the appropriate size for the window based on the image aspect ratio
            window_width = min(width, 800)
            window_height = int(window_width / aspect_ratio)
            self.root.geometry(f"{window_width}x{window_height}")
            # Resize the image to fit the window
            image = image.resize((window_width, window_height))
            self.current_image = ImageTk.PhotoImage(image)
            self.canvas.create_image(0, 0, anchor=tk.NW, image=self.current_image)

    def next_image(self):
        self.current_image_index = (self.current_image_index + 1) % len(self.images)
        self.show_image()

    def prev_image(self):
        self.current_image_index = (self.current_image_index - 1) % len(self.images)
        self.show_image()

    def save_selected_images(self):
        # Set the output folder here
        self.output_folder = "selected_images"
        if not os.path.exists(self.output_folder):
            os.makedirs(self.output_folder)

        if self.current_image_index < len(self.images):
            selected_image = self.images[self.current_image_index]
            filename = os.path.basename(os.path.normpath(self.input_folder)) + "_selected_" + str(self.current_image_index) + ".jpg"
            selected_image.save(os.path.join(self.output_folder, filename))
            self.selected_images.append(selected_image)

# Main
root = tk.Tk()
app = ImageSelector(root)
root.mainloop()
