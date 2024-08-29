# Python code to demonstrate Implementing
# stack using list
stack = ["Amar", "Akbar", "Anthony"]
stack.append("Ram")
stack.append("Iqbal")
print(stack)

# Removes the last item
print(stack.pop())

print(stack)

# Removes the last item
print(stack.pop())

print(stack)

# Python code to demonstrate Implementing
# Queue using list
queue = ["Amar", "Akbar", "Anthony"]
queue.append("Ram")
queue.append("Iqbal")
print(queue)

# Removes the first item
print(queue.pop(0))

print(queue)

# Removes the first item
print(queue.pop(0))

print(queue)

# Python code to demonstrate Implementing
# Stack using deque
from collections import deque
queue = deque(["Ram", "Tarun", "Asif", "John"])
print(queue)
queue.append("Akbar")
print(queue)
queue.append("Birbal")
print(queue)
print(queue.pop())
print(queue.pop())
print(queue)

# Python code to demonstrate Implementing
# Queue using deque
from collections import deque
queue = deque(["Ram", "Tarun", "Asif", "John"])
print(queue)
queue.append("Akbar")
print(queue)
queue.append("Birbal")
print(queue)
print(queue.popleft())
print(queue.popleft())
print(queue)
