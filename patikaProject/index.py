
def flatten(lst):
    flat_list = []
    for item in lst:
        if isinstance(item,list):
            flat_list.extend(flatten(item))
        else:
            flat_list.append(item)
    return flat_list

def reverse_nested(lst):
    reversed_list = []
    for item in lst:
        if isinstance(item, list):
            reversed_list.append(reverse_nested(item))
        else:
            reversed_list.append(item)
    reversed_list.reverse()
    return reversed_list

list1 = [[1,2],[[4,5],6],10,3]
list2 = [[1,2],[5,6],[7,8],[9,10]]
flattened_list1 = flatten(list1)
reversed_list2 = reverse_nested(list2)
print(flattened_list1)
print(reversed_list2)

