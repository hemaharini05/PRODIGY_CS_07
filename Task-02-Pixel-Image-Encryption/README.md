Task-02: Pixel Manipulation for Image Encryption
I Project Overview

This project demonstrates a simple image encryption and decryption technique using pixel manipulation in Python. The main objective of the project is to understand how image data can be protected using basic cryptographic and steganography concepts.

The program hides a secret text message inside an image by modifying the least significant bits of pixel values. During decryption, the program validates the password and message length before revealing the hidden message.

II Technologies Used:

1.Python
2.Pillow (PIL) library
3.Basic Cryptography Concepts
4.Image Processing

III Project Features:

1.Encrypts an image by hiding a secret message inside pixel data
2.Uses a password for authentication
3.Stores and validates message length during decryption
4.Displays clear error messages for:
   4.1 Wrong password
   4.2 Wrong message length
5.Prevents message extraction if authentication fails

IV How the Project Works:
  IV.1 Encryption Process:
1.The user selects encryption mode.
2.The user provides:
  2.1 A password
  2.2 A secret message
3.The program:
  3.1 Generates a secure hash of the password
  3.2 Calculates the message length
  3.3 Combines password hash, message length, and message
  3.4 Converts the data into binary
  3.5 Embeds the binary data into image pixels using least significant bit manipulation
4.The encrypted image is saved as encrypted.png.

   IV.2 Decryption Process

1.The user selects decryption mode.
2.The program extracts hidden binary data from the image.
3.The user is asked to enter the password:
  3.1 If the password is incorrect, decryption stops.
4.If the password is correct, the user is asked to enter the message length:
  4.1 If the length is incorrect, the message is not revealed.
5.If both password and message length are correct, the secret message is displayed.

V Folder Structure
Task-02-Pixel-Encryption/
│
├── README.md
├── pixel.py
├── nature.png
├── encrypted.png

VI How to Run the Project
Step 1: Install Required Package
pip install pillow

Step 2: Run the Program
python pixel.py

Step 3: Follow On-Screen Instructions

Choose Encrypt (E) or Decrypt (D)

Enter password and message when prompted

VII Sample Output:
1. Encryption
Enter E to Encrypt or D to Decrypt: E
Create password: hema123
Enter secret message: hai
Image encrypted successfully

 Decryption (Wrong Password)
Wrong password

Decryption (Wrong Message Length)
Password correct
Wrong message length

Decryption (Successful)
Password correct
Secret Message: hai

VIII Learning Outcome:

Through this project, I gained practical experience in:

1.Image processing using Python
2.Pixel-level data manipulation
3.Basic steganography techniques
4.Password validation using hashing
5.Error handling and input validation

This task helped me understand how cryptography concepts can be applied to protect multimedia data.

Author

Hema Harini
Cyber Security Intern
Prodigy InfoTech
