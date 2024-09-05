import string

def create_playfair_square(key):
    alphabet = string.ascii_uppercase.replace('J', '')
    key = ''.join(sorted(set(key.upper()), key=key.index))  # remove duplicates while preserving order
    matrix = [char for char in key if char in alphabet] + [char for char in alphabet if char not in key]
    
    return [matrix[i:i+5] for i in range(0, 25, 5)]

def playfair_encrypt_decrypt(text, key, decrypt=False):
    square = create_playfair_square(key)
    text = text.upper().replace('J', 'I')
    processed_text = []
    
    i = 0
    while i < len(text):
        if i + 1 < len(text) and text[i] == text[i + 1]:
            processed_text.append(text[i] + 'X')
            i += 1
        else:
            processed_text.append(text[i:i+2])
            i += 2
    
    if len(processed_text[-1]) == 1:
        processed_text[-1] += 'X'
    
    def get_position(letter):
        for row in square:
            if letter in row:
                return (square.index(row), row.index(letter))
    
    def same_row(row, col1, col2):
        if not decrypt:
            return square[row][(col1 + 1) % 5] + square[row][(col2 + 1) % 5]
        else:
            return square[row][(col1 - 1) % 5] + square[row][(col2 - 1) % 5]
    
    def same_column(col, row1, row2):
        if not decrypt:
            return square[(row1 + 1) % 5][col] + square[(row2 + 1) % 5][col]
        else:
            return square[(row1 - 1) % 5][col] + square[(row2 - 1) % 5][col]
    
    def rectangle(row1, col1, row2, col2):
        return square[row1][col2] + square[row2][col1]
    
    result = []
    for digraph in processed_text:
        row1, col1 = get_position(digraph[0])
        row2, col2 = get_position(digraph[1])
        
        if row1 == row2:
            result.append(same_row(row1, col1, col2))
        elif col1 == col2:
            result.append(same_column(col1, row1, row2))
        else:
            result.append(rectangle(row1, col1, row2, col2))
    
    return ''.join(result)

def playfair_encrypt(text, key):
    return playfair_encrypt_decrypt(text, key, decrypt=False)

def playfair_decrypt(text, key):
    return playfair_encrypt_decrypt(text, key, decrypt=True)
