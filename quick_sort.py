
array1 = [1,34,32,4,75,6,37,5,44,5,68,7,27,55,44,3,25,2,36,56,7,8,9]


def quick_sort(array):

  if len(array) <= 1:   #need this bc the funtion is recursive
    return array

  pivot = array[len(array)-1]   #last value in array is the pivot value

  pointer1 = 0      #this pointer is the index from the current value we compare
  pointer2 = -1     #only increases if we want to swap a value

  for i in array:
    if i <= pivot:
      pointer2 += 1
      array[pointer1], array[pointer2] = array[pointer2], array[pointer1]     #values getting swapped If a value smaller or eq than the pivot is found
    pointer1 += 1
  
  '''after the loop all values lower than the pivot value are on the left side of the array, the higher ones are on the right side
  and the pivot value is placed between them, putting it on its perfectly sorted index, seperating the array in 2 parts (higher and lower)

  the following block of code calls this function with the lower part of the array as well as with the higher part:
  - because it is recursive this behaviour is done with every sub-array that gets created in the process until the whole array is sorted
  '''
  lower_part = array[0:pointer2]
  array[0:pointer2] = quick_sort(lower_part)
  upper_part = array[pointer2+1:len(array)]
  array[pointer2+1:len(array)] = quick_sort(upper_part)

  return array

print(quick_sort(array1))
