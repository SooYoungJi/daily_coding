stack = []

stack.append(3)
stack.append(5)
stack.append(2)

temp = stack.pop()
print(temp)

temp = stack.pop(0)
print(temp)

stack.append(4)

temp = stack.pop()
print(temp)