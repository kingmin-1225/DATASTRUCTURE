from priority_queue_base import PriorityQueueBase

class HeapPriorityQueue(PriorityQueueBase):
  def _parent(self, j):
    return (j-1)//2
  
  def _left(self, j):
    return 2*j+1
  
  def _right(self, j):
    return 2*j+2
  
  def _has_left(self, j):
    return self._left(j) < len(self._data)
  
  def _swap(self, i, j):
    self._data[i], self._data[j] = self._data[j], self._data[i]
  
  def _upheap(self, j):
    parent = self._parent(j)
    if j > 0 and self._data[j] < self._data[parent]:
      self._swap(parent, j)
      self._swap(parent)
  
  def _downheap(self, j):
    if self._has_left(j):
      left = self._left(j)
      small_child = left
      if self._has_right(j):
        right = self._right(j)
        if self._data[right] < self._data[left]:
          small_child = right
      if self._data[small_child] < self._data[j]:
        self._swap(small_child, j)
        self._downheap(small_child)
  
  #------------------public behaviors
  def __init__(self):
    self._data = []
  
  def __len__(self):
    return len(self._data)
  
  def add(self, key, value):
    self._data.append(self._Item(key, value))
    self._upheap(len(self._data)-1)
  
  def min(self):
    if self.is_empty():
      raise Exception('Priority queue is empty')
    item = self._data[0]
    return item._key, item._value
  
  def remove_min(self):
    if self.is_empty():
      raise Exception('Priority queue is empty')
    self._swap(0, len(self._data)-1)
    item = self.pop()
    self._downheap(0)
    return item._key, item._value