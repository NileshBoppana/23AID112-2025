def evaluate_postfix(expression):
    stack = []

    for token in expression.split():

        # If operand (number or boolean)
        if token.isdigit():
            stack.append(int(token))

        elif token in ['True', 'False']:
            stack.append(token == 'True')

        else:
            # Unary operator (only for NOT)
            if token == 'not':
                a = stack.pop()
                stack.append(not a)
                continue

            # Binary operators
            b = stack.pop()
            a = stack.pop()

            # Arithmetic operators
            if token == '+':
                stack.append(a + b)
            elif token == '-':
                stack.append(a - b)
            elif token == '*':
                stack.append(a * b)
            elif token == '/':
                stack.append(a // b)

            # Comparison operators
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

            # Logical operators
            elif token == 'and':
                stack.append(a and b)
            elif token == 'or':
                stack.append(a or b)

    return stack.pop()


# Example expressions
expr1 = "2 3 * 5 4 * + 9 -"          # arithmetic
expr2 = "5 3 >"                      # comparison
expr3 = "5 3 > 2 1 < and"            # logical
expr4 = "True False or"              # boolean
expr5 = "5 3 > not"                  # unary logical

print("Expr1:", evaluate_postfix(expr1))
print("Expr2:", evaluate_postfix(expr2))
print("Expr3:", evaluate_postfix(expr3))
print("Expr4:", evaluate_postfix(expr4))
print("Expr5:", evaluate_postfix(expr5))
