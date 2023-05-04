def mod_inverse(a, m):
    for i in range(m):
        if (a * i) % m == 1:
            return i
    return None
def break_affine_cipher(ciphertext, freq1, freq2):
    freqs = {}
    for c in ciphertext:
        if c in freqs:
            freqs[c] += 1
        else:
            freqs[c] = 1
    sorted_freqs = sorted(freqs.items(), key=lambda x: x[1], reverse=True)
    most_frequent = sorted_freqs[0][0]
    second_most_frequent = sorted_freqs[1][0]
    a = (ord(most_frequent) - ord(second_most_frequent)) * mod_inverse(ord('B') - ord('U'), 26) % 26
    b = (ord(most_frequent) - ord('A') * a) % 26
    plaintext = ''
    for c in ciphertext:
        if c.isalpha():
            plaintext += chr((a * (ord(c) - ord('A') - b)) % 26 + ord('A'))
        else:
            plaintext += c
    return plaintext
ciphertext = input('enter the text=')
plaintext = break_affine_cipher(ciphertext, 'B', 'U')
print(plaintext)
   
