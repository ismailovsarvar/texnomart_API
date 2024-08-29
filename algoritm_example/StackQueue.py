# Stack list
stack = ["Sarvar", "Muslima", "Malika"]
stack.append("Fayz")
stack.append("Ziyo")
print(stack)

# Oxirgi elementni olib tashlash
print(stack.pop())
print(stack)
print(stack.pop())
print(stack)

# Queue list
queue = ["Sarvar", "Muslima", "Malika"]
queue.append("Fayz")
queue.append("Ziyo")
print(queue)

# Birinchi elementni olib tashlash
print(queue.pop(0))
print(queue)
print(queue.pop(0))
print(queue)

# Deque yordamida Stack
from collections import deque

queue = deque(["Sardor", "Sarvar", "Aziz", "Laziz"])
print(queue)
queue.append("Akbar")
print(queue)
queue.append("Bobur")
print(queue)
print(queue.pop())
print(queue.pop())
print(queue)

# Deque yordamida Queue
from collections import deque

queue = deque(["Sardor", "Sarvar", "Aziz", "Laziz"])
print(queue)
queue.append("Akbar")
print(queue)
queue.append("Bobur")
print(queue)
print(queue.popleft())
print(queue.popleft())
print(queue)
