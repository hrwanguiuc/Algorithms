# class to represent the tree strucutre
class TreeNode:
    def __init__(self, val=None, key = None, left=None, right=None):
        self.val = val
        self.key = key
        self.left = left
        self.right = right

# construct the table for reference
# format: key -> value
#          11 -> 3

def const(A):
    table = {}
    for i in A:
        key = i / 10
        value = i % 10
        table[key] = value
    return table

# construct the tree
def addNode(root, table):
    num = root.key
    first = num / 10 + 1
    second1 = 2 * (num % 10)
    second2 = second1 - 1 
    l = first * 10 + second1
    r = first * 10 + second2
    if l in table:
        root.left = TreeNode(table[l], l)
    if r in table:
        root.right = TreeNode(table[r], r)
    if root.left:
        addNode(root.left, table)
    if root.right:
        addNode(root.right, table)


def findPathSum(root, total):
    # use the preorder traversal to sum the path
    if not root:
        return 0
    total += root.val

    # when we reach the leaf node
    if not root.left and not root.right:
        return total

    return findPathSum(root.left, total) + findPathSum(root.right, total)


def solution(A):
    table = const(A)
    root = TreeNode(table[11], 11)
    addNode(root, table)
    print findPathSum(root, 0)


if __name__ == "__main__":

    A = [113,215,221,312,324,337,348]
    #A = [113,211,222,312,341,414,481]
    solution(A)

