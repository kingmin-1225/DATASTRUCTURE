class _DoublyLinkedBase:
  class _Node:
    __slots__ = "_element", "_next", "_prev"
    
    def __init__(self, e, prev, next):
      self._element = e
      self._prev = prev
      self._next = next

  def __init__(self):
    self._header = self._Node(None, None, None)
    self._trailer = self._Node(None, None, None)
    self._header._next = self._trailer  
    self._trailer._prev = self._header
    self._size = 0
    ## header -- trailer

  def __len__(self):
    return self._size
  
  def is_empty(self):
    return self._size == 0
  
  def _insert_between(self, e, predecessor, successor):
    newest = self._Node(e, predecessor, successor)
    predecessor._next = newest
    successor._prev = newest
    self._size += 1
    return newest
  
  def _delete_node(self, node):
    predecessor = node._prev
    successor = node._next
    predecessor._next = successor
    successor._prev = predecessor
    self._size -= 1
    element = node._element
    node._prev = node._next = None
    return element