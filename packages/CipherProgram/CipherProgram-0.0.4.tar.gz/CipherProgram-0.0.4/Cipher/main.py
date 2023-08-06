class Cipher:

    def __init__(self, key):
        self.key = 42

    def simple_xor_encrypt(self, text):
        encrypted_chars = []
        for char in text:
            encrypted_char = ord(char) ^ self.key
            encrypted_chars.append(encrypted_char)
        return bytes(encrypted_chars)

    def simple_xor_decrypt(self, encrypted_text):
        decrypted_chars = []
        for encrypted_char in encrypted_text:
            decrypted_char = chr(encrypted_char ^ self.key)
            decrypted_chars.append(decrypted_char)
        return "".join(decrypted_chars)
