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

    def testMultipleCharacterAtoms(self):
        listString = "(s1 s2 s3 jason)"
        self.assertEqual(listToSExpression(listString),
                         "(s1.(s2.(s3.(jason.()))))")

    def testWackyWhitespace(self):
        listString = "    (A    BC   C   )   "
        self.assertEqual(listToSExpression(listString), "(A.(BC.(C.())))")

    def testWackyWhitespace2(self):
        listString = "    (A    (   BC D   )   C   )   "
        self.assertEqual(listToSExpression(listString),
                         "(A.((BC.(D.())).(C.())))")


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

    def testMultipleCharacterAtoms(self):
        sExpressionString = "(s1.(s2.(s3.(jason.()))))"
        self.assertEqual(sExpressionToList(sExpressionString),
                         "(s1 s2 s3 jason)")

    def testWackyWhitespace(self):
        sExpressionString = " (   A  .  (  B C . ( C . ( ) ) )   )    "
        expectedListString = "(A BC C)"
        self.assertEqual(sExpressionToList(
            sExpressionString), expectedListString)

    def testWackyWhitespace2(self):
        sExpressionString = "           ( A . ((     BC.   (D .   ( ) ) ).  (  C. ( )       ) ) )  "
        listStringExpected = "(A (BC D) C)"
        self.assertEqual(sExpressionToList(
            sExpressionString), listStringExpected)


if __name__ == '__main__':
    unittest.main()
