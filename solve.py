import enchant

# Function to decrypt the Caesar cipher with a given shift
def decrypt_caesar_cipher(ciphertext, shift):
    decrypted_text = ""
    for char in ciphertext:
        if char.isalpha():
            shift_amount = ord('A') if char.isupper() else ord('a')
            decrypted_text += chr((ord(char) - shift_amount - shift) % 26 + shift_amount)
        else:
            decrypted_text += char
    return decrypted_text

# Function to check if the decrypted text is a valid English phrase
def is_english(text):
    dictionary = enchant.Dict("en_US")
    words = text.split()
    return all(dictionary.check(word) for word in words)

# Function to crack the Caesar cipher
def crack_caesar_cipher(ciphertext):
    for shift in range(26):
        decrypted_text = decrypt_caesar_cipher(ciphertext, shift)
        if is_english(decrypted_text):
            return f"Shift {shift}: {decrypted_text}"
    return "No valid English text found."

ciphertext = "JAEPDAN YKQLHA CECCHA ZEOYKRAN"
result = crack_caesar_cipher(ciphertext)
print(result)
