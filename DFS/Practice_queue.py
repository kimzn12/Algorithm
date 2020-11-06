from collections import deque

q = deque()

q.append(1)
q.append(2)
q.append(3)
q.append(4)
q.popleft()
q.append('A')

print(q)
q.reverse()
print(q)

# deque([2, 3, 4, 'A'])
# deque(['A', 4, 3, 2])
