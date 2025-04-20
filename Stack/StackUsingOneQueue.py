from collections import deque

class Stack:
   def __init__(self):
       self.q = deque()

   def pop(self):
       if self.empty():
           return None
       return self.q.popleft()

   def top(self):
       if self.empty():
           return None
       return self.q[0]

   def empty(self):
       return len(self.q) == 0

   def push(self,x):
       self.q.append(x)
       # Rotate the queue to make last added element at front
       for _ in range(len(self.q) - 1):
            self.q.append(self.q.popleft())

sol = Stack()
sol.push(1)
sol.push(2)
print(sol.top())
print(sol.pop())
print(sol.empty())