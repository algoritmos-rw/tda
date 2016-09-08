#!/usr/bin/env python3

"""Biblioteca de grafos.

Referencias:

  - R. Sedgewick, ‘Algorithms’ (2011, 4.ª ed.).
  - T. H. Cormen et al., ‘Introduction to Algorithms’ (2009, 3.ª ed.).
"""

from .cc import Kosaraju
from .dfs import DFS

class Graph:
  """Un grafo (dirigido o no dirigido) con un número fijo de vértices.

  Los vértices son siempre números enteros no negativos. El primer
  vértice es 0.

  El grafo se crea vacío, se añaden aristas con add_edge(). Puede representar
  grafos no dirigidos, pero el caller debe realizar la segunda llamada a
  add_edge().
  """
  def __init__(g, V):
    """Construye un grafo sin aristas de V vértices.
    """
    assert (V > 0)
    g._V = V
    g._E = 0
    g._adj = [[] for _ in range(V)]

  def V(g):
    return g._V

  def E(g):
    return g._E

  def adj(g, v):
    """Itera sobre los vértices adyacentes a ‘v’.
    """
    return iter(g._adj[v])

  def reverse(g):
    # TODO(dato): might be a good idea to have a separate Digraph class.
    rev = Graph(g.V())

    for u in g:
      for v in g.adj(u):
        rev.add_edge(v, u)

    return rev

  def add_edge(g, u, v):
    g._adj[u].append(v)
    g._E += 1

  def __iter__(g):
    return iter(range(g.V()))


class SymGraph(Graph):
  """Un grafo que acepta cadenas para nombrar a los vértices.
  """
  def __init__(g, vert_names):
    """Construye un grafo sin aristas a partir de los nombres de los vértices.

    Pre-condición: no hay duplicados en ‘vert_names’.
    Post-condición: los vértices se numeraron de 0 a len(vert_names) - 1.
    """
    g._names = list(vert_names)
    g._vertmap = {name: num for num, name in enumerate(g._names)}
    super().__init__(len(g._names))
    assert (g.V == len(g._vertmap))

  def index(g, name):
    """Devuelve el vértice correspondiente a un nombre, o None.
    """
    return g._vertmap.get(name)

  def name(g, v):
    """Devuelve el nombre de un vértice.
    """
    return g._names[v]

  def add_named_edge(g, a, b):
    g.add_edge(g.index(a), g.index(b))
