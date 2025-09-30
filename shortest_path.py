import csv

def create_matrix():
  with open("gs.csv", "r") as file:
    csv_reader = csv.reader(file)
    
    rows = 0
    for row in csv_reader:
      rows += 1

    matrix = [[0] * rows for _ in range(rows)]
  return fill_matrix(matrix)

def fill_matrix(matrix):
  with open("gs.csv", "r") as file:
    csv_reader = csv.reader(file)
    for index1, row in enumerate(csv_reader):
        for index2, i in enumerate(row):
          matrix[index1][index2]  = i
  return matrix




def search_path(current, *locations):

  matrix = create_matrix()
  visited = [False] * len(locations)
  path = []
  path.append(str(current))
  
  for _ in range(len(locations)):
    current = current
    min_distance = 1000
    next = None
    for i in range(len(locations)):
      loc2 = locations[i]
      if matrix[current][loc2] == ' None':
        continue
      if int(matrix[current][loc2]) < min_distance and not visited[i]:
        min_distance = int(matrix[current][loc2])
        next = loc2
        index_of_next = i 
    
    if next == None:
      break

    visited[index_of_next] = True

    path.append(str(next))
    current = next
  return '->'.join(path)