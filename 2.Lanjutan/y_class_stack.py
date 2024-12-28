class Stack:
  def __init__(self):
    self.stack = []
  
  def is_empty(self): 
    return True if len(self.stack) == 0 else False
  
  def push(self,item):
    self.stack.append(item)
  
  def get_stack(self): 
    return self.stack
  
  def pop(self):
    return None if self.is_empty() else self.stack.pop()

stack = Stack()
stack.push("X")
stack.pop()
stack.push("Y")

print(stack.get_stack())