# Simple_ransomware_python

This Python code searches for a file with a specific extension (".caf") in a specified root directory and its subdirectories, and then performs the following tasks:

Generates a random encryption key using the Fernet class from the cryptography module.
Reads the contents of the found file and encrypts them using the generated key.
Writes the encrypted contents to a new file.
Writes the encryption key to a file.
Sends the key file to a server via a POST request to an IP address.
Checks the server's response to see if the key was uploaded successfully.
The code begins by importing the necessary modules. The os module is used for interacting with the operating system, and the requests and cryptography modules are used for sending HTTP requests and encrypting data, respectively.

Next, the script sets the file extension to search for (".caf") and the root directory to start the search ("/home/pouria/Downloads/"). The variable file_path is initialized to "FILE_NOT_FOUND".

The code then uses the os.walk() function to recursively loop through all the directories in the root directory and its subdirectories. For each file found, the code checks if it has the desired file extension. If so, the path to the file is printed and the file_path variable is set to the path of the found file.

If no file with the desired file extension is found, the script prints "File not found!" and exits.

If a file with the desired file extension is found, the code generates a random encryption key using the Fernet.generate_key() function from the cryptography module. It then initializes the Fernet class with the generated key.

The code then reads the contents of the found file using the open() function, and encrypts the contents using the Fernet.encrypt() method. The encrypted contents are then written to a new file with the path "./encrypted_file".

The encryption key is also written to a file with the path "./key".

The code then sends the key file to a server at IP address 188.40.23.247 using a POST request via the requests.post() function. The key file is attached to the request as a file using the files parameter.

Finally, the script checks the server's response to see if the key was uploaded successfully. If the response status code is 200, the script prints "Key uploaded successfully". Otherwise, it prints "Failed to upload key".
