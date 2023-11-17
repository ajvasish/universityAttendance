 # University Attendance
 
 ### Problem Statement
 In a university, your attendance determines whether you will be allowed to attend your graduation ceremony.
You are not allowed to miss classes for four or more consecutive days.
Your graduation ceremony is on the last day of the academic year, which is the Nth day.

  Your task is to determine the following:

1. The number of ways to attend classes over N days.
2. The probability that you will miss your graduation ceremony.

Represent the solution in the string format as "Answer of (2) / Answer of (1)".
Don't actually divide or reduce the fraction to decimal


### Aproach

First I will try to represent the solution recursively.
1. The number of ways to attend classes over N days:
If **f(n,m)** is the number of ways to attend class over **n** days where you are not allowed to miss **m** or more consecutive days.
**f(n,m) = f(n-1, 0) + f(n-1, m+1)**
where stopping condition is: **if m is 4 return 0** (since we cant skip 4 or more consecutive days) and **if n is 0 return 1**

2) The probability that you will miss your graduation ceremony.
Use the same function above as **f(n-1, 1)**

The number of input params to the recursive function is 2, we can use a 2D Matrix and solve it using dynamic programming as well. 
Both approaches are included. As an additional feature, the number of consecutive days m is configurable.

Time Complexity: O(m\*n) but if m = 4, it is O(n) since m is constant
Space Complexity: O(m\*n) but if m = 4, it is O(n) since m is constant

## To run
```
git clone <repo>
cd universityAttendance
python main.py numDays [numConsecutiveDays ]
```
eg. To run with input n=5
```
python main.py 5
```
eg. To run with input n=5 m=3
```
python main.py 5 3
```
