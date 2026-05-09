class MinStack:

    def __init__(self):
        self.stack = []
        self.min1=float('inf')
        self.minstack=[]
        self.minstack.append(self.min1)

    def push(self, val: int) -> None:
        self.stack.append(val)
        if val<=self.min1:
            self.min1=val
            self.minstack.append(self.min1)

    def pop(self) -> None:
        if self.stack[-1]==self.min1:
            self.minstack.pop()
            if self.minstack:
                self.min1=self.minstack[-1]
            else:
                self.min1=float('inf')
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minstack[-1]
        
