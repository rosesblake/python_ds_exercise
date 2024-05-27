def flip_case(phrase, to_swap):
    new_phrase = ''
    for let in phrase:
        print(let)
        if(let.upper() == to_swap.upper() and let.isupper()):
            new_phrase += let.lower()
        elif(let.lower() == to_swap.lower() and let.islower()):
            new_phrase += let.upper()
        else: new_phrase += let
    return new_phrase
    """Flip [to_swap] case each time it appears in phrase.

        >>> flip_case('Aaaahhh', 'a')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'A')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'h')
        'AaaaHHH'

    """
