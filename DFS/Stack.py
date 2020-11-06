stack = []

stack.append(1)
stack.append(2)
stack.append(3)
stack.append(4)
stack.pop()
stack.append('A')
stack.append('B')
stack.pop()

print(stack)
print(stack[::-1]) # 최상단부터 출력