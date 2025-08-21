
array1 = [34,32,4,75,6,37,5,44,5,68,7,27,55,44,3,25,2,36,56,7,8,9]


#selection sort bedeutet, dass immer der niedrigste Wert, nach ganz vorne gestellt wird, so lange bis die liste sortiert ist
def selection_sort(array):
    for i in range(len(array)):     #die Äußere loop macht so viele Iterationen wie es Elemente zum sortieren gibt
        lowest = array[i]
        lowest_ind = 0
        for j in range(i, len(array)):      #die innere loop startet beim Index i, da ab dort immer die unsortierte Liste anfängt
            if array[j] < lowest:           #und findet den kleinsten wert, in der noch unsortierten liste
                lowest = array[j]
                lowest_ind = j
        print(array)
        array.insert(i, lowest)     #der kleinste Wert wird vorne eingefügt 
        array.pop(lowest_ind+1)     #und an seiner originalen stelle gelöscht
        

selection_sort(array1)

