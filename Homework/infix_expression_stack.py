# Python program to demonstrate infix expression processing using stack

def precedence(op):
    if op == '+' or op == '-':
        return 1
    elif op == '*' or op == '/':
        return 2
    elif op == '^':
        return 3
    return 0


def infix_to_postfix(expression):
    stack = []
    postfix = []

    for ch in expression:
        if ch.isalnum():   # operand
            postfix.append(ch)

        elif ch == '(':
            stack.append(ch)

        elif ch == ')':
            while stack and stack[-1] != '(':
                postfix.append(stack.pop())
            if stack:
                stack.pop()   # remove '('

        else:   # operator
            while stack and precedence(stack[-1]) >= precedence(ch):
                postfix.append(stack.pop())
            stack.append(ch)

    while stack:
        postfix.append(stack.pop())

    return ''.join(postfix)


def evaluate_postfix(postfix):
    stack = []

    for ch in postfix:
        if ch.isdigit():
            stack.append(int(ch))
        else:
            b = stack.pop()
            a = stack.pop()

            if ch == '+':
                stack.append(a + b)
            elif ch == '-':
                stack.append(a - b)
            elif ch == '*':
                stack.append(a * b)
            elif ch == '/':
                stack.append(a / b)
            elif ch == '^':
                stack.append(a ** b)

    return stack[0]


# Main program
expr = input("Enter infix expression: ")

postfix = infix_to_postfix(expr)
print("Postfix expression:", postfix)

# Postfix evaluation works only if expression contains single-digit numbers
if all(c.isdigit() or c in "+-*/^()" for c in expr):
    result = evaluate_postfix(postfix)
    print("Evaluated result:", result)
else:
    print("Evaluation skipped because expression contains variables.")
