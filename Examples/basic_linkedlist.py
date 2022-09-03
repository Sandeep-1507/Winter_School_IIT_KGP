
class Node:

  def __init__(self, data = None, next=None): 
    self.data = data
    self.next = next


class LinkedList:
  def __init__(self):  
    self.head = None
  
  
  def insert(self, data):
    newNode = Node(data)
    if(self.head):
      current = self.head
      while(current.next):
        current = current.next
      current.next = newNode
    else:
      self.head = newNode
  
  
  def print_List(self):
    current = self.head
    while(current):
      print(current.data)
      current = current.next


LL = LinkedList()
LL.insert("Sandeep Patel")
LL.insert("Roll Number")
LL.insert("21MF3IM17")
LL.print_List()