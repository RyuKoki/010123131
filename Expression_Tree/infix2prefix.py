class Prefix:

    def __init__(self):
        self.stack = ''
        self.result = []

    def isOperator(self, e): # e = element
        return (e == '&') or (e == '+') or (e == '!')
        # '& = AND, '+' = OR, '!' = NOT

    def isOperand(self, e): 
        operands = 'I0123456789'
        return e in operands

    def openParenth(self, e):
        return (e == '(')

    def closeParenth(self, e):
        return (e == ')')

    def infix2prefix(self, infix):

        for i in infix:
            if self.openParenth(i):
                continue

            elif self.isOperator(i):
                self.result.append(i)
                if len(self.stack) > 0:
                    self.result.append(self.stack)
                    self.stack = ''

            elif self.isOperand(i):
                self.stack += i

            elif self.closeParenth(i):
                if len(self.stack) > 0:
                    self.result.append(self.stack)
                    self.stack = ''

        print(self.result)

prefix = Prefix()
infix = "!(!(0+I0&1))"
prefix.infix2prefix(infix)
