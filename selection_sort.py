
array1 = [34,32,4,75,6,37,5,44,5,68,7,27,55,44,3,25,2,36,56,7,8,9]

def selection_sort(array):
    for i in range(len(array)):
        sorted = True
        lowest = array[i]
        for j in range(i, len(array)):
            if array[j] < lowest:
                lowest = array[j]
                sorted = False
        array.insert(i, lowest)
        print(array)


selection_sort(array1)
