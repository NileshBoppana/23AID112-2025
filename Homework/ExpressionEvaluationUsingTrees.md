
### Expression Evaluation Using Trees

## Introduction
Expression Trees are binary trees used to represent mathematical expressions.
* Leaves → Operands (numbers/variables)
* Internal nodes → Operators (+, -, *, /)

⸻

## Why Use Expression Trees?
	•	Easy evaluation of expressions
	•	Supports different notations:
        •	Infix
        •	Prefix
        •	Postfix
	•	Useful in:
        •	Compilers
        •	Calculators
        •	Parsing systems

⸻

## Structure of Expression Tree
Example Expression:

(3 + 5) * 2

Tree Representation:

        *
       / \
      +   2
     / \
    3   5


⸻

## Types of Traversals
|Traversal	|Output Form|
| --------- | --------- |
|Inorder	|Infix      |
|Preorder	|Prefix     |
|Postorder	|Postfix    |


⸻

## Building Expression Tree (From Postfix)
Example:

Postfix: 3 5 + 2 *

# Steps:
1. Read expression left → right  
2. If operand → push to stack  
3. If operator:
   - Pop 2 elements  
   - Create node  
   - Push back to stack  

⸻

## Algorithm (Pseudo Code)

```python
for each symbol in postfix:
    if operand:
        push node to stack
    else:
        right = pop()
        left = pop()
        create new node(operator)
        node.left = left
        node.right = right
        push node

return stack top
```

⸻

## Expression Evaluation
# Rule:
- Evaluate Left subtree  
- Evaluate Right subtree  
- Apply operator  

⸻

## Example Evaluation
```
Expression:

(3 + 5) * 2

Steps:

3 + 5 = 8
8 * 2 = 16
```

⸻

## Code Example (Python)
```python
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def evaluate(root):
    if root is None:
        return 0
    
    # If leaf node (operand)
    if root.left is None and root.right is None:
        return int(root.value)
    
    left_val = evaluate(root.left)
    right_val = evaluate(root.right)
    
    if root.value == '+':
        return left_val + right_val
    if root.value == '-':
        return left_val - right_val
    if root.value == '*':
        return left_val * right_val
    if root.value == '/':
        return left_val / right_val
```

⸻

## Advantages
	•	Clear structure of expressions
	•	Easy recursive evaluation
	•	Supports complex expressions

⸻

## Disadvantages
	•	Requires extra memory
	•	Tree construction overhead

⸻

## Conclusion
Expression trees provide an efficient and structured way to:
- Represent expressions
- Convert between notations
- Evaluate expressions easily using recursion

⸻

### Thank You

⸻
