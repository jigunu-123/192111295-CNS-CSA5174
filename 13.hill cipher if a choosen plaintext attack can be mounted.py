import numpy as np
from sympy import Matrix

# Helper function to convert characters to numbers
def char_to_num(char):
    return ord(char) - ord('A')

# Helper function to convert numbers to characters
def num_to_char(num):
    return chr(num + ord('A'))

# Function to calculate the modular inverse of a matrix
def mod_inverse(matrix, modulo):
    det = int(Matrix(matrix).det())
    det_inverse = pow(det, -1, modulo)
    adjoint = np.array(Matrix(matrix).adjugate().tolist()) % modulo
    return (det_inverse * adjoint) % modulo

# Function to encrypt plaintext using the Hill cipher
def encrypt(plaintext, key):
    plaintext = plaintext.upper().replace(" ", "")
    n = len(key)
    padded_length = n - (len(plaintext) % n)
    plaintext += "X" * padded_length

    ciphertext = ""
    for i in range(0, len(plaintext), n):
        block = [char_to_num(char) for char in plaintext[i:i+n]]
        encrypted_block = np.dot(key, block) % 26
        ciphertext += "".join([num_to_char(num) for num in encrypted_block])

    return ciphertext

# Function to decrypt ciphertext using the Hill cipher
def decrypt(ciphertext, key):
    ciphertext = ciphertext.upper().replace(" ", "")
    n = len(key)

    plaintext = ""
    inverse_key = mod_inverse(key, 26)
    for i in range(0, len(ciphertext), n):
        block = [char_to_num(char) for char in ciphertext[i:i+n]]
        decrypted_block = np.dot(inverse_key, block) % 26
        plaintext += "".join([num_to_char(num) for num in decrypted_block])

    return plaintext

# Function to demonstrate the known-plaintext attack on the Hill cipher
def known_plaintext_attack(plaintext, ciphertext):
    plaintext = plaintext.upper().replace(" ", "")
    ciphertext = ciphertext.upper().replace(" ", "")

    if len(plaintext) != len(ciphertext):
        print("Plaintext and ciphertext lengths do not match.")
        return

    n = len(plaintext)
    known_pairs = []
    for i in range(0, n, 2):
        known_pairs.append((char_to_num(plaintext[i]), char_to_num(ciphertext[i])))

    # Construct the matrix equation: K * P = C
    matrix_K = []
    matrix_C = []
    for pair in known_pairs:
        matrix_K.append([pair[0], 1])
        matrix_C.append(pair[1])

    matrix_K = np.array(matrix_K)
    matrix_C = np.array(matrix_C)

    try:
        inverse_K = mod_inverse(matrix_K, 26)
        key = np.dot(inverse_K, matrix_C) % 26

        print("Recovered key:")
        print(key)

        decrypted_plaintext = decrypt(ciphertext, key)
        print("Decrypted plaintext:")
        print(decrypted_plaintext)

    except ValueError:
        print("Known-plaintext attack failed. The matrix K is not invertible.")
