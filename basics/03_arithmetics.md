# Basic Arithemtics Program

This program performs basic mathematic operations, addition, subtraction, multiplication, and division, using **functions** and **conditional statements**.

### Program Overview

1. Define four separate functions for mathematical operations.
2. Takes two numbers as input from the user.
3. Prompts the user to choose an operation.
4. Executes the corresponding function and prints the result.

### Concepts Used

1. **Functions** - Reusable code blocks for specific tasks (addition, subtraction, etc.).
2. **Conditional Statements** - Used to choose which function to execute based on user input.
3. **Type Conversion** - float() is used to handle decimal numbers.
4. **Error Handling** - Division by zero is checked inside the divide() function.

### Functions Used

| Function | Description |
|-----------|--------------|
| `add(x, y)` | Return the sum of two numbers |
| `subtract(x, y)` | Return the difference of two numbers |
| `multiply(x, y)` | Return the product of two numbers |
| `divide(x, y)` | Return the quotient if `y` ≠ 0, otherwise return error message |

### Sample Output

    Enter first number: 15
    Enter second number: 3
    Select operation:
    1. Add
    2. Subtract
    3. Multiply
    4. Divide
    Enter choice (1/2/3/4): 4
    Result: 5.0

