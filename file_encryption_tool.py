from cryptography.fernet import Fernet
import base64
import os

def generate_key():
    return Fernet.generate_key()

def encrypt_message(message, key):
    try:
        fernet = Fernet(key)
        ciphertext = fernet.encrypt(message.encode())
        return ciphertext
    except Exception as e:
        print("Error during encryption:", e)
        return None

def decrypt_message(ciphertext, key):
    try:
        fernet = Fernet(key)
        plaintext = fernet.decrypt(ciphertext).decode()
        return plaintext
    except Exception as e:
        print("Error during decryption:", e)
        return None

def save_to_file(data, filename):
    try:
        with open(filename, 'wb') as file:
            file.write(data)
        print(f"Data saved to {filename}")
    except Exception as e:
        print("Error saving to file:", e)

def save_key_to_file(key, filename):
    try:
        with open(filename, 'wb') as file:
            file.write(key)
        print(f"Key saved to {filename}")
    except Exception as e:
        print("Error saving key to file:", e)

def main():
    key_filename = "encryption_key.key"
    if not os.path.isfile(key_filename):
        key = generate_key()
        save_key_to_file(key, key_filename)
        print("Your encryption key has been generated and saved to 'encryption_key.key'.")
    else:
        with open(key_filename, 'rb') as file:
            key = file.read()
        print("Your encryption key has been loaded from 'encryption_key.key'.")

    operation = input("Choose operation (encrypt/decrypt): ").lower()

    if operation == 'encrypt':
        message = input("Enter the message you want to encrypt: ")
        ciphertext = encrypt_message(message, key)
        if ciphertext:
            filename = "encrypted_data.bin"  # Default filename
            save_to_file(ciphertext, filename)
            print("Message encrypted and saved successfully.")
    elif operation == 'decrypt':
        filename = input("Enter the filename of the encrypted data: ")
        try:
            with open(filename, 'rb') as file:
                ciphertext = file.read()
            plaintext = decrypt_message(ciphertext, key)
            if plaintext:
                print("Message decrypted successfully.")
                print("Plaintext:", plaintext)
        except FileNotFoundError:
            print("File not found.")
    else:
        print("Invalid operation. Choose 'encrypt' or 'decrypt'.")

if __name__ == "__main__":
    main()
