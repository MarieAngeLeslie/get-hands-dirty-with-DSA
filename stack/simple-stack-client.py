from simpleStack import *

stack = Stack(10)
for word in ["May", "the", "force", "be", "with", "you"]:
    if not stack.isFull():
        stack.push(word)
    else:
        print("Can’t insert, stack is full")

print("After pushing", len(stack), "words on the stack, it contains:\n", stack)
print("Is stack full?", stack.isFull())
print("Is stack empty?", stack.isEmpty())
print("Popping items off the stack:")
while not stack.isEmpty():
    print(stack.pop(), end=" ")
print()
print("Is stack empty?", stack.isEmpty())
