class Queue:
  class _Node:
    def __init__(self, e):
      self._element = e
      self._next = None
  def __init__(self):
    self._head = None
    self._tail = None
    self._size = 0
  
  def is_empty(self):
    return self._size == 0
  
  def __len__(self):
    return self._size
  
  def top(self):
    if self.is_empty():
      raise Exception("Queue is Empty")
    return self._head._element
  
  def enqueue(self, e):
    newnode = self._Node(e)
    if self.is_empty():
      self._head = newnode
    else:
      self._tail._next = newnode
    self._tail = newnode
    self._size += 1
  
  def dequeue(self):
    if self.is_empty():
      raise Exception("Queue is Empty")
    answer = self._head._element
    self._head = self._head._next
    self._size -= 1
    if self.is_empty():
      self._tail = None
    return answer