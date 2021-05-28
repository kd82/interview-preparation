def firstDuplicate(a):
    visited = set()
    for elem in a:
        if elem in visited:
            return elem
        visited.add(elem)
    return -1 
    """
    Take aways keep it simple and avoid looping the array twice.
    Read the question properly and look for a hint
    """