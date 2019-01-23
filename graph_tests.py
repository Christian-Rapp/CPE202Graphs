import unittest
from graph import *


class TestList(unittest.TestCase):

    def test_01(self):
        g = Graph('test1.txt')
        self.assertEqual(g.conn_components(), [['v1', 'v2', 'v3', 'v4', 'v5'], ['v6', 'v7', 'v8', 'v9']])
        self.assertTrue(g.is_bipartite())

    def test_02(self):
        g = Graph('test2.txt')
        self.assertEqual(g.conn_components(), [['v1', 'v2', 'v3'], ['v4', 'v6', 'v7', 'v8']])
        self.assertFalse(g.is_bipartite())

    def test_03(self):
        g = Graph('test3.txt')
        self.assertEqual(g.conn_components(), [['v1', 'v2', 'v3', 'v4', 'v5'], ['v6', 'v7', 'v8', 'v9']])

    def test_add_vertex(self):
        g = Graph('test1.txt')
        self.assertEqual(g.get_vertex('v9.5'), None)
        g.add_vertex("v9.5")
        self.assertNotEqual(g.get_vertex('v9.5'), None)
        self.assertEqual(g.get_vertices(), ['v1', 'v2', 'v3', 'v4', 'v5', 'v6', 'v7', 'v8', 'v9', 'v9.5'])
        g.add_vertex('v9.5')
        self.assertEqual(g.get_vertices(), ['v1', 'v2', 'v3', 'v4', 'v5', 'v6', 'v7', 'v8', 'v9', 'v9.5'])
        self.assertNotEqual(g.get_vertices(), ['v1', 'v2', 'v3', 'v4', 'v5', 'v6', 'v7', 'v8', 'v9', 'v9.5', 'v9.5'])

    def test_add_edge(self):
        g = Graph('test1.txt')
        self.assertNotEqual(g.vertex_dict['v4'].adjacent_to, ['v1', 'v2'])
        self.assertEqual(g.vertex_dict['v4'].adjacent_to, ['v1'])
        g.add_edge('v4', 'v2')
        self.assertEqual(g.vertex_dict['v4'].adjacent_to, ['v1', 'v2'])

    def test_connections(self):
        g = Graph('test1.txt')
        # print(g.conn_components())

    def test_bipartite(self):
        g = Graph('test1.txt')
        # print(g.is_bipartite())

if __name__ == '__main__':
   unittest.main()
