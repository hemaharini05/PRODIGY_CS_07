from PIL import Image

def generate_key(password):
    return sum(ord(char) for char in password) % 256


def hide_message(pixels, message):
    for i, char in enumerate(message):
        r, g, b = pixels[i, 0]
        pixels[i, 0] = (ord(char), g, b)


def extract_message(pixels, length):
    message = ""
    for i in range(length):
        r, g, b = pixels[i, 0]
        message += chr(r)
    return message


def encrypt_image(image_path, password, message):
    key = generate_key(password)
    img = Image.open(image_path).convert("RGB")
    pixels = img.load()

    hide_message(pixels, message)

    for i in range(img.width):
        for j in range(img.height):
            r, g, b = pixels[i, j]
            pixels[i, j] = (g + key) % 256, (b + key) % 256, (r + key) % 256

    img.save("encrypted_image.png")
    print("✅ Image encrypted and message hidden successfully")


def decrypt_image(image_path, password, message_length):
    key = generate_key(password)
    img = Image.open(image_path).convert("RGB")
    pixels = img.load()

    for i in range(img.width):
        for j in range(img.height):
            r, g, b = pixels[i, j]
            pixels[i, j] = (b - key) % 256, (r - key) % 256, (g - key) % 256

    message = extract_message(pixels, message_length)
    img.save("decrypted_image.png")

    print("🔓 Decrypted Message:", message)
    print("✅ Image decrypted successfully")


choice = input("Enter E to Encrypt or D to Decrypt: ")
password = input("Enter password: ")

if choice.upper() == 'E':
    message = input("Enter secret message: ")
    encrypt_image("nature.png", password, message)

elif choice.upper() == 'D':
    length = int(input("Enter message length: "))
    decrypt_image("encrypted_image.png", password, length)

else:
    print("❌ Invalid choice")
