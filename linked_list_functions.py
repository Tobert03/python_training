
class Node:
  def __init__(self, value):  #creating a new node / pointer gets set after all the nodes are created
    self.value = value
    self.pointer = None

  def show_list(self):    #input = head node / output = prints all value of the linked list
    while self.value:
      print(self.value)
      if self.pointer == None:
        break
      self = self.pointer

  def find_lowest_value(head):    #input = head node / output = lowest value in the linked list
    lowest_val = head
    current_node = head.pointer
    while current_node:
      if current_node.value < lowest_val.value:
        lowest_val = current_node
        if current_node.pointer == None:
          break
      else:
        None
      
      current_node = current_node.pointer
    return lowest_val
  
  def get_node(head, node_index):   #input = head.node and index of the node u r searching / output = node object
    index = node_index - 1
    current_node = head
    while current_node.value:
      if index == 0:
        return current_node
      if current_node.pointer == None:
        break
      current_node = current_node.pointer
      index -= 1

  def del_node(head, node_index):     #input = head object and index of the node u want to delete / deletes the node
    
    middle_node = Node.get_node(head, node_index)
    if head == middle_node:
      return head.next
    
    left_node = Node.get_node(head, node_index - 1)
    right_node = Node.get_node(head, node_index + 1)

    left_node.pointer = right_node
    del middle_node
    return head
      
  def insert_node(head, name, index, value):    #input = head object, name of the node we creating, index where to insert the new node and value of the node / inserts a new node at a defined index
    name = Node(value)

    try:
      right_node = Node.get_node(head, index)
      name.pointer = right_node
    except:
      None

    try:
      left_node = Node.get_node(head, index - 1)
      left_node.pointer = name
    except:
      None

  #def sort_list(head):
    

node1 = Node(11)
node2 = Node(25)
node3 = Node(2)
node4 = Node(55)

node1.pointer = node2
node2.pointer = node3
node3.pointer = node4



#node1.show_list()

#print("lowest value: ",Node.find_lowest_value(node1).value)

#print(Node.get_node(node1, 2).value)

node1 = Node.del_node(node1, 3)

#Node.insert_node(node1, "node5", 3, 33)

Node.show_list(node1)
#Node.show_list(node1)
