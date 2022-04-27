import unittest
from listToSExpression import listToSExpression
from sExpressionToList import sExpressionToList


class TestListToSExpression(unittest.TestCase):
    def testOne(self):
        listString = "( (3 . 4) 5 ) "
        self.assertEqual(listToSExpression(listString),
                         "( (3 . 4) . (5 . ( ) ) )".replace(" ", ""))

    def testTwo(self):
        listString = "( (3) (4) 5 ) "
        self.assertEqual(listToSExpression(
            listString), "( (3 . ( )) . ( (4 . ( )) . (5 . ( ))))".replace(" ", ""))

    def testThree(self):
        listString = "(A B C) "
        self.assertEqual(listToSExpression(listString),
                         "(A . (B . (C . ())))".replace(" ", ""))

    def testFour(self):
        listString = "((A B) C) "
        self.assertEqual(listToSExpression(listString),
                         "((A . (B . ())) . (C . ()))".replace(" ", ""))

    def testFive(self):
        listString = "(A B (C D)) "
        self.assertEqual(listToSExpression(listString),
                         "(A . (B . ((C . (D . ())) . ())))".replace(" ", ""))

    def testSix(self):
        listString = "((A))"
        self.assertEqual(listToSExpression(listString),
                         "((A . ()) . ())".replace(" ", ""))

    def testSeven(self):
        listString = "(A (B . C))"
        self.assertEqual(listToSExpression(listString),
                         "(A . ((B . C) . ()))".replace(" ", ""))


class TestSExpressionToList(unittest.TestCase):
    def testOne(self):
        sExpressionString = "( (3 . 4) . (5 . ( ) ) )"
        self.assertEqual(sExpressionToList(sExpressionString).replace(
            " ", ""), "( (3 . 4) 5 ) ".replace(" ", ""))

    def testTwo(self):
        sExpressionString = "( (3 . ( )) . ( (4 . ( )) . (5 . ( ))))"
        self.assertEqual(sExpressionToList(sExpressionString).replace(
            " ", ""), "( (3) (4) 5 ) ".replace(" ", ""))

    def testThree(self):
        sExpressionString = "(A . (B . (C . ())))"
        self.assertEqual(sExpressionToList(sExpressionString).replace(
            " ", ""), "(A B C)".replace(" ", ""))

    def testFour(self):
        sExpressionString = "((A . (B . ())) . (C . ()))"
        self.assertEqual(sExpressionToList(sExpressionString).replace(
            " ", ""), "((A B) C)".replace(" ", ""))

    def testFive(self):
        sExpressionString = "(A . (B . ((C . (D . ())) . ())))"
        self.assertEqual(sExpressionToList(sExpressionString).replace(
            " ", ""), "(A B (C D))".replace(" ", ""))

    def testSix(self):
        sExpressionString = "((A.()).())"
        self.assertEqual(sExpressionToList(sExpressionString).replace(
            " ", ""), "((A))".replace(" ", ""))

    def testSeven(self):
        sExpressionString = "(A.((B.C).()))"
        self.assertEqual(sExpressionToList(sExpressionString).replace(
            " ", ""), "(A (B.C))".replace(" ", ""))


if __name__ == '__main__':
    unittest.main()
