
class Node:
    def __init__(self, value = None, request = None, left_child = None, right_child = None, parent = None):
        self.value = value
        self.request = request
        self.left_child = left_child
        self.right_child = right_child
        self.parent = parent

    def setLeftChild(self, node):
        self.left_child = node
    def setRightChild(self, node):
        self.right_child = node
    def getLeftChild(self):
        return self.left_child
    def getRightChild(self):
        return self.right_child
    def setRequest(self, request):
        self.request = request
    def getRequest(self):
        return self.request
    def setValue(self, value):
        self.value = value
    def getValue(self):
        return self.value
    def setParent(self, node):
        self.parent = node
    def getParent(self):
        return self.parent
    
class Heap:
    def __init__(self, head = None, nodes_count = 0):
        self.head = head
        self.nodes_count = nodes_count

    def getMax(self):
        return self.head

    def isEmpty(self):  #returns yes if the tree is empty
        return (self.nodes_count == 0)
    
    def isOdd(self, number):
        return number % 2 != 0
    
    def getHeight(self): #returns the height of the tree
        if self.nodes_count <= 1:
              return 0
        height = 1
        pot = 2
        maxNodes = 2**pot-1
        while self.nodes_count > maxNodes:
            pot += 1
            maxNodes = 2**pot-1
            height += 1
        return height
    
    def getMaxNodes(self):  #returns the maxNodes based on the height of the tree
        return (2**(self.getHeight() + 1))-1

    def getInsertionPath(self): #returns the pathe to insert the next node (inverted)
        insertion_path = []
        iterations = self.getHeight()
        if iterations == 0 and self.nodes_count == 1 or self.nodes_count == self.getMaxNodes():
              iterations += 1
        number = self.nodes_count + 1
        for i in range(iterations):
            if self.isOdd(number):
                insertion_path.append("r")
                number = (number - 1) / 2
            else:
                insertion_path.append("l")
                number = number / 2
        return insertion_path
    
    def _switchNodes(self, node1, node2):
        node1.value, node2.value = node2.value, node1.value
        node1.request, node2.request = node2.request, node1.request
    
    def _bubbleUp(self, node):  #node gets sorted up as long as its value is bigger than the parent value
        while node.parent and node.value > node.parent.value:
            self._switchNodes(node, node.parent)
            node = node.parent

    def _bubbleDown(self, node):
        if node.left_child == None:
            return
        if node.left_child and node.right_child == None:
            if node.left_child.value > node.value:
                self._switchNodes(node, node.left_child)
                node = node.left_child
            else:
                return
        if node.right_child.value > node.value:
            self._switchNodes(node, node.right_child)
            node = node.right_child
        else:
            return
        self._bubbleDown(node)

    def _getLastNodePath(self):
        last_node_path = []
        iterations = self.getHeight()
        if iterations == 0 and self.nodes_count == 1 or self.nodes_count == self.getMaxNodes():
              iterations += 1
        number = self.nodes_count
        for i in range(iterations):
            if self.isOdd(number):
                last_node_path.append("r")
                number = (number - 1) / 2
            else:
                last_node_path.append("l")
                number = number / 2
        return last_node_path
    
    def _getLastNode(self):
        last_node_path = self._getLastNodePath()
        current_node = self.head
        while last_node_path:
            if len(last_node_path) == 1:
                last_step = last_node_path[0]
            dir = last_node_path.pop(-1)
            if dir == "l":
                current_node = current_node.left_child
            else:
                current_node = current_node.right_child
        return current_node, last_step

    def extractMax(self):
        last_node, last_step = self._getLastNode()
        self._switchNodes(self.head, last_node)
        if last_step == "l":
            last_node.parent.setLeftChild(None)
        else:
            last_node.parent.setRightChild(None)
        last_node.setParent(None)
        last_node.setLeftChild(None)
        last_node.setRightChild(None)
        self._bubbleDown(self.head)
        self.nodes_count -= 1

    def insert(self, value, request):     #inserts a new node at the bottom of the tree
        node = Node()
        node.setValue(value)
        node.setRequest(request)
        if self.isEmpty():
            self.head = node
            self.nodes_count += 1
            return
        current_node = self.head
        path = self.getInsertionPath()
        while len(path) > 1:
            dir = path.pop(-1)
            if dir == "l":
                current_node = current_node.left_child
            else:
                current_node = current_node.right_child
        for i in path:
            if i == "l":
                current_node.left_child = node
                node.parent = current_node
            else:
                current_node.right_child = node
                node.parent = current_node
        self._bubbleUp(node)
        self.nodes_count += 1

    
    
    
    
heap1 = Heap()

heap1.insert(1, "Tastatur klemmt")
heap1.insert(2, "FSV hängt")
heap1.insert(3, "Rosi defekt")
heap1.insert(6, "Büro brennt")
heap1.insert(2, "Rechner kaputt")
heap1.insert(18, "sgfsf")
heap1.insert(27, "asdasfrj")
heap1.insert(4, "sfsdfsf")
heap1.insert(3, "ghjghj")


max = heap1.getMax()
print(max.value, max.request)
last = heap1._getLastNode()
heap1.extractMax()
max = heap1.getMax()
print(max.value, max.request)
heap1.extractMax()
max = heap1.getMax()
print(max.value, max.request)
heap1.extractMax()
max = heap1.getMax()
print(max.value, max.request)