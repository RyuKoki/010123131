class BooleanTree:

    def __init__(self):
        self.tree = ['']*50

    def enter_expression(self, expression):

        count_open_brac = [] # list for counting open bracket(s)
    
        # access for all elements in expression
        for i in range(len(expression)):
            if expression[i] == '(':
                # if finding '(' (open bracket), loading for checking couple(s) of brackets
                count_open_brac.append(expression[i])

            elif expression[i] == ')':
                # if finding ')' (close bracket), pop() lastest open bracket
                # you'll know which lastest couple of brackets
                if len(count_open_brac) > 1:
                    # then this couple of brackets is not lastest couple
                    count_open_brac.pop()
                elif len(count_open_brac) == 1 and i == len(expression)-1:
                    # then this close bracket is the lastest bracket
                    # so open bracket which it is its couple, it is the lastest couple
                    return expression[1:-1] # return expression in the lastest couple of bracket
        
            elif expression[0] == '!': # if first element is 'NOT'
                # return original expression
                return expression

        return expression

    def create_tree(self, expression, index_root=0):
        open_brac = []
        huge_opertor = []

        new_exp = self.enter_expression(expression)

        root = ''
        left = ''
        right = ''

        check = True

        for i in range(len(new_exp)):

            if new_exp[i] == '(':
                open_brac.append(i)
                check = False

            elif new_exp[i] == ')':
                if len(open_brac) > 1:
                    open_brac.pop()
                elif len(open_brac) == 1:
                    open_brac.pop()
                    check = True

            elif new_exp[i] in '&+':
                if check == True:
                    huge_opertor.append(i)
                    root = new_exp[i]
                    left = new_exp[:i]
                    right = new_exp[i+1:]

            elif new_exp[i] == '!':
                if check == True:
                    if len(huge_opertor) == 0:
                        root = new_exp[i]
                        left = new_exp[i+1:]
                        right = ''
                    elif len(huge_opertor) > 0:
                        pass

        index_left = (2*index_root)+1
        index_right = (2*index_root)+2

        self.tree[index_root] = root
        self.tree[index_left] = left
        self.tree[index_right] = right

        if len(left) > 1:
            self.create_tree(left, index_left)

        elif len(left) == 1:
            self.tree[index_left] = left[0]
            if len(right) > 1:
                self.create_tree(right, index_right)
            elif len(right) == 1:
                self.tree[index_right] = right[0]

        if len(right) > 1:
            self.create_tree(right, index_right)
        elif len(right) == 1:
            self.tree[index_right] = right[0]

        return self.tree

from splitstring import SplitString
split_exp = SplitString()
boolean_tree = BooleanTree()
# exp_input = "!(1+0)"
# exp_input = "!(!(0+I0&1))"
# exp_input = "(I0+!I1+!(I2))&(!I0+I1+I2)"
exp_input = "!(I0&I1)+!(I1+I2)"
# exp_input = "(((I0&I1&!I2)+!I1)+I3)"
# exp_input = "(I1+I0)"
print('Expression : ', exp_input)
print('', '*'*50)
exp = split_exp.split_string(exp_input)
output = boolean_tree.create_tree(exp, 0)
print(output)
