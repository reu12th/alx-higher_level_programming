# 0x05. Python - Exceptions

### `Python`

## 0. Safe list printing
A function that prints `x` elements of a list.   
* Prototype: `def safe_print_list(my_list=[], x=0):`
File: `0-safe_print_list.py`

## 1. Safe printing of an integers list
A  function that prints an integer with `"{:d}".format()`.   
* Prototype: `def safe_print_integer(value):`
File: `1-safe_print_integer.py`

## 2. Print and count integers
A function that prints first `x` elements of a list and only integers.   
* Prototype: `def safe_print_list_integers(my_list=[], x=0):`
File: `2-safe_print_list_integers.py`

## 3. Integers division with debug
A function that divides 2 integers and prints the result.   
* Prototype: `def safe_print_division(a, b):`
File: `3-safe_print_division.py`

## 4. Divide a list
A  function that divides element by element 2 lists.   
* Prototype: `def list_division(my_list_1, my_list_2, list_length):`
File: `4-list_division.py`

## 5. Raise exception
A function that raises a type exception.   
* Prototype: `def raise_exception():`
File: `5-raise_exception.py`

## 6. Raise a message
A function that raises a name exception with a message.   
* Prototype: `def raise_exception_msg(message=""):`
File: `6-raise_exception_msg.py`

## 7. Safe integer print with error message
A function that prints an integer.   
* Prototype: `def safe_print_integer_err(value):`
File: `100-safe_print_integer_err.py`

## 8. Safe function
A function that executes a function safely. 
* Prototype: `def safe_function(fct, *args):`
File: `101-safe_function.py`

## 9. ByteCode -> Python #4
A Python function `def magic_calculation(a, b):` that does exactly the same as the following Python bytecode:   
```asm
  3           0 LOAD_CONST               1 (0)
              3 STORE_FAST               2 (result)

  4           6 SETUP_LOOP              94 (to 103)
              9 LOAD_GLOBAL              0 (range)
             12 LOAD_CONST               2 (1)
             15 LOAD_CONST               3 (3)
             18 CALL_FUNCTION            2 (2 positional, 0 keyword pair)
             21 GET_ITER
        >>   22 FOR_ITER                77 (to 102)
             25 STORE_FAST               3 (i)

  5          28 SETUP_EXCEPT            49 (to 80)

  6          31 LOAD_FAST                3 (i)
             34 LOAD_FAST                0 (a)
             37 COMPARE_OP               4 (>)
             40 POP_JUMP_IF_FALSE       58

  7          43 LOAD_GLOBAL              1 (Exception)
             46 LOAD_CONST               4 ('Too far')
             49 CALL_FUNCTION            1 (1 positional, 0 keyword pair)
             52 RAISE_VARARGS            1
             55 JUMP_FORWARD            18 (to 76)

  9     >>   58 LOAD_FAST                2 (result)
             61 LOAD_FAST                0 (a)
             64 LOAD_FAST                1 (b)
             67 BINARY_POWER
             68 LOAD_FAST                3 (i)
             71 BINARY_TRUE_DIVIDE
             72 INPLACE_ADD
             73 STORE_FAST               2 (result)
        >>   76 POP_BLOCK
             77 JUMP_ABSOLUTE           22

 10     >>   80 POP_TOP
             81 POP_TOP
             82 POP_TOP

 11          83 LOAD_FAST                1 (b)
             86 LOAD_FAST                0 (a)
             89 BINARY_ADD
             90 STORE_FAST               2 (result)

 12          93 BREAK_LOOP
             94 POP_EXCEPT
             95 JUMP_ABSOLUTE           22
             98 END_FINALLY
             99 JUMP_ABSOLUTE           22
        >>  102 POP_BLOCK

 13     >>  103 LOAD_FAST                2 (result)
            106 RETURN_VALUE
```
* Tip: [`Python bytecode`](https://docs.python.org/3.4/library/dis.html)
File: `102-magic_calculation.py`

## 10. CPython #2: PyFloatObject
Three C functions that print some basic info about Python lists, Python bytes an Python float objects:

**Python lists:**

* Prototype: `void print_python_list(PyObject *p);`
* Format: see example
* If `p` is not a valid `PyListObject`, print an error message (see example)

**Python bytes:**

* Prototype: `void print_python_bytes(PyObject *p);`
* Format: see example
* Line “first X bytes”: print a maximum of 10 bytes
* If `p` is not a valid `PyBytesObject`, print an error message (see example)

**Python float:**

Prototype: `void print_python_float(PyObject *p);`
Format: see example
If `p` is not a valid `PyFloatObject`, print an error message (see example)
Read `/usr/include/python3.4/floatobject.h`

### About:
* Python version: 3.8
* The C Standard Library was utilized
* The shared library was compiled using this command line: `gcc -Wall -Werror -Wextra -pedantic -std=c99 -shared -Wl,-soname,libPython.so -o libPython.so -fPIC -I/usr/include/python3.4 103-python.c`
* The following macros/functions were not utilized: 
    * `Py_SIZE`
    * `Py_TYPE`
    * `PyList_Size`
    * `PyList_GetItem`
    * `PyBytes_AS_STRING`
    * `PyBytes_GET_SIZE`
    * `PyBytes_AsString`
    * `PyBytes_AsStringAndSize`
    * `PyFloat_AS_DOUBLE`
    * `PySequence_GetItem`
    * `PySequence_Fast_GET_SIZE`
    * `PySequence_Fast_GET_ITEM`
    * `PySequence_ITEM`
    * `PySequence_Fast_ITEMS`

### Execution:
```python
~/...$ python3 --version
Python 3.4.3
~/...$ gcc -Wall -Werror -Wextra -pedantic -std=c99 -shared -Wl,-soname,libPython.so -o libPython.so -fPIC -I/usr/include/python3.4 103-python.c
~/...$ cat 103-tests.py 
#!/usr/bin/python3 -u

import ctypes

lib = ctypes.CDLL('./libPython.so')
lib.print_python_list.argtypes = [ctypes.py_object]
lib.print_python_bytes.argtypes = [ctypes.py_object]
lib.print_python_float.argtypes = [ctypes.py_object]
s = b"Hello"
lib.print_python_bytes(s);
b = b'\xff\xf8\x00\x00\x00\x00\x00\x00';
lib.print_python_bytes(b);
b = b'What does the \'b\' character do in front of a string literal?';
lib.print_python_bytes(b);
l = [b'Hello', b'World']
lib.print_python_list(l)
del l[1]
lib.print_python_list(l)
l = l + [4, 5, 6.0, (9, 8), [9, 8, 1024], b"School", "Betty"]
lib.print_python_list(l)
l = []
lib.print_python_list(l)
l.append(0)
lib.print_python_list(l)
l.append(1)
l.append(2)
l.append(3)
l.append(4)
lib.print_python_list(l)
l.pop()
lib.print_python_list(l)
l = ["School"]
lib.print_python_list(l)
lib.print_python_bytes(l);
f = 3.14
lib.print_python_float(f);
l = [-1.0, -0.1, 0.0, 1.0, 3.14, 3.14159, 3.14159265, 3.141592653589793238462643383279502884197169399375105820974944592307816406286]
print(l)
lib.print_python_list(l);
lib.print_python_float(l);
lib.print_python_list(f);
~/...$ ./103-tests.py 
[.] bytes object info
  size: 5
  trying string: Hello
  first 6 bytes: 48 65 6c 6c 6f 00
[.] bytes object info
  size: 8
  trying string: ??
  first 9 bytes: ff f8 00 00 00 00 00 00 00
[.] bytes object info
  size: 60
  trying string: What does the 'b' character do in front of a string literal?
  first 10 bytes: 57 68 61 74 20 64 6f 65 73 20
[*] Python list info
[*] Size of the Python List = 2
[*] Allocated = 2
Element 0: bytes
[.] bytes object info
  size: 5
  trying string: Hello
  first 6 bytes: 48 65 6c 6c 6f 00
Element 1: bytes
[.] bytes object info
  size: 5
  trying string: World
  first 6 bytes: 57 6f 72 6c 64 00
[*] Python list info
[*] Size of the Python List = 1
[*] Allocated = 2
Element 0: bytes
[.] bytes object info
  size: 5
  trying string: Hello
  first 6 bytes: 48 65 6c 6c 6f 00
[*] Python list info
[*] Size of the Python List = 8
[*] Allocated = 8
Element 0: bytes
[.] bytes object info
  size: 5
  trying string: Hello
  first 6 bytes: 48 65 6c 6c 6f 00
Element 1: int
Element 2: int
Element 3: float
[.] float object info
  value: 6.0
Element 4: tuple
Element 5: list
Element 6: bytes
[.] bytes object info
  size: 9
  trying string: School
  first 10 bytes: 48 6f 6c 62 65 72 74 6f 6e 00
Element 7: str
[*] Python list info
[*] Size of the Python List = 0
[*] Allocated = 0
[*] Python list info
[*] Size of the Python List = 1
[*] Allocated = 4
Element 0: int
[*] Python list info
[*] Size of the Python List = 5
[*] Allocated = 8
Element 0: int
Element 1: int
Element 2: int
Element 3: int
Element 4: int
[*] Python list info
[*] Size of the Python List = 4
[*] Allocated = 8
Element 0: int
Element 1: int
Element 2: int
Element 3: int
[*] Python list info
[*] Size of the Python List = 1
[*] Allocated = 1
Element 0: str
[.] bytes object info
  [ERROR] Invalid Bytes Object
[.] float object info
  value: 3.14
[-1.0, -0.1, 0.0, 1.0, 3.14, 3.14159, 3.14159265, 3.141592653589793]
[*] Python list info
[*] Size of the Python List = 8
[*] Allocated = 8
Element 0: float
[.] float object info
  value: -1.0
Element 1: float
[.] float object info
  value: -0.1
Element 2: float
[.] float object info
  value: 0.0
Element 3: float
[.] float object info
  value: 1.0
Element 4: float
[.] float object info
  value: 3.14
Element 5: float
[.] float object info
  value: 3.14159
Element 6: float
[.] float object info
  value: 3.14159265
Element 7: float
[.] float object info
  value: 3.141592653589793
[.] float object info
  [ERROR] Invalid Float Object
[*] Python list info
  [ERROR] Invalid List Object
~/...$
```
File: `103-python.c`
