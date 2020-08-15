class SplitBooleanExp:

    def __init__(self, exp): # exp is 'expression'
        self.exp = str(exp)
        self.load = ''
        self.result = []

    def isOperator(self, e): # e is 'element'
        operators = '+&!'
        return e in operators

    def isOperand(self, e): 
        operands = 'I0123456789'
        return e in operands

    def isParenth(self, e):
        parentheses = '()'
        return e in parentheses

    def isOpenPar(self, e):
        return e == '('

    def isClosePar(self, e):
        return e == ')'

    def Spoolex(self):

        exp_input = self.exp
        exp_input = exp_input.replace(" ", "")

        for i in exp_input:

            if self.isOperator(i) or self.isParenth(i):
                self.result.append(i)

            elif self.isOperand(i):
                self.load += i
                check_next_i = exp_input[exp_input.index(i)+1]
                if self.isOperator(check_next_i) or self.isParenth(check_next_i):
                    self.result.append(self.load)
                    self.load = ''

        return self.result

# expression = '((I0+!I1+!(I2))&(!I0+I1+I2))'
# split_exp = SplitBooleanExp(expression)
# print(split_exp.Spoolex())

class BooleanTree(SplitBooleanExp):

    def __init__(self, exp):
        super().__init__(exp)
        self.stack = []
        self.tree = None
        self.num_node = 0

    def Tree(self, exp_list):

##### coming soon #####