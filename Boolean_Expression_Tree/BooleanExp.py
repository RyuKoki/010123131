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

# expression = '((I0+!I1+!(I2))&(!I0+I1+I2))'
# split_exp = SplitBooleanExp()
# print(split_exp.Spoolex(expression))

class ExpTree(SplitBooleanExp):

    def __init__(self):
        super().__init__()
        self.tree = ['']*50

    def delOuterBrac(self, exp_list):
        load = []
        for i in range(len(exp_list)):
            if  self.isOpenPar(exp_list[i]):
                load.append(exp_list[i])
            elif self.isClosePar(exp_list[i]):
                if len(load) > 1:
                    load.pop()
                elif len(load) == 1 and i == len(exp_list)-1:
                    return(exp_list[1:-1])
        return exp_list
   
    def Tree(self, exp_list, index_root):
        left = None
        right = None
        root = None
        open_brac = []
        close_brac = []

        exp_list = self.delOuterBrac(exp_list)
        
        for i in range(len(exp_list)):

            if self.isOpenPar(exp_list[i]):
                open_brac.append(exp_list[i])

            elif self.isClosePar(exp_list[i]):
                close_brac.append(exp_list[i])

            elif self.isOperator(exp_list[i]):
                if exp_list[i] == '&' or exp_list[i] == '+':
                    if len(open_brac) == len(close_brac):
                        root = exp_list[i]
                        left = exp_list[:i]
                        right = exp_list[i+1:]
                        open_brac.clear()
                        close_brac.clear()

                elif exp_list[i] == '!':
                    root = exp_list[i]
                    left = exp_list[i+1:]
                    right = None

        index_left = (2*index_root)+1
        index_right = (2*index_root)+2

        self.tree[index_root] = root
        self.tree[index_left] = left
        self.tree[index_right] = right

        print(f'test:{exp_list} \nleft: {left} \nroot: {root} \nright: {right}')

exp_tree = ExpTree()
exp_input = '((I0+!I1+!(I2))&(!I0+I1+I2))'
exp_tree.Tree(exp_input, 0)

# There are some error! (ToT)
# I will do it more. But now, i'm losing all enthusiasm.
# New code will be soon.
