def logger(func):
    def log(*args):
        arg = ', '.join([str(arg) for arg in args])
        print(f'{func.__name__} called with {arg}')
        return func(*args)
    return log


@logger
def add(x, y):
    return x + y


@logger
def square_all(*args):
    return [arg ** 2 for arg in args]

square_all(4, 8, 6)