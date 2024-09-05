def vigenere_encrypt(text, keyword):
    encrypted_text = []
    keyword = keyword.upper()
    keyword_repeated = (keyword * (len(text) // len(keyword))) + keyword[:len(text) % len(keyword)]
    
    for i, char in enumerate(text):
        if char.isalpha():
            shift = ord(keyword_repeated[i]) - 65
            shift_amount = 65 if char.isupper() else 97
            encrypted_text.append(chr((ord(char) + shift - shift_amount) % 26 + shift_amount))
        else:
            encrypted_text.append(char)
    return ''.join(encrypted_text)

def vigenere_decrypt(text, keyword):
    decrypted_text = []
    keyword = keyword.upper()
    keyword_repeated = (keyword * (len(text) // len(keyword))) + keyword[:len(text) % len(keyword)]
    
    for i, char in enumerate(text):
        if char.isalpha():
            shift = 26 - (ord(keyword_repeated[i]) - 65)
            shift_amount = 65 if char.isupper() else 97
            decrypted_text.append(chr((ord(char) + shift - shift_amount) % 26 + shift_amount))
        else:
            decrypted_text.append(char)
    return ''.join(decrypted_text)
