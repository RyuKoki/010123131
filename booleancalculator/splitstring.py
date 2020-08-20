class SplitString:

    def __init__(self):
        self.result = []
        self.load = ''

    def operator(self, e): # e is 'element'
        # method for checking 'Is "e" is operator?'
        # '+' stands for 'OR'
        # '&' stands for 'AND'
        # '!' stands for 'NOT'
        operators = '+&!'
        return e in operators

    def operand(self, e): 
        # A - Z or a - z # 0 - 9
        return e.isalpha() or e.isdigit()

    def bracket(self, e):
        return e in '()'

    def split_string(self, exp):
        # this method for spliting all expression into list()
        # always make input 'exp' into string
        exp_input = str(exp)
        exp_input = exp_input.replace(" ", "") # for covering when user type 'space bar'

        for i in exp_input: # access each element from 'exp_input'

            if self.operator(i) or self.bracket(i):
                # if element 'i' is operator or brackets
                # suddenly append result
                self.result.append(i)

            elif self.operand(i):
                # if element 'i' is operand 
                # append load until finding operator or bracket
                self.load += i
                # checking 'Is next of operand 'i' is operator or bracket
                check_next = exp_input[exp_input.index(i)+1]
                if self.operator(check_next) or self.bracket(check_next):
                    # result list() keeps load
                    self.result.append(self.load)
                    # then make load empty
                    self.load = ''

        return self.result

################### T E S T ##################
# split_input = SplitString()
# test_input = "!(1+0)"
# test_input = "!(!(0+I0&1))"
# test_input = "(I0+!I1+!(I2))&(!I0+I1+I2)"
# test_input = "!(I0&I1)+!(I1+I2)"
# test_input = "(((I0&I1&!I2)+!I1)+I3)"
# print(split_input.split_string(test_input))
