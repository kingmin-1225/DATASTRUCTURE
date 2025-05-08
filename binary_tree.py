from tree import Tree
from positional_list import PositionalList

class BinaryTree(Tree, PositionalList):
  class _Node:
    __slots__ = '_element', '_parent', '_left', '_right'
    
    def __init__(self, element, parent=None, left=None, right=None):
      self._element = element
      self._parent = parent
      self._left = left
      self._right = right
  
  def sibling(self, p): # 형제 노드 출력
    parent = self.parent(p)
    if parent is None:
      return None
    if p == self.left(parent):
      return self.right(parent)
    return self.left(parent)
  
  def children(self, p): # 자식 노드 출력
    if self.left(p) is not None:
      yield self.left(p)
    if self.right(p) is not None:
      yield self.right(p)
  
  def _add_root(self, e):
    if self._root is not None:
      raise ValueError('Root exists')
    self._size += 1
    self._root = self._Node(e)
    return self._make_position(self._root)
  
  def _add_left(self, p, e):
    node = self._validate(p)
    if node.left is not None:
      raise ValueError('Left child exists')
    node._left = self._Node(e, node)
    self._size += 1
    return self._make_position(node._left)
  
  def _add_right(self, p, e):
    node = self._validate(p)
    if node._right is not None:
      raise ValueError('Rigth is exists')
    node._right = self._Node(e, node)
    self._size += 1
    return self._make_position(node._right)
  
  def _replace(self, p, e):
    node = self._validate(p)
    old = node._element
    node._element = e
    return old
  
  def _delete(self, p):
    node = self._validate(p)
    if self.num_children(p) == 2:
      raise ValueError('Position has two children')
    child = node._left if node._left else node._right
    if child is not None:
      child._parent = node._parent
    if node is self._root:
      self._root = child
    else:
      parent = node._parent
      if node is parent._left:
        parent._left = child
      else:
        parent._right = child
    self._size -= 1
    node._parent = node
    return node._element