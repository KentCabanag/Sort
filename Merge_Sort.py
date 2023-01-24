# Merge Sort

def merge_sort(list):
    length = len(list)

    if length == 1:
        return list

    mid = length // 2

    left = merge_sort(list[:mid])
    right = merge_sort(list[mid:])

    return merge(left, right)
    
def merge(left, right):
    
