import os
import shutil
from PIL import Image

# Directory containing the images
directory = "img"
original_directory = os.path.join(directory, "original")

# Create 'original' directory if it doesn't exist
if not os.path.exists(original_directory):
    os.makedirs(original_directory)

# Desired size of the icons
desired_size = (200, 48)

# Move original files to 'original' directory and resize them
for filename in os.listdir(directory):
    if filename.endswith(".png") and filename.startswith("tab_"):
        # Construct full path to the file
        filepath = os.path.join(directory, filename)

        # Move the original file to 'original' directory
        shutil.move(filepath, os.path.join(original_directory, filename))

        # Open the original image
        image = Image.open(os.path.join(original_directory, filename))

        # Resize the image
        resized_image = image.resize(desired_size, Image.LANCZOS)

        # Save the resized image with the original filename
        resized_image.save(filepath)

