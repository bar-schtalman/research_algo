def lastcall(func):
    runs = {}
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

# @lastcall
# def param_function(param):
