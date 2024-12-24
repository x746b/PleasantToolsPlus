import sys
import base64
from Crypto.Cipher import AES
from Crypto.Protocol.KDF import PBKDF2
import binascii

def decrypt_to_bytes(key, data):
    try:
        # Split salt and data
        salt = data[:8]
        data_no_salt = data[8:]

        # Derive key and IV using PBKDF2
        key_iv = PBKDF2(key, salt, dkLen=48, count=1000)
        aes_key = key_iv[:32]
        aes_iv = key_iv[32:]

        # Decrypt data
        cipher = AES.new(aes_key, AES.MODE_CBC, aes_iv)
        decrypted_data = cipher.decrypt(data_no_salt)
        return decrypted_data.rstrip(b"\x00")
    except Exception as e:
        print(f"Error during decryption: {e}")
        return None

def decrypt_to_string(key, data):
    decrypted_bytes = decrypt_to_bytes(key, data)
    if decrypted_bytes is None:
        return None
    return decrypted_bytes.decode("utf-8")

def string_to_byte_array(hex_string):
    return binascii.unhexlify(hex_string)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python decrypt.py username encrypted_password")
        sys.exit(1)

    username = sys.argv[1]
    encrypted_password_hex = sys.argv[2]

    # Fixed decryption key from the C# code
    decryption_key = "36AB08A4-422E-4e63-916F-C356691C08F3"

    try:
        encrypted_password_bytes = string_to_byte_array(encrypted_password_hex[2:])  # Remove the 0x prefix
        decrypted_password = decrypt_to_string(decryption_key, encrypted_password_bytes)

        if decrypted_password is not None:
            print(f"Decrypted credentials for {username}: {decrypted_password}")
        else:
            print(f"Failed to decrypt credentials for {username}")

    except Exception as e:
        print(f"Error: {e}")
