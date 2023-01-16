def encrypt(text):
    cipher_text = ""
    key = 5

    for ch in text:
        ascii_code = ord(ch)
        if 32 <= ascii_code <= 47 or 58 <= ascii_code <= 64 or 91 <= ascii_code <= 96 or 123 <= ascii_code <= 126:
            cipher_text += ch
        if ch.islower():
            cipher_text += chr((ascii_code - 97 + key) % 26 + 97)
        elif ch.isupper():
            cipher_text += chr((ascii_code - 65 + key) % 26 + 65)

    return cipher_text, key


def dec(cipher_text, key):
    text = ""
    for ch in cipher_text:
        ascii_code = ord(ch)
        if 32 <= ascii_code <= 47 or 58 <= ascii_code <= 64 or 91 <= ascii_code <= 96 or 123 <= ascii_code <= 126:
            text += ch
        if ch.islower():
            text += chr((ascii_code - 97 - key) % 26 + 97)
        elif ch.isupper():
            text += chr((ascii_code - 65 - key) % 26 + 65)

    return text


def decrypt(text):
    cipher_text = encrypt(text)[0]
    key = encrypt(text)[1]

    decrypt_text = dec(cipher_text, key)

    print("Decrypt text: ", decrypt_text)


def break_cipher():
    cipher_text = "Mjqqt. Rd sfrj nx Qfzwf!"

    for i in range(26):
        key = i + 1
        text = dec(cipher_text, key)

        print(f"key = {key}, text = {text}")


with open("caesar_cipher_text.txt", "r") as file:
    content = file.read()

print("Input text:", content)
encrypt_text = encrypt(content)[0]
print("Encrypt text: ", encrypt_text)

decrypt(content)

print("\nBreak Caesar Cipher")
break_cipher()
