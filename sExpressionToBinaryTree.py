import sys
from node import Node

def indexOfRootPeriod(sExpressionString: str):
  if (sExpressionString[0] != "("):
    print("atom passed")
    sys.exit(1)
  
  if sExpressionString[1] != "(":
    return sExpressionString.index(".")
  
  i = 1
  flag = True
  countUnclosedParens = 0
  while flag or countUnclosedParens:
      flag = False
      if sExpressionString[i] == "(":
        countUnclosedParens += 1
      elif sExpressionString[i] == ")":
        countUnclosedParens -= 1

      i += 1

  return i

def getSubtreeStrings(sExpressionString):
  partition =  indexOfRootPeriod(sExpressionString)
  return [sExpressionString[1:partition], sExpressionString[partition+1:-1]]
  
def isLeaf(sExpressionString):
  return not sExpressionString or sExpressionString[0] != "(" or sExpressionString == "()"

def sExpressionToBinaryTree(sExpressionString):
  sExpressionString = sExpressionString.replace(" ", "")

  if (isLeaf(sExpressionString)):
    return Node(sExpressionString, None, None)
  else:
    subtrees = getSubtreeStrings(sExpressionString)

    return Node(".", sExpressionToBinaryTree(subtrees[0]), sExpressionToBinaryTree(subtrees[1]))

if __name__ == "__main__":
  if (len(sys.argv) < 2):
    print("Usage: python3 " + sys.argv[0] + " S-Expression")
    sys.exit(1)

  sExpressionString = sys.argv[1]

  tree = sExpressionToBinaryTree(sExpressionString)
  tree.display()