###

noods = int(input('Enter number of noods: '))

while noods > 10**4 or noods < 2:
    noods = int(
        input('Please enter a number less than 10,000 and more than 1: '))

###

print('Enter the PreOrder:')
preOrder = input().split(' ')

while len(preOrder) != noods:

    print('Preorder noods count are not equal to noods count. Try Again:')

    preOrder = input().split(' ')


print('Enter the InOrder:')
inOrder = input().split(' ')

while len(inOrder) != noods:

    print('InOrder noods count are not equal to noods count. Try Again:')

    inOrder = input().split(' ')

#### (TEST) TO BE DELETED ###

# noods = 9
# preOrder = "6 2 1 4 3 5 7 9 8".split(' ')
# inOrder = "1 2 3 4 5 6 7 8 9".split(' ')
# preOrder = "25 15 10 4 12 22 18 24 50 35 31 44 70 66 90".split(' ')
# inOrder = "4 10 12 15 18 22 24 25 31 35 44 50 66 70 90".split(' ')

###

preOrder = [int(i) for i in preOrder]
inOrder = [int(i) for i in inOrder]

###

def printPostorder(start, end, preorder, pIndex, dict):

    # base case
    if start > end:
        return pIndex

    # The next element in the preorder sequence will be the root node of
    # subtree formed by sequence `inorder[start, end]`
    value = preorder[pIndex]
    pIndex = pIndex + 1

    # if the current node is a leaf node (no children)
    if start == end:
        # print the value of the root node and return
        print(value, end=' ')
        return pIndex

    # Get the root node index in inorder sequence to determine
    # its left and right subtree boundary
    i = dict[value]

    # recur for the left subtree
    pIndex = printPostorder(start, i - 1, preorder, pIndex, dict)

    # recur for the right subtree
    pIndex = printPostorder(i + 1, end, preorder, pIndex, dict)

    # print the value of the root node
    print(value, end=' ')

    return pIndex


def findPostorder(inorder, preorder):

    # create a dictionary to efficiently find the index of any element in a
    # given inorder sequence
    dict = {}

    # fill the dictionary
    for i, e in enumerate(inorder):
        dict[e] = i

    # `pIndex` stores the index of the next unprocessed node in the preorder sequence.
    # start with the root node (present at 0th index)
    pIndex = 0

    printPostorder(0, len(inorder) - 1, preorder, pIndex, dict)


findPostorder(inOrder, preOrder)