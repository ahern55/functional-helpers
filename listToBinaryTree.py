import sys
from sExpressionToBinaryTree import sExpressionToBinaryTree
from listToSExpression import listToSExpression


def listToBinaryTree(listString):
    sExpressionString = listToSExpression(listString)
    return sExpressionToBinaryTree(sExpressionString)


if __name__ == "__main__":
    if (len(sys.argv) < 2):
        print("Usage: python3 " + sys.argv[0] + " list")
        sys.exit(1)

    listString = sys.argv[1]

    tree = listToBinaryTree(listString)
    tree.display()
