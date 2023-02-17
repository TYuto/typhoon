import unittest
from ast_node import ValueExp, ExpPlus, ExpMinus, ExpMulti, ExpDiv, ExpAnd, ExpOr, ExpGt, ExpIf, SentencesExp, AssignExp, VariableExp, WhileExp, PrintExp, FuncCallExp, FuncDefExp

class AstNodeTest(unittest.TestCase):
    def test_exp_plus(self):
        self.assertEqual(ExpPlus(ValueExp(12), ValueExp(34)).evaluate({}), 46)

    def test_exp_minus(self):
        self.assertEqual(ExpMinus(ValueExp(12), ValueExp(34)).evaluate({}), -22)

    def test_exp_multi(self):
        self.assertEqual(ExpMulti(ValueExp(12), ValueExp(34)).evaluate({}), 408)

    def test_exp_div(self):
        self.assertEqual(ExpDiv(ValueExp(40), ValueExp(4)).evaluate({}), 10)
    
    def test_exp_and(self):
        self.assertEqual(ExpAnd(ValueExp(1), ValueExp(1)).evaluate({}), 1)
        self.assertEqual(ExpAnd(ValueExp(0), ValueExp(1)).evaluate({}), 0)
        self.assertEqual(ExpAnd(ValueExp(1), ValueExp(0)).evaluate({}), 0)
        self.assertEqual(ExpAnd(ValueExp(0), ValueExp(0)).evaluate({}), 0)

    def test_exp_and(self):
        self.assertEqual(ExpOr(ValueExp(1), ValueExp(1)).evaluate({}), 1)
        self.assertEqual(ExpOr(ValueExp(0), ValueExp(1)).evaluate({}), 1)
        self.assertEqual(ExpOr(ValueExp(1), ValueExp(0)).evaluate({}), 1)
        self.assertEqual(ExpOr(ValueExp(0), ValueExp(0)).evaluate({}), 0)
    
    def test_exp_gt(self):
        self.assertEqual(ExpGt(ValueExp(10), ValueExp(9)).evaluate({}), 1)
        self.assertEqual(ExpGt(ValueExp(10), ValueExp(10)).evaluate({}), 0)
        self.assertEqual(ExpGt(ValueExp(10), ValueExp(11)).evaluate({}), 0)
    
    def test_exp_if(self):
        self.assertEqual(ExpIf(ValueExp(1), ValueExp(2), ValueExp(3)).evaluate({}), 2)
        self.assertEqual(ExpIf(ValueExp(0), ValueExp(2), ValueExp(3)).evaluate({}), 3)

class SentencesTest(unittest.TestCase):
    def test_sentences(self):
        self.assertEqual(SentencesExp([ValueExp(1), ValueExp(2), ValueExp(3)]).evaluate({}), 3)
    
    def test_assign(self):
        self.assertEqual(SentencesExp([
            AssignExp('A', ValueExp(12)),
            AssignExp('B', ValueExp(34)),
            ExpPlus(VariableExp('A'), VariableExp('B'))
        ]).evaluate({}), 46)
    
    def test_while(self):
        self.assertEqual(
            SentencesExp([
                AssignExp('I', ValueExp(0)),
                WhileExp(
                    ExpGt(ValueExp(10), VariableExp('I')),
                    AssignExp('I', ExpPlus(VariableExp('I'), ValueExp(1)))
                ),
                VariableExp('I')
            ]).evaluate({})
        , 10)
    
    def test_func(self):
        self.assertEqual(
            SentencesExp([
                FuncDefExp('plusten', ExpPlus(VariableExp('v'), ValueExp(10)), ['v']),
                AssignExp('r', ValueExp(0)),
                AssignExp('r', FuncCallExp('plusten', [VariableExp('r')])),
                AssignExp('r', FuncCallExp('plusten', [VariableExp('r')])),
                VariableExp('r')
            ]).evaluate({})
        , 20)
 
if __name__ == '__main__':
    unittest.main()
