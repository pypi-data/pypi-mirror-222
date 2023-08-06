class Cipher:

    def __init__(self, key, original_text):
        self.text = original_text
        self.key = 42

    def simple_xor_encrypt(self, text, key):
        encrypted_chars = []
        for char in text:
            encrypted_char = ord(char) ^ key
            encrypted_chars.append(encrypted_char)
        return bytes(encrypted_chars)

    def simple_xor_decrypt(self, encrypted_text, key):
        decrypted_chars = []
        for encrypted_char in encrypted_text:
            decrypted_char = chr(encrypted_char ^ key)
            decrypted_chars.append(decrypted_char)
        return "".join(decrypted_chars)

# Example usage:
key = 42
original_text = input("You: ")

cipher = Cipher(key, original_text)

encrypted_text = cipher.simple_xor_encrypt(original_text, key)
decrypted_text = cipher.simple_xor_decrypt(encrypted_text, key)

print("Encrypted text:", encrypted_text)
print("Decrypted text:", decrypted_text)
