import string
import types


def safe_call(fun : types.FunctionType, **kwargs):
    """
    >>> safe_call(f, x=5, y=7.0, z=3)
    15.0
    >>> safe_call(f2,x= "hello",y= "yalla",z= "maccabi")
    hello yalla maccabi
    >>> safe_call(f, x=5, y=7.0, z="abc")
    an error has occurred
    """
    if fun.__annotations__ == {}:
        print(fun(**kwargs))
    else:
        try:
            print(fun(**kwargs))
        except:
            print("an error has occurred")


def f(x: int, y: float, z):
    return x + y + z


def f2(x: string, y: string, z: string):
    return x + " " + y + " " + z


def f3(s):
    return (s)


if __name__ == '__main__':
    import doctest

    doctest.testmod()

    safe_call(f2, x="a", y="b", z="c")  # returns "abc"
    safe_call(f, x=5, y=7.0, z=3)  # returns 15.0
    safe_call(f, x=5, y="abc", z=3)  # raises an exception
    safe_call(f3, s="get")  # returns "get"
