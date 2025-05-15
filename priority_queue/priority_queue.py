class PriorityQueue:
  def __init__(self):
    self._data = []
  
  def is_empty(self):
    return len(self._data) == 0
  
  def _swap(self, i, j):
    self._data[i], self._data[j] = self._data[j], self._data[i]
  
  def _left(self, j):
    return j*2+1
  
  def _right(self, j):
    return j*2+2
  
  def _parent(self, j):
    return (j-1)//2
  
  def _upheap(self, j):
    if j == 0:
      return
    parent = self._parent(j)
    if self._data[j] < self._data[parent]:
      self._swap(j, parent)
      self._upheap(parent)
  
  def _downheap(self, j):
    left = self._left(j)
    right = self._right(j)
    small_child = left if left < len(self._data) else -1
    if small_child == -1:
      return
    if right < len(self._data) and self._data[right] < self._data[left]:
      small_child = right
    if self._data[small_child] < self._data[j]:
      self._swap(j, small_child)
      self._downheap(small_child)
  
  def insert(self, e):
    self._data.append(e)
    self._upheap(len(self._data)-1)
  
  def delete(self):
    if self.is_empty():
      raise Exception("PQ is empty")
    self._swap(0, len(self._data)-1)
    answer = self._data.pop()
    self._downheap(0)
    return answer