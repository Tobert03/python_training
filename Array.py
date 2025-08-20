
#Array bzw Liste:
array = [5,4,3,3,5,6,7,7,5,4,32]

#Variable für kleinsten Wert:
lowest = array[0]

#Array wird durchgegangen und der kleinste wert in der Variable gespeichert:
for i in array:
  if i < lowest:
    lowest = i

print(lowest)