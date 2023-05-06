import math

# Define a function to count possible Playfair keys
def count_keys():
    count = 0
    for i in range(25):
        for j in range(i+1, 25):
            if i != 9 and j != 9: # Skip 'J'
                count += 1
    return count

# Calculate the number of possible keys
keys = count_keys()
print("Possible keys in the Playfair cipher: ", keys)
print("Approximate power of 2: ", math.log(keys, 2))

# Define a function to count effectively unique Playfair keys
def count_unique_keys():
    count = 0
    used_keys = set()
    for i in range(25):
        for j in range(i+1, 25):
            if i != 9 and j != 9: # Skip 'J'
                key = (i,j) if i < j else (j,i)
                if key not in used_keys:
                    used_keys.add(key)
                    count += 1
    return count

# Calculate the number of effectively unique keys
unique_keys = count_unique_keys()
print("Effectively unique keys in the Playfair cipher: ", unique_keys)
print("Approximate power of 2: ", math.log(unique_keys, 2))
