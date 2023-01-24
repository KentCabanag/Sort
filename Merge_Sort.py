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
    output = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            output.append(left[i])
            i += 1
        else:
            output.append(right[j])
            j += 1

    output.extend(left[i:])
    output.extend(right[j:])

    return output

def main():
    print("Array values: [93, 40, 91, 62, 56, 38, 46, 64, 78, 87]")
    print("\nMerge Sort")
    unsorted = [93, 40, 91, 62, 56, 38, 46, 64, 78, 87] # My Array values
    sorted = merge_sort(unsorted)
    print(sorted)# printing the Merge Sort

main()