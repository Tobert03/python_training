'''
array1 = [5,4,3,3,5,6,7,7,5,4,32]

def bubble(array):
  
  noChanges = 0
  while noChanges != len(array)-1:
    noChanges = 0
    for i in range(len(array)-1):
      value1 = array[i]
      value2 = array[i+1]
      if value1 > value2:
        array[i] = value2
        array[i+1] = value1
      else:
        noChanges += 1
    print(array)
      

bubble(array1)
'''


array = [34,445,65,34,76,3,5,6,88,6]

n = len(array)

#äußere loop muss 1 mal weniger laufen als die länge des arrays, sonst IndexError
for i in range(n-1):
  swapped = False
  for j in range(n-i-1):      #Innere loop läuft bei jeder ausführung um einen index kürzer, da der größte wert jedes mal nach hinten verschoben wurde
    if array[j] > array[j+1]:
      array[j], array[j+1] = array[j+1], array[j]   #wenn der linke wert größer als der rechte ist werden sie getauscht
      swapped = True
  if not swapped:    #wenn beim durchlaufen des arrays keine werte getauscht wurden, ist die sortierung beendet
    break
  noChanges = 0
  print(array)