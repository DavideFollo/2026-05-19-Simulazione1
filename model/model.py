import networkx as nx

from database.DAO import DAO


class Model:
    def __init__(self):
        self._IdMapGeneri = DAO.getAllGenre(self)
        self._IdMapArtisti = {}



    def getGeneri(self):
        res = []
        for v in self._IdMapGeneri.values():
            res.append(v)
        return res

    def getNodes(self, genere):
        artisti = DAO.getAllNodes(genere)
        for a in artisti:
            self._IdMapArtisti[a.ArtistId] = a
        return artisti


    def build_graph(self):
        self._graph =nx.DiGraph()
        self._graph.add_nodes_from(self._IdMapArtisti)