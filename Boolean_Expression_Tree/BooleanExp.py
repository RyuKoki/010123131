class ExpManage: # ExpMange stands for 'Expression Management'

    def __init__(self):
        self.result = []
        self.load = ''

    def isOperator(self, e): # e is 'element'
        # method for checking 'Is "e" is operator?'
        operators = '+&!'
        return e in operators

    def isOperand(self, e): 
        # method for checking 'Is "e" is in operand?'
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
        # always make input 'exp' into string
        exp_input = str(exp)
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


class ExpTree(ExpManage): # ExpTree stands for 'Expression Tree'

    # ExpTree is inheritance from ExpManage
    def __init__(self):
        super().__init__()
        self.tree = []*50
        self.left_child = []
        self.right_child = []

    def delOuterBrac(self, exp_list):
        # load list() for counting open and close bracket
        load = []
        # access all elements from exp_list
        for i in range(len(exp_list)):
            if  self.isOpenPar(exp_list[i]):
                # if find open bracket >> append to load list()
                load.append(exp_list[i])
            elif self.isClosePar(exp_list[i]):
                # if find close bracket
                if len(load) > 1:
                    # if open bracket in load list() more than 1
                    # delete last open bracket in load list()
                    load.pop()
                elif len(load) == 1 and i == len(exp_list)-1:
                    # if load list() has only one open bracket and index of the last close bracket
                    # return value of exp_list from index 1 to index -1
                    return(exp_list[1:-1])
        return exp_list

    def Tree(self, exp, root, index_r): 
        # index_r stands for 'index of root'
        # exp stands for 'expression' into list()
        open_brac = []
        exp = self.delOuterBrac(exp)

        CHECK = True
        for i in exp:

            if CHECK:

                if self.isOpenPar(i):
                    open_brac.append(i)
                    index_start = exp.index(i)

                elif self.isClosePar(i):
                    if len(open_brac) > 1:
                        open_brac.pop()
                    elif len(open_brac) == 1:
                        index_end = exp.index(i)
                        open_brac.pop()
                        CHECK = False

            if not CHECK:

                if self.isOperator(i):
                    if (i == '&') or (i == '+'):
                        root = i
                        left = exp[index_start:index_end+1]
                        right = exp[exp.index(i)+1]

                        
                        
                        
                        
exp_tree = ExpTree()
expression = "!(I0&I1)+!(I1+I2)"
split = exp_tree.Spoolex(expression)
print(split)
outer_brac = exp_tree.delOuterBrac(split)
print(outer_brac)

# more code will be coming soon
# Thank you
