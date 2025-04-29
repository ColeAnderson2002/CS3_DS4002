# Upload and unzip snake images
from google.colab import files
import zipfile
import os

# Upload data.zip
uploaded = files.upload()

# Unzip the uploaded file
with zipfile.ZipFile("snake_data.zip", 'r') as zip_ref:
    zip_ref.extractall("./snake_data")

# Check directory structure
for root, dirs, files in os.walk("./snake_data", topdown=True):
    print(root)
