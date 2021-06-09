from collections import List, defaultdict
"""
Intial idea i came up with
"""
def groupThePeople1(groupSizes: List[int]) -> List[List[int]]:
    """
    """
    indices = [i for i in range(len(groupSizes))] #O(n)
    zipped = sorted(zip(groupSizes, indices)) #O(n)
    i = 0
    result = []
    while i < len(indices): #O(n)
        c, val = zipped[i]
        curr = []
        for j in range(i, i + c): 
            curr.append(zipped[j][1])
        i += c
        result.append(curr)
    return result

def groupThePeople2(groupSizes: List[int]) -> List[List[int]]: # O(n)
    g_map = dict()
    result = []
    for i, g in enumerate(groupSizes):
        if g not in g_map:
            g_map[g] = []
        g_map[g].append(i)
        if len(g_map[g]) == g:
            result.append(g_map[g])
            g_map[g] = []
    return result


def groupThePeople3(groupSizes: List[int]) -> List[List[int]]: #Same
    g_map = defaultdict(list)
    result = []
    for i, g in enumerate(groupSizes):
        g_map[g].append(i)
        if len(g_map[g]) == g:
            result.append(g_map[g])
            g_map[g] = []
    return result
"""
Key Takeaways
Default list is a life saver and can save a lot of code.
Default value if key is not present can be specified in the argument
"""