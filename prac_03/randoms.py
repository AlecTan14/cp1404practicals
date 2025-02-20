"""
Program used to test and practice using random functions
"""

import random
dir(random)

print(random.randint(5, 20))  # line 1
print(random.randrange(3, 10, 2))  # line 2
print(random.uniform(2.5, 5.5))  # line 3

"""
For the following questions I ran the program 5 times.

These were the results:

1st Run:

13
9
4.0084419257024795

2nd Run:

15
3
4.466055866771518

3rd Run:

7
9
3.5558303301647483

4th Run:

8
7
5.454084857825009

5th Run:

12
7
2.7972377422487313

What did you see on line 1?
- A whole number between 5 and 20
What was the smallest number you could have seen, what was the largest?
- The smallest number I could have seen would be a 5, The largest would be a 20.

What did you see on line 2?
- A random whole number from the given range within increments of 2
What was the smallest number you could have seen, what was the largest?
- The smallest number I could have seen would be a 3, The largest would be a 9.
Could line 2 have produced a 4?
- No. Because it is in increments of 2, the only possible numbers are: 3, 5, 7, 9.

What did you see on line 3?
- A random float value within the given range
What was the smallest number you could have seen, what was the largest?
- The smallest number would have been 2.5, and the largest would have been 5.5
"""

"""
Write code, not a comment, to produce a random number between 1 and 100 inclusive.
"""

print(random.randint(1,100))



