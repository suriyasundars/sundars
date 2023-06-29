import time
class stack:
    def __init__(self):
        self.items=[]
    def isEmpty(self):
        return (self.items)
    def push(self,item):
        self.items.append(item)
    def pop(self):
        return self.items.pop()
    def peek(self):
        return (self.items[len(self.items)-1])
    def size(self):
        return len(self.items)
    def display(self):
        return self.items
s=stack()
start=time.time()
print(s.isEmpty())
print("push operation")
s.push(11)
s.push(12)
s.push(13)
print("size:",s.size())
print(s.display())
print("peek",s.peek())
print("pop operation")
print(s.pop())
print(s.pop())
print(s.display())
print("size:",s.size())
end=time.time()
print("run time of the program is",end-start)