def alphabet_position(letter):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    letter = letter.lower()
    return alphabet.index(letter)
    #if letter in 




def rotate_character(char, rot):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'    
    
    if char.isalpha():
        new_position = ((alphabet_position(char) + rot) % 26)
        if char.isupper():            
            return alphabet[new_position].upper()
        else:
            return alphabet[new_position]

    else:
        return char