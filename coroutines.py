#Name: Saumick Pradhan
# M13893733
################################################
# Lab11 Higher-Order Generators and CoRoutines #
###############################################
#RQ1
def merge(s0, s1):
    """Yield the elements of strictly increasing iterables s0 and s1, removing
    repeats. Assume that s0 and s1 have no repeats. You can also assume that s0
    and s1 represent infinite sequences.

    >>> m = merge([0, 2, 4, 6, 8, 10, 12, 14], [0, 3, 6, 9, 12, 15])
    >>> type(m)
    <class 'generator'>
    >>> list(m)
    [0, 2, 3, 4, 6, 8, 9, 10, 12, 14, 15]
    >>> def big(n):
    ...    k = 0
    ...    while True: yield k; k += n
    >>> m = merge(big(2), big(3))
    >>> [next(m) for _ in range(11)]
    [0, 2, 3, 4, 6, 8, 9, 10, 12, 14, 15]
    """
    i0, i1 = iter(s0), iter(s1)
    e0, e1 = next(i0, None), next(i1, None)
    "*** YOUR CODE HERE ***"
    try:
      while 1:
            if e1 < e0:
              yield e1
              e1 = next(i1, e0) 
            elif e1 > e0:
                yield e0
                e0 = next(i0, e1)   
            else:
                yield e0
                e0, e1 = next(i0, None), next(i1, None)
    except:
        pass


#RQ2
def residues_generator(m):
    """
    Takes in an integer m, and yields m different generators, 
    each one returns the numbers in a distinct residue class of m.

    >>> res_mod_four = residues_generator(4)
    >>> for res_group in res_mod_four:
    ...     for _ in range(3):
    ...         print(next(res_group))
    0
    4
    8
    1
    5
    9
    2
    6
    10
    3
    7
    11
    """
    "*** YOUR CODE HERE ***"

    def gen(k):
        while 1:
            yield k
            k += m

    for k in range(m):
        yield gen(k)


#RQ3
def zip(*iterables):
    """
    Takes in any number of iterables and zips them together.
    Returns a generator that outputs a series of lists, each
    containing the nth items of each iterable.
    >>> z = zip([1, 2, 3], [4, 5, 6], [7, 8])
    >>> for i in z:
    ...     print(i)
    ...
    [1, 4, 7]
    [2, 5, 8]
    """
    "* YOUR CODE HERE *"
    try:
      iList = [iter(i) for i in iterables]
      while True:
        yield [next(elements) for elements in iList]
    except:
      pass

# RQ4 Coroutines Question
def supplier(ingredients, chef):
    for ingredient in ingredients:
        try:
            chef.send(ingredient)
        except StopIteration as e:
            print(e)
            break
        except RuntimeError as e:
            print('No one left to serve!')
            break
    chef.close()


def customer():
    served = False
    while True:
        try:
            dish = yield
            print('Yum! Customer got a {}!'.format(dish))
            served = True
        except GeneratorExit:
            if not served:
                print('Customer never got served.')
            raise

def chef(customers, dishes):
    """
    >>> cust = customer()
    >>> next(cust)
    >>> c = chef({cust: 'hotdog'}, {'hotdog': ['bun', 'hotdog']})
    >>> next(c)
    >>> supplier(['bun', 'hotdog'], c)
    Yum! Customer got a hotdog!
    Chef went home.

    >>> cust = customer()
    >>> next(cust)
    >>> c = chef({cust: 'hotdog'}, {'hotdog': ['bun', 'hotdog']})
    >>> next(c)
    >>> supplier(['bun'], c)
    Chef went home.
    Customer never got served.

    >>> cust = customer()
    >>> next(cust)
    >>> c = chef({cust: 'hotdog'}, {'hotdog': ['bun', 'hotdog']})
    >>> next(c)
    >>> supplier(['bun', 'hotdog', 'mustard'], c)
    Yum! Customer got a hotdog!
    No one left to serve!
    """
    "* YOUR CODE HERE *"
    remaining_customers = dict(customers)
    ingredients = set()
    while True:
        try:
            ingredient = yield
        except GeneratorExit:
            print('Chef went home.')
            for customer in customers:
                customer.close()
            raise

        ingredients.add(ingredient)

        if not remaining_customers:
            raise StopIteration('No one left to serve!')

        for customer, dish_name in dict(remaining_customers).items():
          # include an if-statement to check 
          # if all ingredients for dish are available to chef
          # so that the customer is ready to be served
          if all(ingredient in ingredients for ingredient in dishes[dish_name]): 
            remaining_customers.pop(customer)  
            customer.send(dish_name)    

import doctest
doctest.testmod(verbose=True)
