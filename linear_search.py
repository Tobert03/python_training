array1 = [1,34,32,4,75,6,37,5,44,5,68,7,27,55,44,3,25,2,36,56,7,8,9]

def linear_search(search_value, array):
  output = -1                             #if the value isn't found function returns -1
  for index, i in enumerate(array):
    if i == search_value:
      output = index
      break             #breaking the loop so output is the first occurrence of the value
  return output
  
value = int(input("value: "))
print(linear_search(value, array1))