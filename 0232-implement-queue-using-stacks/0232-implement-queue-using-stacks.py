class MyQueue(object):

    def __init__(self):
        self.inn = [] 
        self.out = [] 
    def push(self, x):
        self.inn.append(x)         
    def pop(self):
        if len(self.out) == 0:
            while len(self.inn):
                self.out.append(self.inn.pop()) 
        return self.out.pop()
    def peek(self):
        if len(self.out) == 0:
            while len(self.inn):
                self.out.append(self.inn.pop())
        return self.out[len(self.out)-1]
    def empty(self):
        return len(self.inn) == 0 and len(self.out) == 0
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()