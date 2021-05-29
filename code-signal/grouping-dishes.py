"""
You are given a list dishes, where each element consists of a list of strings beginning with the name of the dish, 
followed by all the ingredients used in preparing it. You want to group the dishes by ingredients, so that for each ingredient 
you'll be able to find all the dishes that contain it (if there are at least 2 such dishes).

Return an array where each element is a list beginning with the ingredient name, followed by the names of all the dishes that 
contain this ingredient. The dishes inside each list should be sorted lexicographically, and the result array should be sorted 
lexicographically by the names of the ingredients.

"""
def groupingDishes(dishes):
    map = {}
    for dish in dishes:
        dish_name = dish[0]
        for i in dish[1:]:
            if i not in map:
                map[i] = []
            map[i].append(dish_name)
    ans = []
    for key in sorted(map.keys()):
        if len(map[key]) > 1:
            ans.append([key] + sorted(map[key]))
    return ans
"""
    Issues More about the language than the actual implentation 
    Key Takeaways:
    1. We can sort the keys of map directly while iterating
    2. Python sorts the list differently.
    3. If you are spending way too much time then there is something wrong
"""