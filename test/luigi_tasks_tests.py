import unittest
import mock
import os
from luigi_tree import luigi_tasks

class TestNode(unittest.TestCase):
    @mock.patch('luigi.LocalTarget')
    def test_output(self, mock_local_target):
        node = luigi_tasks.Node(level=1, node_id=1,
                                leaf=1, sleep=1,
                                output_dir='foo')
        node.output()
        output_file = 'foo/Level_1_NodeID_1_Leaf_1.txt'
        mock_local_target.assert_called_once_with(output_file)

    def test_requires_left_leaf(self):
        kwargs = {'level': 2, 'node_id': 1,
                  'leaf': 1, 'sleep': 1,
                  'output_dir': 'foo'}
        root_node = luigi_tasks.Node(**kwargs)
        actual = root_node.requires()

        kwargs['level'] = 1
        kwargs['node_id'] = 2
        right_node = luigi_tasks.Node(**kwargs)

        kwargs['node_id'] = 0
        kwargs['leaf'] = 0
        left_node = luigi_tasks.Node(**kwargs)

        expected = ( right_node, left_node )
        self.assertEqual(actual, expected)

    def test_requires_right_leaf(self):
        kwargs = {'level': 2, 'node_id': 1,
                  'leaf': 0, 'sleep': 1,
                  'output_dir': 'foo'}
        root_node = luigi_tasks.Node(**kwargs)
        actual = root_node.requires()

        kwargs['level'] = 1
        kwargs['node_id'] = 2
        right_node = luigi_tasks.Node(**kwargs)

        kwargs['leaf'] = 1
        left_node = luigi_tasks.Node(**kwargs)

        expected = ( right_node, left_node )
        self.assertEqual(actual, expected)

    def test_run(self):
        kwargs = {'level': 2, 'node_id': 1,
                  'leaf': 0, 'sleep': 0,
                  'output_dir': '.'}
        root_node = luigi_tasks.Node(**kwargs)
        try:
            root_node.run()
            expected = ['Node file\n', 'Level: 2\n', 'Node ID: 1\n', 'Leaf: 0\n']

            with open('Level_2_NodeID_1_Leaf_0.txt') as f:
                actual = f.readlines()

            self.assertEqual(actual, expected)
        finally:
            os.remove('Level_2_NodeID_1_Leaf_0.txt')

class TestRoot(unittest.TestCase):
    @mock.patch('luigi.LocalTarget')
    def test_output(self, mock_local_target):
        root = luigi_tasks.Root(level=1, sleep=1,
                                output_dir='foo')
        root.output()
        output_file = 'foo/Root_Level_1.txt'
        mock_local_target.assert_called_once_with(output_file)

    def test_requires(self):
        kwargs = {'level': 2, 'sleep': 1,
                  'output_dir': 'foo'}
        root_node = luigi_tasks.Root(**kwargs)
        actual = root_node.requires()

        kwargs['node_id'] = kwargs['level']*2
        kwargs['leaf'] = 0
        right_node = luigi_tasks.Node(**kwargs)

        kwargs['leaf'] = 1
        left_node = luigi_tasks.Node(**kwargs)

        expected = ( right_node, left_node )
        self.assertEqual(actual, expected)

    def test_run(self):
        kwargs = {'level': 2, 'sleep': 0,
                  'output_dir': '.'}
        root_node = luigi_tasks.Root(**kwargs)
        try:
            root_node.run()
            expected = ['Root file\n', 'Level: 2\n']

            with open('Root_Level_2.txt') as f:
                actual = f.readlines()

            self.assertEqual(actual, expected)
        finally:
            os.remove('Root_Level_2.txt')

if __name__ == '__main__':
    unittest.main()

