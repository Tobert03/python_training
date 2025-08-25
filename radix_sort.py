
array1 = [123,654,765,234,156,876,693,732,10,15,45,46]

def redix_sort(array):
  redix_array = [ [], [], [], [], [], [], [], [], [], [] ]    #10 sub lists for the values 0 to 9

  exp = 1

  while max(array) // exp > 0:    #as many loops as the biggest value has characters

    for i in range(len(array)):     #loops through original array
      value = array.pop(0)
      index = (value // exp) % 10     #example 234 // 1 = 234 % 10 = 4 / in 2nd loop 234 // 10 = 23 % 10 = 3
      redix_array[index].append(value)       #starting from the right most character: the value of the character = the sub array the value gets appended to
    
    for list in redix_array:
      for i in range(len(list)):
        value = list.pop(0)
        array.append(value)       #after getting sorted in the redix_array the values getting back in the original array in sorted order
    
    exp *= 10
  return array

print(redix_sort(array1))
