class RedBlackTree:
  class _Node:
    def __init__(self, k, v):
      self._red = True
      self._key = k
      self._value = v
      self._left = None
      self._right = None
      self._parent = None
  
  def __init__(self):
    self._root = None
    self._size = 0
  
  def is_empty(self):
    return self._size == 0
  
  def _search(self, node, k):
    if node is None:
      return None
    if node._key == k:
      return node
    elif node._key < k and node._right:
      return self._search(node._right, k)
    elif node._key > k and node._left:
      return self._search(node._left, k)
    return node
  
  def __getitem__(self, k):
    node = self._search(self._root, k)
    if node and node._key == k:
      return node._key
    raise KeyError('Key Error'+repr(k))
  
  def _right_rotate(self, y):
    x = y._left
    T2 = x._right
    x._right = y
    y._left = T2
    x._parent = y._parent
    y._parent = x
    if T2:
      T2._parent = y
    
    if x._parent:
      if x._parent._left == y:
        x._parent._left = x
      else:
        x._parent._right = x
    else:
      self._root = x
    return x
  
  def _left_rotate(self, x):
    y = x._right
    T2 = y._left
    y._left = x
    x._right = T2
    y._parent = x._parent
    x._parent = y
    if T2:
      T2._parent = x
    if y._parent:
      if y._parent._left == x:
        y._parent._left = y
      else:
        y._parent._right = y
    else:
      self._root = y
    return y

  def _sibling(self, node):
    if node._parent is None:
      return None
    if node._parent._left == node:
      return node._parent._right
    return node._parent._left
  
  def _remedying_double_red(self, node):
    if node._parent is None or not(node._red and node._parent._red):
      return
    parent = node._parent
    uncle = self._sibling(parent)
    grandpa = parent._parent
    if uncle is None or not uncle._red: # case1
      grandpa._red = True
      if parent == grandpa._right:
        if node == parent._left:
          self._right_rotate(parent)
          node._red = False
        else:
          parent._red = False
        self._left_rotate(grandpa)
      else:
        if node == parent._right:
          self._left_rotate(parent)
          node._red = False
        else:
          parent._red = False
        self._right_rotate(grandpa)
    else: # case2
      grandpa._red = False if self._root else True
      uncle._red = False
      parent._red = False
      self._remedying_double_red(grandpa)


  def __setitem__(self, k, v):
    if self.is_empty():
      self._root = self._Node(k, v)
      self._root._red = False
      return
    node = self._search(self._root, k)
    if node._key == k:
      node._value = v
    elif node._key < k:
      newnode = self._Node(k, v)
      newnode._parent = node
      node._right = newnode
      ## red 중복 처리
      self._remedying_double_red(newnode)
    else:
      newnode = self._Node(k, v)
      newnode._parent = node
      node._left = newnode
      ## red 중복 처리
      self._remedying_double_red(newnode)
