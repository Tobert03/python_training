
array1 = [1,34,32,4,75,6,37,5,44,5,68,7,27,55,44,3,25,2,36,56,7,8,9]

#Prinzip von insertion sort= Array hat einen sortierten teil am anfang der immer Größer wird und sortiert immer den ersten wert aus dem unsortierten teil in den sortierten Teil ein

def insertion_sort(array):
  print(array)
  n = len(array)
  for i in range(n-1):    #n-1 da wir bereits mit dem Einsortieren des 2ten Wertes im array starten 
    value = array[i+1]    #Value zum einsortieren ist der 2te wert und verschiebt sich mit jeder Iteration eins nach rechts
    count = 0   
    for j in array[0:i+1]:    #die innere loop läuft über den Sortierten Teil des arrays, dieser verlängert sich pro Iteration um 1
        if j <= value:
           count += 1           #wenn der Value größer oder gleich des aktuelen wertes des sortierten Teils ist, wird der count um 1 erhöht (damit wird der Index ermittelt in den der Wert einsortiert werden muss)
    array.insert(count, value)    #Value wird an der ermittelten stelle eingefügt
    array.pop(i+2)      #Und an seiner vorherien stelle entfernt (+2, da sich der index durch den insert um 1 verschoben hat)
    print(array)


insertion_sort(array1)


'''
Musterlösung:

my_array = [64, 34, 25, 12, 22, 11, 90, 5]

n = len(my_array)
for i in range(1,n):
    insert_index = i
    current_value = my_array[i]
    for j in range(i-1, -1, -1):
        if my_array[j] > current_value:
            my_array[j+1] = my_array[j]
            insert_index = j
        else:
            break
    my_array[insert_index] = current_value

print("Sorted array:", my_array)
'''

