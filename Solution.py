# Scaffold for solution to DIT873 / DAT346, Programming task 1


def fib (limit) :
    # Given an input limit, calculate the Fibonacci series within [0,limit]
    # The first two numbers of the series are always equal to 1,
    # and each consecutive number returned is the sum of the last two numbers.
    # You should use generators for implementing this function
    # See https://docs.python.org/3/howto/functional.html#generator-expressions-and-list-comprehensions
    # Your code below

    F1=0
    F2=1
    while F1<limit:
        yield F1
        F1, F2 = F2, F1 + F2   #calculating the Fibonacchi numbers : each consecutive number returned is the sum of the last two numbers.
    

def list_fib(limit) :
    # Construct a list of Fibonacci series
    return list(fib(limit)) #convert generator to list

# The following is called if you execute the script from the commandline
# e.g. with python solution.py
if __name__ == "__main__":
    assert list_fib(20) == [0, 1, 1, 2, 3, 5, 8, 13]
    assert list_fib(40) == [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
    assert list_fib(100) == [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    assert list_fib(1000) == [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987]
    
