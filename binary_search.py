
array1 = [1,2,3,5,6,7,8,10,13,15,16,18,19,23,24,25,26,30,53,68,84,93,123,157,198,246,379,394,425,467,687,999]

def binary_search(array, target):
  pointer1 = 0                      #left end of the sub array
  pointer2 = len(array)-1           #right end of the sub array
  found = False
  timeout = 0

  while found == False:

    subarray_len = pointer2 - pointer1
    middle = pointer1 + (subarray_len // 2)

    if array[middle] == target:                   #if the middle value of the sub array = the target it returns its index
      return "index: " + str(middle)
    
    if array[middle] > target:                    #if target is smaller than the middle value, sub array goes to the left of it
      pointer2 = pointer2 - (subarray_len//2)
      if (subarray_len//2) == 0:
        pointer1 -= 1
        timeout += 1

    if array[middle] < target:                    #if target is bigger than the middle value, sub array goes to the right of it
      pointer1 = pointer1 + (subarray_len//2)
      if (subarray_len//2) == 0:
        pointer1 += 1
        timeout += 1
    
    if timeout == 2:                              #if the pointers are on the same position for 2 iterations = target not in array
      return "value not found"


    
num = int(input("search value: "))
print(binary_search(array1, num))