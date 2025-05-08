class Tree:
  class Position:
    def __init__(self, container, node): ## container는 PositionalList 자체를 의미, node는 해당 Position의 node를 의미미
      self._container = container
      self._node = node
    
    def element(self):
      raise NotImplemented('must be impolemented by subclass')
    
    def __eq__(self, other):
      raise NotImplemented('must be impolemented by subclass')
    
    def __ne__(self, other):
      return not (self == other)
  
  def root(self):
    raise NotImplemented('must be impolemented by subclass')
  
  def parent(self, p):
    raise NotImplemented('must be impolemented by subclass')
  
  def num_children(self, p):
    raise NotImplemented('must be impolemented by subclass')
  
  def children(self, p):
    raise NotImplemented('must be impolemented by subclass')
  
  def __len__(self):
    raise NotImplemented('must be impolemented by subclass')
  
  def is_root(self, p):
    return self.root() == p
  
  def is_leaf(self, p):
    return self.num_children(p) == 0
  
  def is_empty(self):
    return len(self) == 0
  
  def depth(self, p):
    if self.is_root(p):
      return 0
    else:
      return 1 + self.depth(self.parent(p))
  
  def _height1(self):
    return max(self.depth(p) for p in self.positions() if self.is_leaf(p))
  
  def _height2(self, p):
    if self.is_leaf(p):
      return 0
    else:
      return 1 + max(self._height2(c) for c in self.children(p))
  
  def height(self, p=None):
    if p is None:
      p = self.root()
    return self._height2(p)