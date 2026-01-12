🔐 Task-02: Pixel Manipulation for Image Encryption
I Project Overview

This project is developed as part of the Prodigy InfoTech Cyber Security Internship (Task-02).
The main goal of this task is to understand how images can be encrypted using pixel manipulation techniques and how the same image can be restored using the correct key.

In addition to basic image encryption, this project also demonstrates:
1.Password-based encryption
2.Hiding a secret message inside an image
3.Secure decryption using the same password

The implementation is kept simple and beginner-friendly while still reflecting a real-world security concept.

II How the Project Works

An image is made up of thousands of pixels, and each pixel contains RGB (Red, Green, Blue) values.
In this project:
1.The user provides a password, which is converted into a numeric key.
2.A secret message is hidden inside the image by modifying pixel values.
3.The image is encrypted by:
  3.1 Swapping RGB values
  3.2 Applying a mathematical operation using the generated key
4.During decryption, the process is reversed using the same password, and:
  4.1 The original image is restored
  4.2 The hidden message is extracted successfully

This ensures that without the correct password, the image remains unreadable.

III Technologies Used

1.Python 3
2.Pillow (PIL) library for image processing
3.VS Code for development

IV How to Run the Project

1.Make sure Python is installed on your system.
2.Install the required library:
pip install pillow
3.Place an input image (e.g., nature.png) inside the project folder.
4.Run the program:
python pixel.py
5.Choose:
  5.1 E to encrypt the image
  5.2 D to decrypt the image

Enter the password and other required inputs when prompted.

V Output Files

After successful execution, the following files are generated:

1. encrypted_image.png → The encrypted version of the original image (appears distorted)
2. decrypted_image.png → The original image restored after decryption

The secret message entered during encryption is also displayed during the decryption process.

VI Security Concepts Demonstrated

1.Image encryption using pixel manipulation
2.Password-based key generation
3.Data confidentiality
4.Basic steganography (hidden message inside image)
5.Reversible encryption and decryption

VII Sample Use Case

1.This type of technique can be applied in:
2.Secure image sharing
3.Digital watermarking
4.Privacy protection
5.Educational demonstrations of cryptography concepts

VIII Internship Task Details

1.Internship: Prodigy InfoTech – Cyber Security
2.Task Number: Task-02
3.Task Name: Pixel Manipulation for Image Encryption

IX Conclusion

This project successfully demonstrates how image encryption can be implemented using simple pixel operations and password-based security.
It provides a practical understanding of how visual data can be protected from unauthorized access using basic cryptographic principles.
