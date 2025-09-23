class Node:
  def __init__(self, value = None, next_node = None):
    self.value = value
    self.next_node = next_node
  def setNext(self, next):
    self.next_node = next
  def getNext(self):
    return self.next_node
  def getValue(self):
    return self.value

class Stack:
  def __init__(self,size = 0):
    self.top = Node()
    self.size = size

  def isEmpty(self):
    return self.size == 0
  
  def getSize(self):
    return self.size

  def push(self, value):
    temp = Node(value)
    temp.setNext(self.top.getNext())
    self.top.setNext(temp)
    self.size += 1

  def pop(self):
    if self.isEmpty():
      return
    value = self.top.getNext().getValue()
    if self.getSize() > 1:
      self.top.setNext((self.top.getNext()).getNext())
    self.size -= 1
    return value

  def peek(self):
    if self.isEmpty():
      return
    return self.top.getNext().getValue()