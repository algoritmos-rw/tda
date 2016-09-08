from . import dfs

class Kosaraju(dfs.DFS):
  """Componentes fuertemente conexas en un grafo dirigido.
  """
  def __init__(self, G):
    rev_dfs = dfs.DFS(G.reverse())
    super().__init__(G, rev_dfs.reverse_post())

  @staticmethod
  def cfc(G):
    cfc = {}
    dfs = Kosaraju(G)

    for v in G:
      cfc.setdefault(dfs.cc(v), []).append(v)

    return cfc.values()
