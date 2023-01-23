#Selection Sort
def selection_sort(list):
    var = len(list)
    for i in range(var-1): 
        min = i

        for j in range(i+1, var):
            if list[j] < list[min]:
                min = j

        if min != i:
            temp = list[i]
            list[i] = list[min]
            list[min] = temp

    return list
