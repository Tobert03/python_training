
array1 = [1,34,32,4,75,6,37,5,44,5,68,7,27,55,44,3,25,2,36,56,7,8,9]


def merge_sort(array):
  mid = len(array)//2
  sub1 = array[:mid]      #splitting array into 2 sub arrays
  sub2 = array[mid:]

  if len(sub1) > 1:
    merge_sort(sub1)      #recursively splitting every sub array if it has at least 2 values
  if len(sub2) > 1:
    merge_sort(sub2)

  merge(array, sub1, sub2)    #merging the arrays together again while sorting the values

  return array

def merge(array, sub1, sub2):
  array.clear()
  while len(sub1) > 0 and len(sub2) > 0:      #compare the first values of the 2 arrays 
    if sub1[0] < sub2[0]:
      array.append(sub1.pop(0))               #appending the lower value to the main array until 1 sub array is empty
    else:
      array.append(sub2.pop(0))
  
  if len(sub1) > 0:
    for i in range(len(sub1)):                #appending the remaining values of 1 sub array to the main array
      array.append(sub1.pop(0))
  if len(sub2) > 0:
    for i in range(len(sub2)):
      array.append(sub2.pop(0))

  return array
  
print(merge_sort(array1))