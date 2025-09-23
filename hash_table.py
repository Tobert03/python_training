class Node:     #nodes for the linked lists
  def __init__(self, value, next = None):
    self.value = value
    self.next = next    #just using a singly linkedlist to safe storage
  def get_next(self):
    return self.next
  def set_next(self, node):
    self.next = node
    

class Bucket:     #linked lists working as buckets
  def __init__(self):
    self.head = None
    self.size = 0

  def is_empty(self):
    return self.size == 0
  def get_size(self):
    return self.size
  def set_head(self, node):
    self.head = node

  def add_node(self, value):  #adds a node to the front (head) of the list
    temp = Node(value)
    if self.is_empty() == False:
      temp.set_next(self.head)
    self.head = temp
    self.size += 1

  def _delete_node(self, prev_node, next_node):   #sets pointer of previous node to the node after the one we deleting
    if prev_node and next_node:
      prev_node.set_next(next_node)
    elif prev_node:                   #if there is no next node, set prev pointer to None
      prev_node.set_next(None)
    elif next_node:
      self.set_head(next_node)        #if there is no previous node, make next node the head
    else:
      self.set_head(None)         #if its the only node in the list set head to None
    self.size -= 1
    
  def _search_node(self, value):    #searching for a value in the list and returns if it was found + prev and next node of it
    if self.is_empty():
      return False, None, None      #straight up ends the function if the list is empty
    current_node = self.head
    prev_node = None
    next_node = current_node.next
    while current_node != None:
      if value == current_node.value:         #iterating through the list, checking every node
        return True, prev_node, next_node
      current_node = next_node
      try:
        next_node = current_node.get_next()     #if there is no next node, next_node is set to None
      except:
        next_node = None
      try:
        prev_node = prev_node.get_next()      #used this try/except block to set the prev_node at the end of 1st iteration and update it in the second
      except:
        prev_node = self.head
    return False, None, None     #return if node is not found

  def search_value(self, value):    #public search function thats using the private one and only returning the bool value
    bool, prev, next = self._search_node(value)
    return bool
  
  def delete_value(self, value):        #public delete function using the private search and delete function
    bool, prev, next = self._search_node(value)
    if bool == True:
      self._delete_node(prev, next)
      return f"{value} deleted"
    else:
      return f"{value} doesn't exist"

class hashTable:    #Hash Table, implemented as a list with 10 Buckets(LinkedLists)
  def __init__(self):
    self.table = [Bucket(), Bucket(), Bucket(), Bucket(), Bucket(), Bucket(), Bucket(), Bucket(), Bucket(), Bucket()]

  #private functions for adding, searching and deleting values:
  def _add_value(self, value, index):
    self.table[index].add_node(value)

  def _search_value(self, value, index):
    return self.table[index].search_value(value)
  
  def _delete_value(self, value, index):
    return self.table[index].delete_value(value)

  def _hash_function(self, value):     #hashing the string values into a number between 0 and 9(index of its Bucket in the tabe)
    return sum(ord(char) for char in value) % 10
  
  #public functions:
  def add_value(self, value):
    index = self._hash_function(value)
    self._add_value(value, index)
    return f"{value} was added to the dataset"

  def search_value(self, value):
    index = self._hash_function(value)
    return f"{value} in dataset: {self._search_value(value, index)}"
  
  def delete_value(self, value):
    index = self._hash_function(value)
    return self._delete_value(value, index)