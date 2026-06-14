class MinStack:
    def __init__(self):
        self.stack = []
        self.min_val = float('inf')
        self.minstack = []
    
    def push(self , val:int)-> None:
        self.stack.append(val)
        
        if not self.minstack:
            self.minstack.append(val)
        else:
            if self.minstack[-1] > val:
                self.minstack.append(val)
            else:
                self.minstack.append(self.minstack[-1])
        
    
    def pop(self)-> None:
    
        self.minstack.pop()
        self.stack.pop()
    
    def top(self)-> int:
        print( self.stack[-1])

        return self.stack[-1]
    
    def getMin(self) -> int:
        print(self.minstack[-1])
        return self.minstack[-1]