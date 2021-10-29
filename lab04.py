##Lab04 Required Questions ##

#########
# Lists #
#########


# RQ1
def cascade(lst):
    """Returns the cascade of the given list.

    >>> cascade([1, 2, 3, 4])
    [1, 2, 3, 4, 4, 3, 2, 1]
    """
    "*** YOUR CODE HERE ***"
    ## reverse = lst[start:stop:step]
    return lst[0:len(lst):1] + lst[::-1]


# RQ2
def maptwice(fn, seq):
    """Applies fn twice onto each element in seq and returns the resulting list.

    >>> maptwice(lambda x: x*x, [1, 2, 3])
    [1, 16, 81]
    """
    "*** YOUR CODE HERE ***"
    if len(seq) == 0:
        return []
    else:
        return maptwice(fn, seq[:-1]) + [fn(fn(seq[-1]))]


#RQ3
def filterout(pred, seq):
    """Keeps elements in seq only if they do not satisfy pred.

    >>> filterout(lambda x: x % 2 == 0, [1, 2, 3, 4])
    [1, 3]
    """
    "*** YOUR CODE HERE ***"
    if len(seq) == 0:
        return []
    else:
        if not (pred(seq[0])):
            return [seq[0]] + filterout(pred, seq[1:])
        else:
            return filterout(pred, seq[1:])


#RQ4
def comp(n, pred):
    """ Uses a one line list comprehension to return list of the first n integers (0...n-1) which satisfy the predicate pred.
    >>> comp(7, lambda x: x%2 ==0)
    [0, 2, 4, 6]
    """
    "*** YOUR CODE HERE ***"
    i = 0
    l = []
    while (i < n):
        if (pred(i)):
            l = l + [i]
            i += 1
        else:
            i += 1
    return l


#RQ5
def flatten(lst):
    """ Takes a nested list and "flattens" it.
    
    >>> flatten([1, 2, 3]) 
    [1, 2, 3]
    >>> x = [1, [2, 3], 4]      
    >>> flatten(x)
    [1, 2, 3, 4]
    >>> x = [[1, [1, 1]], 1, [1, 1]] 
    >>> flatten(x)
    [1, 1, 1, 1, 1, 1]
    >>> lst = [1, [[2], 3], 4, [5, 6]]
    >>> flatten(lst)
    [1, 2, 3, 4, 5, 6]
    """
    "*** YOUR CODE HERE ***"
    l = []
    for i in lst:
      if type(i) is list:
        l = l + flatten(i)
      else:
        l = l + [i]
    return l


import doctest
if __name__ == "__main__":
    doctest.testmod(verbose=True)
