from collections import deque

class Stack:
   def __init__(self):
       self.q1 = deque()
       self.q2 = deque()

   def pop(self):
       if self.empty():
           return None
       return self.q1.popleft()

   def top(self):
       if self.empty():
           return None
       return self.q1[0]

   def empty(self):
       return len(self.q1) == 0

   def push(self,x):
       self.q2.append(x)
       #Step 1:Put new element in q2
       #Step 2:Move all elements from q1 to q2
       #Step 3:Swap q1 and q2
       while self.q1:
           self.q2.append(self.q1.popleft())
           self.q1, self.q2 = self.q2, self.q1

sol = Stack()
sol.push(1)
sol.push(2)
sol.push(3)
print(sol.top())
print(sol.pop())
print(sol.top())