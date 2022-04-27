import sys

def getNextListItem(listString, startIndex):
  if listString[startIndex] != "(":
    return listString[startIndex]

  countUnclosedParens = 1
  i = startIndex + 1
  
  while countUnclosedParens:
      if listString[i] == "(":
        countUnclosedParens += 1
      elif listString[i] == ")":
        countUnclosedParens -= 1

      i += 1

  return  listString[startIndex: i]

def buildListItems(listString):
  index = 1
  listItems = []

  while index < len(listString) - 1:
    listItem = getNextListItem(listString, index)
    listItems.append(listItem)

    index += len(listItem)

  return listItems


def isSExpression(listItem):
  return listItem[0] == "(" and "." not in listItem

def buildSExpression(listItems):
  sExpression = ""
  i = 0

  for listItem in listItems:
    sExpression += "("
    if isSExpression(listItem):
      sExpression += buildSExpression(buildListItems(listItem))
    else:
      sExpression += listItem
    sExpression += "."

    i += 1
    
    if i == len(listItems):
      sExpression += "()"

  sExpression += ")" * len(listItems)

  return sExpression
  
def listToSExpression(listString):
  listString = listString.replace(" ", "")

  return buildSExpression(buildListItems(listString))


if __name__ == "__main__":
  if (len(sys.argv) < 2):
    print("Usage: python3 " + sys.argv[0] + " list")
    sys.exit(1)

  listString = sys.argv[1]

  print (listToSExpression(listString))


