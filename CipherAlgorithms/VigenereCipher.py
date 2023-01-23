def generate_key(text, word):
    key = ""
    k = 0

    while len(key) != len(text):
        if k == len(word):
            k = 0
        key += word[k]
        k += 1

    return key


def encrypt_with_vigenere_table(text, key):
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
                'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    vigenere_table = list()

    for shift in range(len(alphabet)):
        temp = list()
        for i in range(shift, len(alphabet)):
            temp.append(alphabet[i])
        for j in range(0, shift):
            temp.append(alphabet[j])

        vigenere_table.append(temp)

    #for i in range(len(vigenere_table)):
        #print(vigenere_table[i])

    text = text.lower()
    cipher_text = ""

    for i in range(len(text)):
        index1 = ord(text[i]) - 97
        index2 = ord(key[i]) - 97
        cipher_text += vigenere_table[index1][index2]

    return cipher_text


def encrypt(text, key):
    cipher_text = ""

    for i in range(len(text)):
        if 32 <= ord(text[i]) <= 47 or 58 <= ord(text[i]) <= 64 or 91 <= ord(text[i]) <= 96 or 123 <= ord(text[i]) <= 126:
            cipher_text += text[i]
        elif text[i].islower():
            index1 = ord(text[i]) - 97
            index2 = ord(key[i]) - 97
            cipher_text += chr((index1 + index2) % 26 + 97)
        elif text[i].isupper():
            index1 = ord(text[i]) - 65
            index2 = ord(key[i]) - 65
            cipher_text += chr((index1 + index2) % 26 + 65)

    return cipher_text


def decrypt(cipher, key):
    text = ""
    for i in range(len(cipher)):
        if 32 <= ord(cipher[i]) <= 47 or 58 <= ord(cipher[i]) <= 64 or 91 <= ord(cipher[i]) <= 96 or 123 <= ord(
                cipher[i]) <= 126:
            text += cipher[i]
        elif cipher[i].islower():
            index1 = ord(cipher[i]) - 97
            index2 = ord(key[i]) - 97
            text += chr((index1 - index2) % 26 + 97)
        elif cipher[i].isupper():
            index1 = ord(cipher[i]) - 65
            index2 = ord(key[i]) - 65
            text += chr((index1 - index2) % 26 + 65)

    return text


input_text = "Hello, World."
print("input text: ", input_text)
key_word = "lemon"
cipher_key = generate_key(input_text, key_word)
print("key: ", cipher_key)

#encrypt_text = encrypt_with_vigenere_table(input_text, generate_key(input_text, key_word))
encrypt_text = encrypt(input_text, cipher_key)
print("Cipher text: ", encrypt_text)

print("Decrypt text: ", decrypt(encrypt_text, cipher_key))
