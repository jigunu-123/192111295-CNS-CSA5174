import string

def generate_cipher(keyword):
    # Generate the cipher sequence from the keyword
    keyword = keyword.upper()
    unused_letters = ''.join([char for char in string.ascii_uppercase if char not in keyword])
    cipher_sequence = keyword + unused_letters
    return cipher_sequence

def encrypt(message, cipher_sequence):
    # Encrypt the message using the given cipher sequence
    message = message.upper()
    ciphertext = ''
    for char in message:
        if char in string.ascii_uppercase:
            index = string.ascii_uppercase.index(char)
            ciphertext += cipher_sequence[index]
        else:
            ciphertext += char
    return ciphertext

def decrypt(ciphertext, cipher_sequence):
    # Decrypt the ciphertext using the given cipher sequence
    plaintext = ''
    for char in ciphertext:
        if char in string.ascii_uppercase:
            index = cipher_sequence.index(char)
            plaintext += string.ascii_uppercase[index]
        else:
            plaintext += char
    return plaintext

# Example usage
keyword = 'CIPHER'
cipher_sequence = generate_cipher(keyword)
print(f"Cipher sequence: {cipher_sequence}")

message = 'This is a secret message.'
ciphertext = encrypt(message, cipher_sequence)
print(f"Ciphertext: {ciphertext}")

decrypted_message = decrypt(ciphertext, cipher_sequence)
print(f"Decrypted message: {decrypted_message}")

