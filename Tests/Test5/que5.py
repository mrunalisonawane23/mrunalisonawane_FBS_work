def find_union(list1, list2):
    union_list = list(list1)
    
    for item in list2:
        if item not in union_list:
            union_list.append(item)
            
    return union_list

list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]

result = find_union(list1, list2)
print("List 1:", list1)
print("List 2:", list2)
print("Union of lists:", result)