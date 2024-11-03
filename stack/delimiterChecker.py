from simpleStack import *

stack = Stack(100)

expr = input("Enter the expression you want to check : ")

errors = 0

for pos, letter in enumerate(expr):
    if letter in "({[":
        if not stack.isFull():
            stack.push(letter)
        else:
            raise Exception("Stack overflow on stack")

    elif letter in ")}]":
        if stack.isEmpty():
            print("Error:", letter, "at position", pos, "doesn't macth any delimiter")
            errors += 1
        else:
            left = stack.pop()
            if not (
                left == "("
                and letter == ")"
                or left == "{"
                and letter == "}"
                or left == "["
                and letter == "]"
            ):
                print(
                    "Error:", letter, "at position", pos, "doesn't macth any delimiter"
                )
                errors += 1

if stack.isEmpty() and errors == 0:
    print("Delimiters balance in expression", expr)
elif not stack.isEmpty():
    print("Expression missing right delimiters for", stack)
