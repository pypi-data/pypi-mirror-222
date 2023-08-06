from main import *

key = 42069
original_text = input("You: ")

cipher = Cipher(key)

encrypted_text = cipher.simple_xor_encrypt(original_text)
decrypted_text = cipher.simple_xor_decrypt(encrypted_text)

print("Encrypted text:", encrypted_text)
print("Decrypted text:", decrypted_text)
