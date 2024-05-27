def single_letter_count(word, letter):
    # count = 0
    # for el in word:
    #     if (el == letter):
    #         count += 1
    # return count

    return word.count(letter)

    """How many times does letter appear in word (case-insensitively)?
    
        >>> single_letter_count('Hello World', 'h')
        1
        
        >>> single_letter_count('Hello World', 'z')
        0
        
        >>> single_letter_count("Hello World", 'l')
        3
    """