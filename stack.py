class Stack():
    def __init__(self):
        self.stack=None
        self.HEAD=0
    def push(self,value):
        if self.stack is None:
            self.stack=[]
            self.stack.append(value)
        else:
            self.stack.append(0)
            for i in range(len(self.stack)-1,self.HEAD,-1):
            
                self.stack[i]=self.stack[i-1]
            self.stack[0]=value

    def print_stack(self):
        for i in range(len(self.stack)):
            print(f"The {i+1}'th value is {self.stack[i]}")
    def pop(self):
        val=self.stack[0]
        for i in range(0,len(self.stack)-1):
            self.stack[i]=self.stack[i+1]
        del self.stack[-1]
        return val
    def peek(self):
        return self.stack[0]
    def is_empty(self):
        if self.stack is None :
            return True
        return False