class Queue:
  class _Node:
    __slots__ = '_element', '_next'
    
    def __init__(self, e, next):
      self._element = e
      self._next = next

  def __init__(self):
    self._head = None ## out
    self._tail = None ## in
    self._size = 0
  
  def __len__(self):
    return self._size
  
  def is_empty(self):
    return self._size == 0
  
  def enqueue(self, e):
    newest = self._Node(e, None)
    if self.is_empty():
      self._head = newest
    else:
      self._tail._next = newest
    self._tail = newest
    self._size += 1
  
  def first(self):
    if self.is_empty():
      raise Exception('Queue is empty')
    return self._head._element
  
  def dequeue(self):
    if self.is_empty():
      raise Exception('Queue is empty')
    answer = self._head._element
    self._head = self._head._next
    self._size -= 1
    if self.is_empty():
      self._tail = None
    return answer

# q = Queue()
# q.enqueue(1)
# q.enqueue(2)
# q.enqueue(3)
# q.enqueue(4)
# print(q.first())
# print(q.dequeue())
# print(q.dequeue())
# print(q.dequeue())
# print(len(q))