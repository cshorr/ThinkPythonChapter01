"""
# Exercise04
The following questions give you a chance to practice writing arithmetic
expressions.

1. How many seconds are there in 42 minutes 42 seconds?

2. How many miles are there in 10 kilometers? Hint: there are 1.61 kilometers in a
mile.

3. If you run a 10 kilometer race in 42 minutes 42 seconds, what is your average
pace in seconds per mile?
    * AVG Velocity Equation => r * t = d
    * So, r = d / t, but we want t in seconds per mile its asking for t/d
    * And, d must be in miles and t in seconds
    * So, ((42*60) + 42)seconds / (10 / 1.61)K

4. What is your average pace in minutes and seconds per mile?

5. What is your average speed in miles per hour?

If you already know about variables, you can use them for this exercise. If you
don’t, you can do the exercise without them – and then we’ll see them in the next
chapter.
"""
# No Variables
print(42 * 60 + 42)  # Seconds in 42 minutes
print(10 / 1.61)  # Miles in 10K
print((42*60 + 42) / (10 / 1.61))  # This of course could be simplified.
print( 2562 / 6.211180124223602)  # One way to simplify is to see the previous 2 answers can be used.
print((42/60 + 42) / (10 / 1.61))  # Minutes per mile, which again could be simplified.
print(412.482 / 60) # Minutes per mile with previously calculated value,
                    # but what if we just want the minute portion, not the fractional portion?
print(412.482 // 60)  # This is "integer division" meaning the fractional part gets truncated.
print((10 / 1.61) / ((42/60) + (42/3600)))  # Miles per Hour. This of course could be simplified.
print(6.211180124223602 / (2562 / 3600)) # Here we re-use values from the previous calculations.

"""
Wouldn't it be easier if we could store and re-use the values without having to
re-type them or cut-n-paste them? Well, as noted, variables are the answer. Here
is a solution using variables.
"""
print("-"*80)
sec_in_min = 42 * 60 + 42
mile_in_10k = 10 / 1.61
sec_per_mile = sec_in_min / mile_in_10k
min_per_mile = sec_per_mile / 60
min_per_mile_int_only = sec_per_mile // 60
mile_per_hour = (6.211180124223602 / (2562 / 3600)) # Here we re-use values from the previous calculations.
print(f"""1. {sec_in_min} Seconds in Min.
2. {mile_in_10k} Miles in 10K.
3. {sec_per_mile} Seconds per Mile.
4. {min_per_mile} Minutes per Mile.
   {min_per_mile_int_only} Minutes per Mile, integer part only.
5. {mile_per_hour} Miles per hour.
""")
