class SplitString: # ExpMange stands for 'Expression Management'

    def __init__(self):
        self.result = []
        self.load = ''

    def operator(self, e): # e is 'element'
        # method for checking 'Is "e" is operator?'
        operators = '+&!'
        return e in operators

    def operand(self, e): 
        return e.isalpha() or e.isdigit()

    def open_bracket(self, e):
        return e == '('

    def close_bracket(self, e):
        return e == ')'

    def split_expression(self, exp):
        # this method for spliting all expression into list()
        # always make input 'exp' into string
        exp_input = str(exp)
        exp_input = exp_input.replace(" ", "") # for covering when user type 'space bar'

        for i in exp_input: # access each element from 'exp'

            if self.operator(i) or self.open_bracket(i) or self.close_bracket(i):
                # if element 'i' is operator (isOperator == True),
                # or element 'i' is parentheses (isParenth == True), 
                # output is result list() that appends it
                self.result.append(i)

            elif self.operand(i):
                # if element 'i' is operand (isOperand == True), 
                # load string keeps it until finding operator
                self.load += i
                # checking 'Is next of operand 'i' is operator or parantheses
                check_next_i = exp_input[exp_input.index(i)+1]
                if self.operator(check_next_i) or self.open_bracket(check_next_i) or self.close_bracket(check_next_i):
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
        self.tree = ['']*50

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
            elif exp_list[0] == '!':
                return exp_list

        return exp_list

    def Tree(self, exp): 
        # exp stands for 'expression' into list()
        open_brac = []
        huge_op = []

        root = None
        left = None
        right = None

        # use 'delOuterBrac' for delete outer brac
        new_exp = self.delOuterBrac(exp)

        # initial boolean values for some checking
        check = True

        # access all elements in expression
        for i in range(len(new_exp)):
            
            # part 1 : part of checking couple parentheses
            if self.isOpenPar(new_exp[i]): # check open parenthese
                open_brac.append(i)
                # print(open_brac)
                # change check to False for blocking to check part 2
                check = False

            elif self.isClosePar(new_exp[i]): # check close parenthese
                if len(open_brac) > 1:
                    # check this close bracket 
                    # if it's not lasting couple
                    # pop lasting open bracket (open_brac)
                    open_brac.pop()
                    # print(open_brac)
                elif len(open_brac) == 1:
                    # if it's lasting bracket
                    # pop final open bracket
                    open_brac.pop()
                    # print(open_brac)
                    check = True

            # part 2 : checking what's an operator that is outside the couple
            elif new_exp[i] in '&+': # checking 'OR' or 'AND' element
                if check == True: # if finish checking couple parentheses (part 1)
                    huge_op.append(i) # for using to check 'NOT' element
                    root = new_exp[i] # make root is 'OR' or 'AND' element
                    left = new_exp[:i] # make left child from index 0 to before index_end
                    right = new_exp[i+1:] # make right child
                    # print(root, left, right)

            elif new_exp[i] == '!': # checking 'NOT' element
                if check == True: # if finish checking from part 1
                    if len(huge_op) == 0: # if don't have any 'OR' or 'AND' element
                        root = new_exp[i] # make root is 'NOT'
                        left = new_exp[i+1:] # make left child of root is all elements after 'NOT'
                        right = None

                elif len(huge_op) > 0: # if outside of finish couples parentheses has 'OR' or 'AND'
                    pass # using checking 'OR' or 'AND' element instead

        print('root : ', root)
        print('left : ', left)
        print('right : ', right)

        # adding root, left and right in to tree list for using drawing
        index_root = 0 # initial index of beginning of root at 0
        index_left = (2*index_root)+1
        index_right = (2*index_root)+2

        self.tree[index_root] = root
        self.tree[index_left] = left
        self.tree[index_right] = right

        # part 3 : recursive all branches of tree
        # if len(left) > 1:
            # to be continue
            


exp_tree = ExpTree()
# exp_input = "!(1+0)"
# exp_input = "!(!(0+I0&1))"
# exp_input = "(I0+!I1+!(I2))&(!I0+I1+I2)"
# exp_input = "!(I0&I1)+!(I1+I2)"
# exp_input = "(((I0&I1&!I2)+!I1)+I3)"
# exp_input = "(I1+I0)"
print(exp_input)
print('**********************************************************')
split = exp_tree.spoolExp(exp_input)
print(split)
print('**********************************************************')
exp_tree.Tree(split)