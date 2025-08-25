
array1 = [123,654,765,234,156,876,693,732]

def redix_sort(array):
  redix_array = [ [], [], [], [], [], [], [], [], [], [] ]    #10 sub lists for the values 0 to 9

  characters = len(str(array[0]))    #gets how many characters the values have

  for length in range(characters):    #values have 3 characters = loops 3 times

    for i in range(len(array)):     #loops through original array
      value = array.pop(0)
      string = str(value)
      index = string[int(characters)-1-length]
      redix_array[int(index)].append(value)       #starting from the right most character: the value of the character = the sub array the value gets appended to
    
    for list in redix_array:
      for i in range(len(list)):
        value = list.pop(0)
        array.append(value)       #after getting sorted in the redix_array the values getting back in the original array in sorted order
  return array

print(redix_sort(array1))