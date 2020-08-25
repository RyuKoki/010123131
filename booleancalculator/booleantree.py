class BooleanTree:

    def __init__(self):
        self.tree = []

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

    def create_tree(self, expression):
        open_brac = []
        huge_opertor = []

        new_exp = self.enter_expression(expression)

        root = None
        left = None
        right = None

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
                        right = None
                    elif len(huge_opertor) > 0:
                        pass

            