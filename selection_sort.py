
array1 = [1,34,32,4,75,6,37,5,44,5,68,7,27,55,44,3,25,2,36,56,7,8,9]


#selection sort bedeutet, dass immer der niedrigste Wert, nach ganz vorne gestellt wird, so lange bis die liste sortiert ist
def selection_sort(array):
    print(array)
    for i in range(len(array)-1):     #die Äußere loop macht so viele Iterationen wie es Elemente zum sortieren gibt
        lowest = array[i]
        lowest_ind = i
        for j in range(i+1, len(array)):      #die innere loop startet beim Index i, da ab dort immer die unsortierte Liste anfängt
            if array[j] < lowest:           #und findet den kleinsten wert, in der noch unsortierten liste
                lowest = array[j]
                lowest_ind = j
        array[i], array[lowest_ind] = array[lowest_ind], array[i]       #erster und niedrigster wert, werden getauscht
        print(array)
        

selection_sort(array1)
