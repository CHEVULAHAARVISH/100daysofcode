#we are filling stack using put method

# using queue module


from queue import LifoQueue

# Initializing a stack
stack = LifoQueue(maxsize = 10)

# qsize() show the number of elements
# in the stack
print(stack.qsize())

# put() function to push
# element in the stack
stack.put('H')
stack.put('A')
stack.put('A')
stack.put('R')
stack.put('V')
stack.put('I')
stack.put('S')
stack.put('H')
#checking wheather elements are filled or not
print("Full: ", stack.full())
print("Size: ", stack.qsize())
