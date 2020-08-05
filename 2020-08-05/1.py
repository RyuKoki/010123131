##################################################
# Name : Onpinya Phokhahutthakosol
# Student ID : 62-010126-2026-1
# File name : 1.py
##################################################

# update : 05 Aug 2020
class Tree:

    def __init__(self, root, left=None, right=None):
        self.root = root
        self.left = left
        self.right = right

    def __str__(self):
        return '(' + str(self.root) + ', ' + str(self.left) + ', ' + str(self.right) + ')'

# tree_1 = Tree('&', 'I0', 'I1')
# tree_2 = Tree('+', tree_1, Tree('!', Tree('&', 'I1', 'I2'), None))
# print(tree_2)

class Expression(Tree):

    def __init__(self, root, left=None, right=None):
        super().__init__(root, left=None, right=None)
        self.tree_list = []
        
# next is coming soon
