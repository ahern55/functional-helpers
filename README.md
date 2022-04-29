# functional-helpers

Python modules for converting Functional S-Expressions to and from lists, and a binary tree visualization.

## Use

List -> S-Expression:\
`$ python3 listToSExpression.py "(A B (C))"`

S-Expression -> List:\
`$ python3 sExpressionToList.py "(A.(B.((C.()).())))"`

List -> Binary Tree:\
`$ python3 listToBinaryTree.py "(A B (C))"`

S-Expression -> Binary Tree:\
`$ python3 sExpressionToBinaryTree.py "(A.(B.((C.()).())))"`

## Demo

![Screen Shot 2022-04-27 at 7 16 33 PM](https://user-images.githubusercontent.com/61369954/165646598-5e70017f-5405-481a-927f-8b5732409a1b.png)

---

## Left to Be Desired

hacky implementation, more unit tests 🤠
