"""
# Exercise03
Recall that every expression has a value, every value has a type, and we can use
the type function to find the type of any value.

What is the type of the value of the following expressions? Make your best guess
for each one, and then use type to find out.

765
2.718
'2 pi'
abs(-7)
abs(-7.0)
abs
int
type

## Guesses
int
float
string
int
float
function
type
function

## Results
```
<class 'int'>
<class 'float'>
<class 'str'>
<class 'int'>
<class 'float'>
<class 'builtin_function_or_method'>
<class 'type'>
<class 'type'> !?! what !?!
```
"""
print(type(765))
print(type(2.718))
print(type('2 pi'))
print(type(abs(-7)))
print(type(abs(-7.0)))
print(type(abs))
print(type(int))
print(type(type))
