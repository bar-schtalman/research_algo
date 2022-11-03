import string
import types


def safe_call(fun : types.FunctionType, **kwargs):
    """
    description: this function provide type check for argument before execute the wanted function
    :param :func, func_args
    :return:func calculate. in case of bad syntax -> "an error has occurred"
    >>> safe_call(f, x=5, y=7.0, z=3)
    15.0
    >>> safe_call(f2,x= "hello",y= "yalla",z= "maccabi")
    hello yalla maccabi
    >>> safe_call(f, x=5, y=7.0, z="abc")
    an error has occurred
    >>> safe_call(f3,s = "hey",y = 3)
    heyheyhey
    >>> safe_call(f3,s= 3,y= "hey")
    heyheyhey
    >>> safe_call(f3,s= "hello",y= "yalla")
    an error has occurred
    >>> safe_call(f4,x= 5.12)
    0.1200000000000001
    >>> safe_call(f4,x= (5,2))
    an error has occurred
    >>> safe_call(f2,x = ("hello", "yalla", "maccabi"),y = [1,2],z =  "hey",c = 5)
    an error has occurred
    >>> safe_call(f,x = {'a': "hello", 'b': "yalla", 'c': "maccabi"},y = (1,2),z =  "hey")
    an error has occurred
    >>> safe_call(f,x = {'a': "hello", 'b': "yalla", 'c': "maccabi"},y = (1,2),z =  "hey",z2 = "bye")
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


def f3(s: string, y:int):
    return (s*y)

def f4(x: float):
    a = int(x)
    return x%a

if __name__ == '__main__':
    import doctest

    doctest.testmod()


