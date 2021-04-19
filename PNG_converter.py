import os
from PIL import Image


# grabs arguments
image_folder = input("Enter image folder path: ")
new_folder = input("Enter new folder path: ")

# checks if path already exists and creates it if not
if not os.path.exists(new_folder):
    os.makedirs(new_folder)

# saves each image in image_folder as a png in new_folder
for filename in os.listdir(image_folder):
    img = Image.open(f"{image_folder}/{filename}")
    clean_name = os.path.splitext(filename)[0]  # converts to tuple: (filename[0], extension[1])
    img.save(f"{new_folder}/{clean_name}.png", "png")
    print(f"{clean_name} has been converted")
