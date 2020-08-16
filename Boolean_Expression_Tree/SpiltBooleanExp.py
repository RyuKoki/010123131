# SplitBoolenaExp for spliting expression
class SplitBooleanExp:

    def __init__(self): # exp is 'expression'
        self.exp = None
        self.load = ''
        self.result = []

    def isOperator(self, e): # e is 'element'
        # method for checking 'Is "e" is operator?'
        operators = '+&!'
        return e in operators

    def isOperand(self, e): 
        operands = 'I0I1I2I3I4I5I6I7I8I9'
        return e in operands

    def isParenth(self, e):
        parentheses = '()'
        return e in parentheses

    def isOpenPar(self, e):
        return e == '('

    def isClosePar(self, e):
        return e == ')'

    def Spoolex(self, exp): # Spoolex stands for 'Split Boolean Expression'
        # this method for spliting all expression into list()
        self.exp = str(exp) # always make input 'exp' into string

        exp_input = self.exp
        exp_input = exp_input.replace(" ", "") # for covering when user type 'space bar'

        for i in exp_input: # access each element from 'exp'

            if self.isOperator(i) or self.isParenth(i):
                # if element 'i' is operator (isOperator == True),
                # or element 'i' is parentheses (isParenth == True), 
                # output is result list() that appends it
                self.result.append(i)

            elif self.isOperand(i):
                # if element 'i' is operand (isOperand == True), 
                # load string keeps it until finding operator
                self.load += i
                # checking 'Is next of operand 'i' is operator or parantheses
                check_next_i = exp_input[exp_input.index(i)+1]
                if self.isOperator(check_next_i) or self.isParenth(check_next_i):
                    # if next of operand 'i' is operator or parantheses
                    # result list() keeps load
                    self.result.append(self.load)
                    # then make load empty
                    self.load = ''

        return self.result

expression = '((I0+!I1+!(I2))&(!I0+I1+I2))'
split_exp = SplitBooleanExp()
print(split_exp.Spoolex(expression))
