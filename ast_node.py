
class Exp():
    def evaluate(self, env): 
        print("TODO")
        return 0
    def evaluate_type(self):
        return 'Null'

class ValueExp(Exp):
    def __init__(self, value):
        super().__init__()
        self.value = value
    def evaluate(self, env):
        return self.value

class VariableExp(Exp):
    def __init__(self, name):
        super().__init__()
        self.name = name
    def evaluate(self, env):
        if self.name in env:
            return env[self.name]
        else:
            print("{} is not defined".format(self.name))
            return 0

class BinExp(Exp):
    def __init__(self, left, right):
        super().__init__()
        self.left = left
        self.right = right

class ExpPlus(BinExp):
    def evaluate(self, env):
        return self.left.evaluate(env) + self.right.evaluate(env)

class ExpMinus(BinExp):
    def evaluate(self, env):
        return self.left.evaluate(env) - self.right.evaluate(env)

class ExpDiv(BinExp):
    def evaluate(self, env):
        return self.left.evaluate(env) / self.right.evaluate(env)
    
class ExpMulti(BinExp):
    def evaluate(self, env):
        return self.left.evaluate(env) * self.right.evaluate(env)

class ExpAnd(BinExp):
    def evaluate(self, env):
        if self.left.evaluate(env) == 1 and self.right.evaluate(env) == 1:
            return 1
        else:
            return 0

class ExpOr(BinExp):
    def evaluate(self, env):
        if self.left.evaluate(env) == 1 or self.right.evaluate(env) == 1:
            return 1
        else:
            return 0

class ExpGt(BinExp):
    def evaluate(self, env):
        if self.left.evaluate(env) > self.right.evaluate(env):
            return 1
        else:
            return 0

class ExpIf(Exp):
    def __init__(self, condition, if_exp, then_exp):
        super().__init__()
        self.condition = condition
        self.if_exp = if_exp
        self.then_exp = then_exp
    def evaluate(self, env):
        if(self.condition.evaluate(env) == 1):
            return self.if_exp.evaluate(env)
        else:
            return self.then_exp.evaluate(env)

class AssignExp(Exp):
    def __init__(self, name, value):
        super().__init__()
        self.name = name
        self.value = value
    
    def evaluate(self, env):
        val = self.value.evaluate(env)
        env[self.name] = val
        return val


class SentencesExp(Exp):
    def __init__(self, exps):
        super().__init__()
        self.exps = exps
    def evaluate(self, env):
        val = ''
        for s in self.exps:
            val = s.evaluate(env)
        return val

class PrintExp(Exp):
    def __init__(self, value):
        super().__init__()
        self.value = value
    def evaluate(self, env):
        val = self.value.evaluate(env)
        print("Print Exp Output: {}".format(val))
        return val

class WhileExp(Exp):
    def __init__(self, condition, exp):
        super().__init__()
        self.condition = condition
        self.exp = exp
    def evaluate(self, env):
        val = ''
        while( self.condition.evaluate(env) == 1):
            val = self.exp.evaluate(env)
        return val

class FuncDefExp(Exp):
    def __init__(self, name, exp, variables):
        self.name = name
        self.exp = exp
        self.variables = variables
    def evaluate(self, env):
        env[self.name] = { 'f': self.exp, 'v': self.variables}
        return self.name

class FuncCallExp(Exp):
    def __init__(self, name, variables):
        self.name = name
        self.variables = variables
    def evaluate(self, env):
        f = env[self.name]
        if(len(f['v']) != len(self.variables)):
            print('variables incorrect')
        new_env = env.copy()
        for i in range(len(self.variables)):
            new_env[f['v'][i]] = self.variables[i].evaluate(env)
        value = f['f'].evaluate(new_env)
        for k in env.keys():
            env[k] = new_env[k]
        return value
            

    