
array1 = [2,3,1,5,3,2,4,3,1,4,5,3,1,4,2,5,2]
count_array = [0,0,0,0,0]     #the count_array needs to have as many values as there are different values in the array we wanna sort

def counting_sort(array, count_array):
  for i in array:
    count_array[i-1] +=1    #the value is the index of the count_array that gets added +1

  sorted_array = []
  
  for index, i in enumerate(count_array):   #looping through count_array
    for j in range(i):                      #the value is the number of iterations for the inner loop
      sorted_array.append(index+1)          #the value gets added to the new list as often as it got counted
  
  return sorted_array


print(counting_sort(array1, count_array))