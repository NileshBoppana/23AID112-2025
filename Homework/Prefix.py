def evaluate_prefix(expression):
    stack = []

    tokens = expression.split()[::-1]

    for token in tokens:

        # Numbers
        if token.isdigit():
            stack.append(int(token))

        # Boolean values
        elif token in ['True', 'False']:
            stack.append(token == 'True')

        else:
            # Unary operator (NOT)
            if token == 'not':
                a = stack.pop()
                stack.append(not a)
                continue

            # Binary operators
            a = stack.pop()
            b = stack.pop()

            # Arithmetic
            if token == '+':
                stack.append(a + b)
            elif token == '-':
                stack.append(a - b)
            elif token == '*':
                stack.append(a * b)
            elif token == '/':
                stack.append(a // b)

            # Comparison
            elif token == '>':
                stack.append(a > b)
            elif token == '<':
                stack.append(a < b)
            elif token == '>=':
                stack.append(a >= b)
            elif token == '<=':
                stack.append(a <= b)
            elif token == '==':
                stack.append(a == b)
            elif token == '!=':
                stack.append(a != b)

            # Logical
            elif token == 'and':
                stack.append(a and b)
            elif token == 'or':
                stack.append(a or b)

    return stack.pop()


# Examples
expr1 = "- + * 2 3 * 5 4 9"           # arithmetic
expr2 = "> 5 3"                       # comparison
expr3 = "and > 5 3 < 2 1"             # logical
expr4 = "or True False"               # boolean
expr5 = "not > 5 3"                   # unary

print("Expr1:", evaluate_prefix(expr1))
print("Expr2:", evaluate_prefix(expr2))
print("Expr3:", evaluate_prefix(expr3))
print("Expr4:", evaluate_prefix(expr4))
print("Expr5:", evaluate_prefix(expr5))
