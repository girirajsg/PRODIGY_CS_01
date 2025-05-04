def encrypt(text, shift):
    result = ""

    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base + shift) % 26 + base)
        else:
            result += char
    return result

def decrypt(text, shift):
    return encrypt(text, -shift)

def main():
    print("Caesar Cipher Program")
    choice = input("Type 'encrypt' or 'decrypt': ").lower()

    message = input("Enter your message: ")
    shift = int(input("Enter shift value (e.g., 3): "))

    if choice == 'encrypt':
        encrypted = encrypt(message, shift)
        print(f"Encrypted Message: {encrypted}")
    elif choice == 'decrypt':
        decrypted = decrypt(message, shift)
        print(f"Decrypted Message: {decrypted}")
    else:
        print("Invalid choice. Please type 'encrypt' or 'decrypt'.")

if __name__ == "__main__":
    main()
