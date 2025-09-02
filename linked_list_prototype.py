
class Node:
  def __init__(self, value):
    self.value = value
    self.pointer = None

  def show_list(self):
    while self.value:
      print(self.value)
      if self.pointer == None:
        break
      self = self.pointer

node1 = Node(11)
node2 = Node(25)
node3 = Node(2)
node4 = Node(55)

node1.pointer = node2
node2.pointer = node3
node3.pointer = node4


node1.show_list()