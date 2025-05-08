from map_base import MapBase
from random import randrange

class HashMapBase(MapBase):
  def __init__(self, cap=11, p=109345121):
    self._table = [None]*cap
    self._n = 0
    self._prime = p
    self._scale = 1 + randrange(p-1)
    self._shift = randrange(p)