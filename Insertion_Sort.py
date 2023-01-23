# Insertion Sort
def insertion_sort(list):  
    for i in range(1, len(list)):  
        current = list[i]  

        j = i - 1  
        while j >= 0 and current < list[j]:  
            list[j+1] = list[j]  
            j -= 1  
        list[j+1] = current  

    return list

def main():
    list = [93, 40, 91, 62, 56, 38, 46, 64, 78, 87] # My Array values
    insertion_sort(list)
    print(list) # printing the Insertion Sort
