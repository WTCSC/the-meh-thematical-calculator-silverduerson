# The Meh Calculator

A simple Python calculator that does basic math but has a very lazy personality.

## Features
- Add, subtract, multiply, and divide two numbers.
- Handles division by zero with a cheeky message.
- Interactive prompts with humorous commentary.

## Examlple interaciton
Welcome... I guess. This is a calculator. Don’t get too excited.
What’s your name? ...Not that I care: Alice
Cool, Alice. Let’s just get this over with.
First number, please... hurry up: 12
Second number... fine, type it: 8
Pick an operation. Options are: +, -, *, /
Which one do you want? +
Yeah, the answer is 20. Happy now?

## Decision Tree
Start

├── Print welcome message

├── Ask for user name → print snarky response

├── Ask for num1

├── Ask for num2

├── Ask for operation (+, -, *, /)

└── Decision:
    
 ├── If "+" → call add(a, b) → print result
    
├── If "-" → call subtract(a, b) → print result

├── If "*" → call multiply(a, b) → print result
└── If "/" 
      
├── If b == 0 → print "I don’t think you can do that smart guy"
└── Else → call divide(a, b) → print result

## Usage

Run the script:

```bash
python calculator.py
