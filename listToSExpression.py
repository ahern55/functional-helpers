import sys


def getIdentifierStartingAtIndex(listString: str, startIndex):
    result = ""
    i = startIndex
    while not listString[i].isspace() and listString[i] not in {"(", ")"}:
        result += listString[i]
        i += 1

    return [result, i]


def getIndexAfterConsumingWhitespace(listString: str, startIndex):
    i = startIndex
    while listString[i].isspace():
        i += 1

    return i


def getNextListItem(listString, startIndex):
    startIndex = getIndexAfterConsumingWhitespace(listString, startIndex)
    if listString[startIndex] != "(":
        return getIdentifierStartingAtIndex(listString, startIndex)

    countUnclosedParens = 1
    i = startIndex + 1

    while countUnclosedParens:
        if listString[i] == "(":
            countUnclosedParens += 1
        elif listString[i] == ")":
            countUnclosedParens -= 1

        i += 1

    return [listString[startIndex: i], i]


def buildListItems(listString):
    index = 1
    listItems = []

    while index < len(listString) - 1:
        [listItem, i] = getNextListItem(listString, index)
        if listItem:
            listItems.append(listItem)

        index = i

    return listItems


def isSExpression(listItem):
    return listItem and listItem[0] == "(" and "." not in listItem


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


def listToSExpression(listString: str):
    listString = listString.strip()

    return buildSExpression(buildListItems(listString)).replace(" ", "")


if __name__ == "__main__":
    if (len(sys.argv) < 2):
        print("Usage: python3 " + sys.argv[0] + " list")
        sys.exit(1)

    listString = sys.argv[1]

    print(listToSExpression(listString))
