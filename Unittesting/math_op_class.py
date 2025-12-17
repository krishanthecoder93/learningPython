class Calculate:
    def add_number(self,a,b):
        return a+b
    def sub_number(self,a,b):
        return a-b
    def mul_number(self,a,b):
        return a*b
    def div_number(self,a,b):
        if b==0:
            raise ValueError("Division by zero error")
        return a//b