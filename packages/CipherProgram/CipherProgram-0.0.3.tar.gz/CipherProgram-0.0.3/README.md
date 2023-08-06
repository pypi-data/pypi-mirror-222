# Simple Cipher Program

This program encrypts any input text into machine code. That's it lol

To use it...

```
from Cipher import *

key = 42
original_text = input("You: ")

cipher = Cipher(key, original_text)

encrypted_text = cipher.simple_xor_encrypt(original_text, key)
decrypted_text = cipher.simple_xor_decrypt(encrypted_text, key)

print("Encrypted text:", encrypted_text)
print("Decrypted text:", decrypted_text)
```
