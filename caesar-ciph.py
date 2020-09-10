from dict import open_dict
import copy
import string

# given a ciphertext encoded with a caesar shift,
# decrypt and return the plaintext

# creates dictionary
dict = open_dict()

# reads ciphertext and converts to list
ciph = input()
split = list(ciph)

shifted_lst= []

# compute each caesar shift
for shift in range(26):
    text = copy.deepcopy(split)
    for i in range(len(split)):
        if text[i] >= 'a' and text[i] <= 'z':
            if ord(text[i])+shift > ord('z'):
                overflow = shift - (ord('z') - ord(text[i]))-1
                text[i] = chr(ord('a')+overflow)
            else:
                text[i] = chr(ord(text[i])+shift)
        if text[i] >= 'A' and text[i] <= 'Z':
            if ord(text[i])+shift > ord('Z'):
                overflow = shift - (ord('Z') - ord(text[i]))-1
                text[i] = chr(ord('A')+overflow)
            else:
                text[i] = chr(ord(text[i])+shift)
    shifted = ''.join(text)
    shifted_lst.append(shifted)

# calculate the number of real words contained in each caesar shift
max = -1
max_ind = -1
for i in range(len(shifted_lst)):
    words = shifted_lst[i].split(' ')
    count = 0
    for word in words:
        # prune any punctuation from the word
        word = word.translate(str.maketrans('', '', string.punctuation))
        if word in dict:
            count += 1
    if count > max:
        max = count
        max_ind = i

# prints the caesar shift that contained the most real words
print(shifted_lst[max_ind])
