import sys


def getIdentifierStartingAtIndex(sExpressionString: str, startIndex):
    result = ""
    i = startIndex
    while not sExpressionString[i].isspace() and sExpressionString[i] not in {"(", ")", "."}:
        result += sExpressionString[i]
        i += 1

    return [result, i]


def getFirstListItem(sExpressionString):
    if sExpressionString[0] != "(":
        return getIdentifierStartingAtIndex(sExpressionString, 0)

    countUnclosedParens = 1
    i = 1

    while countUnclosedParens:
        if sExpressionString[i] == "(":
            countUnclosedParens += 1
        elif sExpressionString[i] == ")":
            countUnclosedParens -= 1

        i += 1

    return [sExpressionString[0: i], i]


def buildListItems(fullSExpressionString):
    listItems = []

    sExpressionString: str = fullSExpressionString[1:]
    while len(sExpressionString):
        [listItem, i] = getFirstListItem(sExpressionString)
        if (listItem):
            listItems.append(listItem)

        listItemLength = len(listItem)
        sExpressionString = sExpressionString[listItemLength + 2:]

    return [listItem for listItem in listItems if listItem != ")"]


def isList(listItem):
    return listItem[0] == "(" and ".()" in listItem


def buildList(listItems):
    listString = "("

    for listItem in listItems:
        if isList(listItem):
            listString += sExpressionToList(listItem)
        else:
            listString += listItem
        listString += " "

    listString = listString.strip()
    listString += ")"
    return listString


def sExpressionToList(sExpressionString):
    sExpressionString = sExpressionString.replace(" ", "")

    return buildList(buildListItems(sExpressionString))


if __name__ == "__main__":
    if (len(sys.argv) < 2):
        print("Usage: python3 " + sys.argv[0] + " S-Expression")
        sys.exit(1)

    sExpressionString = sys.argv[1]

    print(sExpressionToList(sExpressionString))
