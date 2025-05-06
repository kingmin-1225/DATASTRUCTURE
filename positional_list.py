from doubly_linked_base import _DoublyLinkedBase

class PositionalList(_DoublyLinkedBase):

  ##------------------------------nested Position class--------------------------
  class Position:
    def __init__(self, container, node): ## container는 PositionalList 자체를 의미, node는 해당 Position의 node를 의미미
      self._container = container
      self._node = node
    
    def element(self):
      return self._node._element
    
    def __eq__(self, other):
      return type(other) is type(self) and other._node is self._node
    
    def __ne__(self, other):
      return not (self == other)
  
  ##-----------------------------utility method---------------------------
  def _validate(self, p): ## Position p가 유효한(실제 존재하는지) Position인지 확인 후 해당 Position 안의 node 반환환
    if not isinstance(p, self.Position): # p의 type이 Position인지 확인
      raise TypeError('p must be proper Position type')
    if p._container is not self:
      raise ValueError('p does not belong to this container')
    if p._node._next is None:
      raise ValueError('p is no longer valid')
    return p._node   ## 
  
  def _make_position(self, node):
    if node is self._header or node is self._trailer:
      return None
    else:
      return self.Position(self, node)
  
  ##----------------------------accessors---------------------
  def first(self):
    return self._make_position(self._header._next)
  
  def last(self):
    return self._make_position(self._trailer._prev)
  
  def before(self, p):
    node = self._validate(p)
    return self._make_position(node._prev)
  
  def after(self, p):
    node = self._validate(p)
    return self._make_position(node._next)
  
  def __iter__(self):
    cursor = self.first()
    while cursor is not None:
      yield cursor.element()
      cursor = self.after(cursor)
  
  ##---------------------------mutators--------------------------
  def _insert_between(self, e, predecessor, successor):
    node = super()._insert_between(e, predecessor, successor) ## self._insert_between을 하게 되면 재귀문임 여기서 원하는 것은 부모 클래스의 _insert_between을 실행하여 node를 얻는 것임
    return self._make_position(node)
  
  def add_first(self, e):
    return self._insert_between(e, self._header, self._header._next)
  
  def add_last(self, e):
    return self._insert_between(e, self._trailer.prev, self._trailer)
  
  def add_before(self, p, e):
    original = self._validate(p)
    return self._insert_between(e, original._prev, original)
  
  def add_after(self, p, e):
    original = self._validate(p)
    return self._insert_between(e, original, original._next)
  
  def delete(self, p):
    original = self._validate(p)
    return self._delete_node(original)
  
  def replace(self, p, e):
    original = self._validate(p)
    old_value = original._element
    original._element = e
    return old_value