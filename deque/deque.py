class Deque:
  class _Node:
    __slots__ = '_element', '_next', '_prev'
    def __init__(self, e, prev, next):
      self._element = e
      self._next = next
      self._prev = prev
  
  def __init__(self):
    self._head = self._Node(None, None, None)
    self._tail = self._Node(None, self._head, None)
    self._head._next = self._tail
    self._size = 0
  
  def is_empty(self):
    return self._size == 0
  
  def __len__(self):
    return self._size
  
  def head(self):
    if self.is_empty():
      raise Exception('Deque is empty')
    return self._head._next._element

  def tail(self):
    if self.is_empty():
      raise Exception('Deque is empty')
    return self._tail._prev._element

  def push_right(self, e):
    new_node = self._Node(e, self._tail._prev, self._tail)
    self._tail._prev._next = new_node
    self._tail._prev = new_node
    self._size += 1
  
  def push_left(self, e):
    new_node = self._Node(e, self._head, self._head._next)
    self._head._next._prev = new_node
    self._head._next = new_node
    self._size += 1
  
  def pop_right(self):
    if self.is_empty():
      raise Exception('Deque is empty')
    self._size -= 1
    node = self._tail._prev
    self._tail._prev = node._prev
    node._prev._next = self._tail
    return node._element
  
  def pop_left(self):
    if self.is_empty():
      raise Exception('Deque is empty')
    self._size -= 1
    node = self._head._next
    self._head._next = node._next
    node._next._prev = self._head
    return node._element