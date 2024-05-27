def mode(nums):
    counts = {}
    for num in nums:
        counts[num] = counts.get(num, 0) + 1  
    max_count = 0
    mode_num = None
    for num, count in counts.items():
        if count > max_count:
            max_count = count
            mode_num = num

    return mode_num
    """Return most-common number in list.

    For this function, there will always be a single-most-common value;
    you do not need to worry about handling cases where more than one item
    occurs the same number of times.

        >>> mode([1, 2, 1])
        1

        >>> mode([2, 2, 3, 3, 2])
        2
    """
