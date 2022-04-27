# functional-helpers

Python modules for converting Functional S-Expressions to and from lists, and a binary tree visualization.

## Use

List -> S-Expression:
`python3 listToSExpression.py "(A B (C))"`

S-Expression -> List:
`python3 sExpressionToList.py "(A.(B.((C.()).())))"`

List -> Binary Tree:
`python3 listToBinaryTree.py "(A B (C))"`

S-Expression -> Binary Tree:
`python3 sExpressionToBinaryTree.py "(A.(B.((C.()).())))"`

---

## Left to Be Desired

Right now, the modules do not work for atoms of more than one character. For example, a list of (s1 s2) would not be correctly transformed into an S-Expression.
