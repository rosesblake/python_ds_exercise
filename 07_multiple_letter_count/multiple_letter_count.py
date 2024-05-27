def multiple_letter_count(phrase):
    counts = {}
    for letter in phrase:
        counts[letter] = counts.get(letter, 0) + 1
    return counts

    """Return dict of {ltr: frequency} from phrase.

        >>> multiple_letter_count('yay')
        {'y': 2, 'a': 1}

        >>> multiple_letter_count('Yay')
        {'Y': 1, 'a': 1, 'y': 1}
    """