def extract_full_names(people):
    # full_name = []
    # for names in people:
    #     full_name.append(names['first'] + ' ' + names['last'])
    # return full_name
    return [names['first'] + ' ' + names['last'] for names in people]
    #I love comprehensions
    """Return list of names, extracting from first+last keys in people dicts.

    - people: list of dictionaries, each with 'first' and 'last' keys for
              first and last names

    Returns list of space-separated first and last names.

        >>> names = [
        ...     {'first': 'Ada', 'last': 'Lovelace'},
        ...     {'first': 'Grace', 'last': 'Hopper'},
        ... ]

        >>> extract_full_names(names)
        ['Ada Lovelace', 'Grace Hopper']
    """

names = [
    {'first': 'Ada', 'last': 'Lovelace'},
    {'first': 'Grace', 'last': 'Hopper'},
 ]

print(extract_full_names(names))