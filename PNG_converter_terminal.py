import sys
import os
from PIL import Image


# grabs arguments
image_folder = sys.argv[1]
new_folder = sys.argv[2]

# checks if path already exists and creates it if not
if not os.path.exists(new_folder):
    os.makedirs(new_folder)
else:
    print(f"{new_folder} already exists")

# saves each image in image_folder as a png in new_folder
for filename in os.listdir(image_folder):
    img = Image.open(f"{image_folder}/{filename}")
    clean_name = os.path.splitext(filename)[0]  # converts to tuple: (filename[0], extension[1])
    img.save(f"{new_folder}/{clean_name}.png", "png")
    print(f"{clean_name} has been converted")
