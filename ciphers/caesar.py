def caesar_encrypt(text, shift):
    encrypted_text = []
    for char in text:
        if char.isalpha():
            shift_amount = 65 if char.isupper() else 97
            encrypted_text.append(chr((ord(char) + shift - shift_amount) % 26 + shift_amount))
        else:
            encrypted_text.append(char)
    return ''.join(encrypted_text)

def caesar_decrypt(text, shift):
    return caesar_encrypt(text, -shift)
