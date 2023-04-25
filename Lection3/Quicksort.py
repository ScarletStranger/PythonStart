def quicksort(array):
    if len(array) <= 1:
        return array
    else:
        pivot = array[0]
    lesser = [i for i in array[1:] if i <= pivot]
    greater = [i for i in array[1:] if i > pivot]
    return quicksort(lesser) + [pivot] + quicksort(greater)

print(quicksort([10,5,2]))
