"""
# Exercise 01
You might wonder what round does if a number ends in 0.5. The answer is that it
sometimes rounds up and sometimes rounds down. Try these examples and see if you
can figure out what rule it follows.

round(42.5)
42
round(43.5)
44
If you are curious, ask a virtual assistant, "If a number ends in 0.5, does
Python round up or down?"
"""
print(round(42.5))
print(round(43.5))
"""
AI Bot Answer: If a number ends in 0.5, does Python round up or down?

Python rounds numbers ending in 0.5 up to the nearest even integer. This is known
as "round half to even" or "banker's rounding". Here's a quick explanation:

For positive numbers:
1.5 rounds to 2
2.5 rounds to 2
3.5 rounds to 4

For negative numbers:
-1.5 rounds to -2
-2.5 rounds to -2
-3.5 rounds to -4

This rounding method is designed to reduce bias in statistical sampling and
financial calculations. It ensures that when rounding a large set of numbers,
you're equally likely to round up or down, which can be important in certain
applications. If you need different rounding behavior, you might want to use the
math.floor(), math.ceil(), or create a custom rounding function.
"""