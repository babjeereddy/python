from collections import deque

queue = deque()
queue.append(1)      # Enqueue
queue.append(2)
queue.append(3)
print(queue.popleft())  # Dequeue (1)
print(queue)            # deque([2, 3])
