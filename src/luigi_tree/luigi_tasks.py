import luigi
import time
import os

class Node(luigi.Task):
    """
    Basic Node class implementation which requires two more Node
    Tasks if the tree has more levels to schedule. Some Node classes
    will share Node requirements forming a pascal-like Node triangle.
    """
    level = luigi.IntParameter()
    node_id = luigi.IntParameter()
    leaf = luigi.IntParameter()
    sleep = luigi.IntParameter()
    output_dir = luigi.Parameter()

    def output(self):
        file_name = 'Level_{}_NodeID_{}_Leaf_{}.txt'.format(self.level, self.node_id, self.leaf)
        return luigi.LocalTarget(os.path.join(self.output_dir, file_name))

    def requires(self):
        next_level = self.level - 1
        if next_level != 0:
            if self.leaf:
                return ( Node(next_level, self.node_id+1, 1, self.sleep, self.output_dir),
                         Node(next_level, self.node_id-1, 0, self.sleep, self.output_dir) )
            else:
                return ( Node(next_level, self.node_id+1, 0, self.sleep, self.output_dir),
                         Node(next_level, self.node_id+1, 1, self.sleep, self.output_dir) )

    def run(self):
        time.sleep(self.sleep)
        with self.output().open('w') as outfile:
            outfile.write('Node file\n')
            outfile.write('Level: ' + str(self.level) + '\n')
            outfile.write('Node ID: ' + str(self.node_id) + '\n')
            outfile.write('Leaf: ' + str(self.leaf) + '\n')

class Root(luigi.Task):
    """
    Basic Root task that requires two leaf Node tasks:
                           R
                          / \
                         N1 N2
    """
    level = luigi.IntParameter()
    sleep = luigi.IntParameter()
    output_dir = luigi.Parameter()

    def output(self):
        file_name = 'Root_Level_{}.txt'.format(self.level)
        return luigi.LocalTarget(os.path.join(self.output_dir, file_name))

    def requires(self):
        return ( Node(self.level, self.level*2, 0, self.sleep, self.output_dir),
                 Node(self.level, self.level*2, 1, self.sleep, self.output_dir) )

    def run(self):
        time.sleep(self.sleep)
        with self.output().open('w') as f:
            f.write('Root file\nLevel: ' + str(self.level) + '\n')

