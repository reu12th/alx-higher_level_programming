# This is the dir 0x01. Python - if/else, loops, functions

### 0. Positive anything is better than negative nothing
This program will assign a random signed number to the variable `number` each time it is executed. Complete the source code in order to print whether the number stored in the variable `number` is positive or negative.  
File: `0-positive_or_negative.py`

### 1. The last digit
This program will assign a random signed number to the variable `number` each time it is executed. Complete the source code in order to print the last digit of the number stored in the variable `number`.  
File: `1-last_digit.py`

### 2. I sometimes suffer from insomnia. And when I can't fall asleep, I play what I call the alphabet game
A program that prints the ASCII alphabet, in lowercase, not followed by a new line.  
File: `2-print_alphabet.py`

### 3. When I was having that alphabet soup, I never thought that it would pay off
A program that prints the ASCII alphabet, in lowercase, not followed by a new line.  
File: `3-print_alphabt.py`

### 4. Hexadecimal printing
A program that prints all numbers from `0` to `98` in decimal and in hexadecimal.  
File: `4-print_hexa.py`

### 5. 00...99
A program that prints numbers from `0` to `99`.  
File: `5-print_comb2.py`

### 6. Inventing is a combination of brains and materials. The more brains you use, the less material you need
A program that prints all possible different combinations of two digits.  
File: `6-print_comb3.py`

### 7. islower
A function that checks for lowercase character.  
File: `7-islower.py`

### 8. To uppercase
A function that prints a string in uppercase followed by a new line.  
File: `8-uppercase.py`

### 9. There are only 3 colors, 10 digits, and 7 notes; it's what we do with them that's important
A function that prints the last digit of a number.  
File: `9-print_last_digit.py`

### 10. a + b
A function that adds two integers and returns the result.  
File: `10-add.py`

### 11. a ^ b
A function that computes `a` to the power of `b` and return the value.  
File: `11-pow.py`

### 12. Fizz Buzz
A function that prints the numbers from `1` to `100` separated by a space.  
File: `12-fizzbuzz.py`

### 13. Insert in sorted linked list
A function in C that inserts a number into a sorted singly linked list.  
File: `13-insert_number.c, lists.h` (unavailable yet)

### 14. Smile in the mirror
A program that prints the ASCII alphabet, in reverse order, alternating lowercase and uppercase (`z` in lowercase and `Y` in uppercase) , not followed by a new line.  
File: `100-print_tebahpla.py`

### 15. Remove at position
A function that creates a copy of the string, removing the character at the position `n` (not the Python way, the “C array index”).  
File: `101-remove_char_at.py`

### 16. ByteCode -> Python #2
A Python function `def magic_calculation(a, b, c):` that does exactly the same as the following Python bytecode:   
```asm
  3           0 LOAD_FAST                0 (a)
              3 LOAD_FAST                1 (b)
              6 COMPARE_OP               0 (<)
              9 POP_JUMP_IF_FALSE       16

  4          12 LOAD_FAST                2 (c)
             15 RETURN_VALUE

  5     >>   16 LOAD_FAST                2 (c)
             19 LOAD_FAST                1 (b)
             22 COMPARE_OP               4 (>)
             25 POP_JUMP_IF_FALSE       36

  6          28 LOAD_FAST                0 (a)
             31 LOAD_FAST                1 (b)
             34 BINARY_ADD
             35 RETURN_VALUE

  7     >>   36 LOAD_FAST                0 (a)
             39 LOAD_FAST                1 (b)
             42 BINARY_MULTIPLY
             43 LOAD_FAST                2 (c)
             46 BINARY_SUBTRACT
             47 RETURN_VALUE
```
`tips - `[`ByteCode`](https://docs.python.org/3.4/library/dis.html)  
File: `102-magic_calculation.py`

