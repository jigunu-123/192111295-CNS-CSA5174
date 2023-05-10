import random
def generate_key(length):
    key = []
    for i in range(length):
        key.append(random.randint(0, 26))
    return key
def encrypt(plaintext, key):
    ciphertext = ""
    key_index = 0
    for c in plaintext:
        if c.isalpha():
            shift = key[key_index]
            if c.isupper():
                ciphertext += chr((ord(c) - 65 + shift) % 26 + 65)
            else:
                ciphertext += chr((ord(c) - 97 + shift) % 26 + 97)
            key_index = (key_index + 1) % len(key)
        else:
            ciphertext += c
    return ciphertext
def decrypt(ciphertext, key):
    plaintext = ""
    key_index = 0
    for c in ciphertext:
        if c.isalpha():
            shift = key[key_index]
            if c.isupper():
                plaintext += chr((ord(c) - 65 - shift) % 26 + 65)
            else:
                plaintext += chr((ord(c) - 97 - shift) % 26 + 97)
            key_index = (key_index + 1) % len(key)
        else:
            plaintext += c
    return plaintext
plaintext = "This is a secret message."
key = generate_key(len(plaintext))
ciphertext = encrypt(plaintext, key)
decrypted_text = decrypt(ciphertext, key)
print("Plaintext:  ", plaintext)
print("Ciphertext: ", ciphertext)
print("Decrypted:  ", decrypted_text)
