""" Project Euler """

# Problem 1
"""
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get
3, 5, 6 and 9. The sum of these multiples is 23. Find the sum of all the
multiples of 3 or 5 below 1000.
"""
ans = sum(x for x in range(1, 1000) if x % 3 == 0 or x % 5 == 0)
print(f"Answer 1: {ans}")

# Problem 2
"""
Each new term in the Fibonacci sequence is generated by adding the previous two
terms. By starting with 1 and 2, the first 10 terms will be: 1, 2, 3, 5, 8, 13,
21, 34, 55, 89, etc. By considering the terms in the Fibonacci sequence whose
values do not exceed four million, find the sum of the even-valued terms.
"""
def fib():
    a, b, s = 0, 1, 1
    while s < 4000000:
        s = a + b
        a = b
        b = s
        yield s


ans = sum(x for x in fib() if x % 2 == 0)
print(f"Answer 2: {ans}")

# Problem 3
"""
The prime factors of 13195 are 5, 7, 13 and 29. What is the largest prime factor
of the number 600851475143?
"""
import math

def largest_factor(n):
    start = math.floor(math.sqrt(n))
    while start > 1:
        if n % start == 0 and largest_factor(start) == 1:
            break
        start -= 1
    return start

ans = largest_factor(600851475143)
print(f"Answer 3: {ans}")

# Problem 4
"""
A palindromic number reads the same both ways. The largest palindrome made from
the product of two 2-digit numbers is 9009 = 91 × 99. Find the largest
palindrome made from the product of two 3-digit numbers.
"""
def max_nines(d):
    a = 0
    for _ in range(d):
        a *= 10
        a += 9
    return a

def len_of_number(d):
    l = 0
    while d > 0:
        l += 1
        d //= 10
    return l

def reverse_number(d, l):
    ans = 0
    for _ in range(l):
        ans *= 10
        ans += d % 10
        d //= 10
    return ans

def is_palindrome(p):
    l = len_of_number(p) // 2
    fhalf = p // 10 ** l
    if len_of_number(p) % 2 == 1:
        # It's an odd length number, drop the middle digit
        fhalf //= 10
    lhalf = p % 10 ** l
    lhalf = reverse_number(lhalf, l)
    return fhalf == lhalf

def subset_tuples(a, b):
    return ((x, y) for x in range(1, a+1) for y in range(x, b+1))

def largest_palindrome(d):
    a = b = max_nines(d)
    tups = sorted(list(subset_tuples(a, b)), key=lambda t: t[0]*t[1], reverse=True)
    for x, y in tups:
        if is_palindrome(x*y):
            return x*y
    return None

ans = largest_palindrome(3)
print(f"Answer 4: {ans}")

# Problem 5
"""
2520 is the smallest number that can be divided by each of the numbers from 1
to 10 without any remainder. What is the smallest positive number that is
evenly divisible by all of the numbers from 1 to 20?
"""
def find_numbers(a, b):
    assert(0 < a < b)
    ans = list(range(2, b+1))
    while b > a:
        for prime in find_primes(b):
            if prime in ans:
                ans.remove(prime)
        b -= 1
    return ans

def find_primes(d):
    assert(d > 1)
    return (num for num in range(2, d) if d % num == 0)

def find_end(b):
    ans = 1
    for i in range(1, b+1):
        ans *= i
    return ans

def least_common_number(a, b):
    numbers = find_numbers(a, b)
    for num in range(b, find_end(b), b):
        if all(num % n == 0 for n in numbers):
            return num
    return None

ans = least_common_number(1, 20)
print(f"Answer 5: {ans}")
