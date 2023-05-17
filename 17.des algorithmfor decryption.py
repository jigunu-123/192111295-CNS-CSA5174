import binascii

def permutate(original, permutation):
    permuted = ''
    for index in permutation:
        permuted += original[index - 1]
    return permuted

def generate_round_keys(key):
    pc1 = [57, 49, 41, 33, 25, 17, 9,
           1, 58, 50, 42, 34, 26, 18,
           10, 2, 59, 51, 43, 35, 27,
           19, 11, 3, 60, 52, 44, 36,
           63, 55, 47, 39, 31, 23, 15,
           7, 62, 54, 46, 38, 30, 22,
           14, 6, 61, 53, 45, 37, 29,
           21, 13, 5, 28, 20, 12, 4]

    pc2 = [14, 17, 11, 24, 1, 5,
           3, 28, 15, 6, 21, 10,
           23, 19, 12, 4, 26, 8,
           16, 7, 27, 20, 13, 2,
           41, 52, 31, 37, 47, 55,
           30, 40, 51, 45, 33, 48,
           44, 49, 39, 56, 34, 53,
           46, 42, 50, 36, 29, 32]

    shifts = [1, 1, 2, 2, 2, 2, 2, 2,
              1, 2, 2, 2, 2, 2, 2, 1]

    key = permutate(key, pc1)

    round_keys = []
    left = key[:28]
    right = key[28:]

    for shift in shifts:
        left = left[shift:] + left[:shift]
        right = right[shift:] + right[:shift]
        round_key = permutate(left + right, pc2)
        round_keys.append(round_key)

    round_keys.reverse()
    return round_keys

def expand_and_permutate(right_half):
    expansion_table = [32, 1, 2, 3, 4, 5,
                       4, 5, 6, 7, 8, 9,
                       8, 9, 10, 11, 12, 13,
                       12, 13, 14, 15, 16, 17,
                       16, 17, 18, 19, 20, 21,
                       20, 21, 22, 23, 24, 25,
                       24, 25, 26, 27, 28, 29,
                       28, 29, 30, 31, 32, 1]

    return permutate(right_half, expansion_table)

def substitute(s_input, s_boxes):
    output = ''
    for index in range(0, 48, 6):
        s_block = s_input[index:index + 6]
        row = int(s_block[0]
