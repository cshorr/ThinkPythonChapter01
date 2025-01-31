"""
# Exercise02
When you learn about a new feature, you should try it out and make mistakes on
purpose. That way, you learn the error messages, and when you see them again,
you will know what they mean. It is better to make mistakes now and deliberately
than later and accidentally.

You can use a minus sign to make a negative number like -2. What happens if you
put a plus sign before a number? What about 2++2?

What happens if you have two values with no operator between them, like 4 2?

If you call a function like round(42.5), what happens if you leave out one or
both parentheses?
"""
print(+2)
# The result is a positive 2
print(2++2)
# The result is unexpectedly 4 and not an error
print(4 * 2)
# "SyntaxError: invalid syntax. Perhaps you forgot a comma?"
print(round (42.5))
# SyntaxError: '(' was never closed
print(round (42.5))
# Same as print(4 2), weird! Why?
# SyntaxError: invalid syntax. Perhaps you forgot a comma?
