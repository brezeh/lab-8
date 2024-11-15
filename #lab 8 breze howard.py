#lab 8 breze howard

#program 1
#Define the stack class
class Stack():
    def __init__(self):
        self.items = [] #initialize an empty list to store stack items

    #return True if the stack is empty, otherwise False
    def is_empty(self):
        return len(self.items) == 0
    
    #add an item to the top of the stack
    def push(self, item):
        self.items.append(item) 

    #remove and return the top item from the stack if it's not empty
    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        return None  #if the stack is empty, return None
    
    #return the top item without removing it if the stack is not empty
    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        return None #if the stack is empty, return None
    
#create a stack to keep track of opening parentheses
def is_balanced(expression):
    stack = Stack()

    #define matching pairs for parentheses
    opening = "({["
    closing = ")}]"
    matches = {')': '(', '}': '{', ']': '['}

    #loop through each character in the expression
    for char in expression:
        if char in opening:
            stack.push(char) #check if the character is an opening parenthesis

    #check if the character is a closing parenthesis
        elif char in closing:
            if stack.is_empty() or stack.pop() != matches[char]:
                return False #if the stack is empty or top of the stack doesn't match the closing parenthesis, return False
                
    #if stack is empty, all parentheses were matched; otherwise, return False
    return stack.is_empty()
    
#test cases
expression1 = "({X+Y}*Z)"
expression2 = "{X+Y}*Z)"
expression3 = "({X+Y}*Z"
expression4 = "[A+B]*({X+Y}]*Z)"

#expected output: True, False, False, False respectively
print(is_balanced(expression1))
print(is_balanced(expression2))
print(is_balanced(expression3))
print(is_balanced(expression4))

#program 2
#Define the stack class
class Stack():
    def __init__(self):
        self.items = [] #initialize an empty list to store stack items

    #return True if the stack is empty, otherwise False
    def is_empty(self):
        return len(self.items) == 0
    
    #add an item to the top of the stack
    def push(self, item):
        self.items.append(item) 

    #remove and return the top item from the stack if it's not empty
    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        return None  #if the stack is empty, return None
    
    #return the top item without removing it if the stack is not empty
    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        return None #if the stack is empty, return None
    
#initialize two stacks: one for numbers and one for operators
def evaluate_expression(expression):
    num_stack = Stack()  # Stack for numbers
    op_stack = Stack()   # Stack for operators

    #helper function to apply an operator to the top two numbers on num_stack
    def apply_operator():
        #pop the top operator from op_stack
        operator = op_stack.pop()
        #pop the top two numbers from num_stack
        right = num_stack.pop()
        left = num_stack.pop()

        #perform the operation and push the result back to num_stack
        if operator == '+':
            num_stack.push(left + right)
        elif operator == '-':
            num_stack.push(left - right)
        elif operator == '*':
            num_stack.push(left * right)
        elif operator == '/':
            num_stack.push(left / right)

    #loop through each character in the expression
    i = 0
    while i < len(expression):
        char = expression[i]

        #ignore whitespace characters
        if char == ' ':
            i += 1
            continue

        #check if the character is a digit
        if char.isdigit():
            #pass the entire number and push it to num_stack
            num = 0
            while i < len(expression) and expression[i].isdigit():
                num = num * 10 + int(expression[i])
                i += 1
            num_stack.push(num)
            continue

        #check if the character is an opening parenthesis '('
        elif char == '(':
            op_stack.push(char) #push '(' to op_stack to mark the start of a group

        #check if the character is a closing parenthesis ')'
        elif char == ')':
            #pop and apply operators until '(' is found
            while not op_stack.is_empty() and op_stack.peek() != '(':
                apply_operator()
            op_stack.pop()  #pop '(' from the stack

        #if it's an operator (+, -, *, /)
        elif char in "+-*/":
            #apply operators based on precedence, then push current operator to op_stack
            while (not op_stack.is_empty() and
                   (op_stack.peek() in "+-*/") and
                   ((char in "+-" and op_stack.peek() in "+-") or
                    (char in "*/" and op_stack.peek() in "*/") or
                    (char in "+-" and op_stack.peek() in "*/"))):
                apply_operator()
            op_stack.push(char)

        #move to the next character
        i += 1

    #after the loop, apply any remaining operators in op_stack
    while not op_stack.is_empty():
        apply_operator()

    #return the final result from num_stack
    return num_stack.pop()

#test cases
expression1 = "(((6+9)/3)*(6-4))"
expression2 = "10 + (2 * (6 + 4))"
expression3 = "100 * (2 + 12) / 4"

#expected output: 10, 30, 350 respectively
print(evaluate_expression(expression1))
print(evaluate_expression(expression2))
print(evaluate_expression(expression3))