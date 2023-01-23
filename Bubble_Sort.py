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

def main():
    print("Array values: [93, 40, 91, 62, 56, 38, 46, 64, 78, 87]")
    print("\nBubble Sort")
    list = [93, 40, 91, 62, 56, 38, 46, 64, 78, 87] # My Array values
    bubble_sort(list)
    print(list) # printing the Bubble Sort

#calling the main
main()