
# CS2021 Lab 02 - Required Questions

#  RQ1
from operator import add, sub
def a_plus_abs_b(a, b):
    """Return a+abs(b), but without calling abs.

    >>> a_plus_abs_b(2, 3)
    5
    >>> a_plus_abs_b(2, -3)
    5
    """
    if b < 0:
        f = lambda x,y: sub(x,y)
    else:
        f = lambda x,y:add(x,y)
    return f(a, b)


#  RQ2
def two_of_three(a, b, c):
    """Return x*x + y*y, where x and y are the two largest members of the
    positive numbers a, b, and c.

    >>> two_of_three(1, 2, 3)
    13
    >>> two_of_three(5, 3, 1)
    34
    >>> two_of_three(10, 2, 8)
    164
    >>> two_of_three(5, 5, 5)
    50
    """
    return a**2 + b**2 + c**2 - min([a, b, c])**2


#  RQ3
def largest_factor(n):
    """Return the largest factor of n that is smaller than n.

    >>> largest_factor(15) # factors are 1, 3, 5
    5
    >>> largest_factor(80) # factors are 1, 2, 4, 5, 8, 10, 16, 20, 40
    40
    """

    for x in range (n-1,1,-1):
    	if n % x == 0:
    		return x
    	

         
#  RQ4

# First, conider this simplest of dispatch functions the if_function function, which tests the truthiness of the first argument and returns one of the other two arguments.

def if_function(condition, true_result, false_result):
   
    """Return true_result if condition is a true value, and
    false_result otherwise.
    >>> if_function(True, 2, 3)
    2
    >>> if_function(False, 2, 3)
    3
    >>> if_function(3==2, 3+2, 3-2)
    1
    >>> if_function(3>2, 3+2, 3-2)
    5
    """
    if condition:
        return true_result
    else:
        return false_result


# The following two functions will simply call one-line functions named c,t,f.

def with_if_function():
    return if_function(c(), t(), f())
def with_if_statement():
    """
    >>> with_if_statement()
    1
    """
    if c():
        return t()
    else:
        return f()


#  Although it seems these two functions will always do the same thing. You can show they in fact do not. Write three one-line functions c, t,and f such that calling the with_if_statement and calling the with_if_function do different things.

def c():
    "*** YOUR CODE HERE ***"
    return 1


def t():
    "*** YOUR CODE HERE ***"
    return 1

def f():
    "*** YOUR CODE HERE ***"
    return 2/0

# Hint:  write the functions (c,t,f) so that calling the with_if_statement function returns the integer number 1, but calling the with_if_function function throws a ZeroDivisionError

#Required Question 5

def keep(pred,n):
    """Implements the function of a predicate pred and a number n, and prints the numbers from 1 to n to the screen if it fulfills the predicate.

    >>> keep(lambda x : x%2 ==0, 5)
    2
    4
    """
    "*** YOUR CODE HERE ***"
    
    for i in range (1,n,1):
      if pred(i):
        print(i)
        i += 1



import doctest
if __name__ == "__main__":
  doctest.testmod(verbose=True)
