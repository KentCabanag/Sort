# Bubble Sort
def bubble_sort(list):
    var = len(list)

    for i in range(var-1):
        for j in range(var-1):
            if list[j] > list[j+1]: 
                tmp = list[j]
                list[j] = list[j+1]
                list[j+1] = tmp

    return list
