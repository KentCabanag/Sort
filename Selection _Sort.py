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

def main():
    list = [93, 40, 91, 62, 56, 38, 46, 64, 78, 87] # My Array values
    selection_sort(list)
    print(list)

#calling the main
main()