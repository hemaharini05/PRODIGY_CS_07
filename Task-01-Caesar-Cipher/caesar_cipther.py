def caesar_cipher(input_text, shift_value, operation_mode):
    # This will store the final encrypted/decrypted message
    final_text = ""

    # Process each character one by one
    for current_char in input_text:
        if current_char.isalpha():
            # Decide base value depending on uppercase or lowercase
            base_value = ord('A') if current_char.isupper() else ord('a')

            if operation_mode == "encrypt":
                shifted_char = chr(
                    (ord(current_char) - base_value + shift_value) % 26 + base_value
                )
            elif operation_mode == "decrypt":
                shifted_char = chr(
                    (ord(current_char) - base_value - shift_value) % 26 + base_value
                )

            final_text += shifted_char
        else:
            # Non-alphabetic characters are kept as they are
            final_text += current_char

    return final_text
def bruteforce_decrypt(cipher_text):
    print("\n--- Brute Force Decryption ---")
    # Try all possible shift values to show how weak the cipher is
    for possible_shift in range(1, 26):
        decrypted_text = caesar_cipher(cipher_text, possible_shift, "decrypt")
        print(f"Shift {possible_shift}: {decrypted_text}")
def get_valid_shift():
    # Keep asking until a valid shift value is entered
    while True:
        try:
            shift_input = int(input("Enter shift value (between 0 and 25): "))
            if 0 <= shift_input <= 25:
                return shift_input
            else:
                print("Please enter a number only between 0 and 25.")
        except ValueError:
            print("Invalid input! Numbers only are allowed.")
def main():
    print("=== Caesar Cipher Program ===")

    user_message = input("Enter your message: ")
    if not user_message.strip():
        print("Message cannot be empty!")
        return
    print("\nChoose an option:")
    print("E - Encrypt the message")
    print("D - Decrypt the message")
    print("B - Brute Force Decrypt")
    user_choice = input("Enter your choice: ").upper()

    if user_choice == 'E':
        shift_value = get_valid_shift()
        encrypted_message = caesar_cipher(user_message, shift_value, "encrypt")
        print("Encrypted Message:", encrypted_message)

    elif user_choice == 'D':
        shift_value = get_valid_shift()
        decrypted_message = caesar_cipher(user_message, shift_value, "decrypt")
        print("Decrypted Message:", decrypted_message)

    elif user_choice == 'B':
        bruteforce_decrypt(user_message)

    else:
        print("Invalid choice! Please select E, D, or B.")


if __name__ == "__main__":
    main()
