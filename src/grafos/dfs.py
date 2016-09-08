"""Implementación de DFS."""

# TODO(dato): timestamps; edge classification; cycles.

import enum

class Color(enum.Enum):
  white = 1
  gray = 2
  black = 3

class _VertInfo:

  def __init__(self):
    self.color = Color.white
    self.parent = None
    self.cc = -1


class DFS:
  """Implementación de depth-first search.
  """
  def __init__(self, G, origins=None):
    self.__pre = []
    self.__post = []
    vert = [_VertInfo() for _ in G]
    cc = 0

    if origins is None:
      origins = G

    for u in list(origins):
      if vert[u].color == Color.white:
        self.__dfs(G, u, vert, cc)
        cc += 1

    self.__vert = vert
    self.__num_cc = cc


  def __dfs(self, G, u, vert, cc):
    """Función recursiva que implementa DFS.

    Recibe el vértice, el arreglo de atributos de los vértices, y la componente
    conexa.
    """
    vert[u].cc = cc
    vert[u].color = Color.gray
    self.__pre.append(u)

    for v in G.adj(u):  # We use (u, v) to match Cormen’s pseudo-code.
      if vert[v].color == Color.white:
        vert[v].parent = u
        self.__dfs(G, v, vert, cc)

    vert[u].color = Color.black
    self.__post.append(u)

  def visited(self, u):
    """Indica si un vértice fue visitado por el recorrido.
    """
    return self.__vert[u].color == Color.black

  def cc(self, u):
    """Devuelve el número de componente conexa de un vértice.
    """
    return self.__vert[u].cc

  def num_cc(self):
    """Número de componentes conexas en el recorrido.
    """
    return self.__num_cc

  def same_cc(self, u, v):
    """Indica si dos vértices pertenecen a la misma componente conexa.
    """
    return self.__vert[u].cc == self.__vert[v].cc

  def pre(self):
    return iter(self.__pre)

  def post(self):
    return iter(self.__post)

  def reverse_post(self):
    return reversed(self.__post)
