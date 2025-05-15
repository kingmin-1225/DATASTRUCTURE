from binary_tree import BinaryTree
from map_base import MapBase

class TreeMap(BinaryTree, MapBase):
  def _subtree_search(self, p, k):
    if k == p.key():
      return p
    elif self.left(p) is not None:
      return self._subtree_search(self.left(p), k)
    else:
      if self.right(p) is not None:
        return self._subtree_search(self.right(p), k)
    return p
  
  def _subtree_first_position(self, p): ## p가 루트노드로 있는 서브트리의 첫번째 요소 반환
    walk = p
    while self.left(walk) is not None:
      walk = self.left(walk)
    return walk
  
  def _subtree_last_position(self, p):  ## p가 루트노드로 있는 서브트리의 마지막 요소 반환
    walk = p
    while self.right(walk) is not None:
      walk = self.right(walk)
    return walk
  
  def first(self):
    return self._subtree_first_position(self.root()) if len(self) > 0 else None
  
  def last(self):
    return self._subtree_last_position(self.root()) if len(self) > 0 else None
  
  def before(self, p):
    self._validate(p)
    if self.left(p):
      return self._subtree_last_position(self.left(p))
    else:
      walk = p
      above = self.parent(walk)
      while walk is not None and walk == self.left(above):
        walk = above
        above = self.parent(walk)
      return above
  
  def after(self, p):
    self._validate(p)
    if self.right(p):
      return self._subtree_first_position(self.right(p))
    else:
      walk = p
      above = self.parent(walk)
      while walk is not None and walk == self.right(above):
        walk = above
        above = self.parent(walk)
      return above
  
  def find_position(self, k):
    if self.is_empty():
      return None
    else:
      p = self._subtree_search(self.root(), k)
      self._rebalance_access(p)
      return p
  
  def find_min(self):
    if self.is_empty():
      return None
    else:
      p = self.first()
      return p.key(), p.value()
  
  def find_ge(self, k):
    if self.is_empty():
      return None
    else:
      p = self.find_position(k)
      if p.key() < k:
        p = self.after(p)
      return p.key(), p.value() if p is not None else None
  
  def find_range(self, start, stop):
    if not self.is_empty():
      if start is None:
        start = self.first()
      else:
        p = self.find_position(start)
        if p.key() < start:
          p = self.after(p)
      while p is not None and (stop is None or p.key() < stop):
        yield p.key(), p.value()
        p = self.after(p)
  
  def __getitem__(self, key):
    if self.is_empty():
      raise KeyError('Key Error' + repr(key))
    else:
      p = self._subtree_search(self.root(), key)
      self._rebalanced_access(p)
      if key != p.key():
        raise KeyError('Key Error: ' + repr(key))
      return p.value()
  
  def __setitem__(self, key, value):
    if self.is_empty():
      leaf = self._add_root(self._Item(key, value))
    else:
      p = self._subtree_search(self.root(), key)
      if p.key() == key:
        p.element()._value = value
        self._rebalance_access(p)
        return
      else:
        item = self._Item(key, value)
        if p.key() < key:
          leaf = self._add_right(p, item)
        else:
          leaf = self._add_left(p, item)
    self._rebalance_insert(leaf)
  
  def __iter__(self):
    p = self.first()
    while p is not None:
      yield p.key()
      p = self.after(p)
  
  def delete(self, p):
    self._validate(p)
    if self.left(p) and self.right(p):
      replacement = self._subtree_last_position(self.left(p))
      self._replace(p, replacement.element())
      p = replacement
    parent = self.parent(p)
    self._delete(p)
    self._rebalance_delete(parent)
  
  def __delitem__(self, key):
    if not self.is_empty():
      p = self._subtree_search(self.root(), key)
      if k == p.key():
        self.delete(p)
        return
      self._rebalance_access(p)
    raise KeyError('Key Error: ' + repr(key))