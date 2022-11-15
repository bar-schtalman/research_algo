runs = {}


def lastcall(func):
    """
    this is a "decorator" method for execute functions with one parameter.
    this method save for every executed functions the parameter and the returned value,
    if it found that any function has already executed with the given parameter it won't need to execute the program,
    it will give immediate the answer.

    >>> f(3)
    9
    >>> f(3)
    I already told you that the answer is 9 !
    >>> f(5)
    25
    >>> f1(3)
    4
    >>> f1(189)
    190
    >>> f(5)
    I already told you that the answer is 25 !
    >>> f2("abc")
    abc(:
    >>> f2("hahaha")
    hahaha(:
    >>> f2("abc")
    I already told you that the answer is abc(: !
    >>> f3(15)
    False
    >>> f3(20)
    True
    >>> f(5)
    I already told you that the answer is 25 !
    >>> f2("hahaha")
    I already told you that the answer is hahaha(: !
    >>> f3(18)
    True
    >>> f3(15)
    I already told you that the answer is False !
    >>> f3(18)
    I already told you that the answer is True !
    """

    def wrapper(param):
        if func.__name__ in runs:
            if param in runs[func.__name__]:
                print("I already told you that the answer is", runs[func.__name__][param], "!")
            else:
                ans = func(param)
                runs[func.__name__][param] = ans
                print(ans)
        else:
            ans = func(param)
            print(ans)
            runs[func.__name__] = {}
            runs[func.__name__][param] = ans

    return wrapper


@lastcall
def f(x: int):
    return x ** 2


@lastcall
def f1(x: int):
    return x + 1


@lastcall
def f2(s: str):
    return s + "(:"


@lastcall
def f3(x: int):
    return x % 2 == 0


if __name__ == '__main__':
    import doctest

    doctest.testmod()
    """
f(3)
f(3)
f(4)
f1(3)
f1(5)
f1(5)
f2("abc ")
f2("abc ")
f(2)
f(2)
f(10)
f(2)
f(10)
  """

# @lastcall
# def param_function(param):
