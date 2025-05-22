def cache(func):
    cache = {}

    def wrapper(*args):
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]

    return wrapper


def log(func):
    def wrapper(*args):
        print("Calling function: {} with arguments : {}".format(func.__name__, ", ".join(map(str, args))))
        return func(*args)

    return wrapper

@cache
@log
def sum(a, b):
    print("Calculating... sum of {} and {}".format(a, b))
    return a + b

print(sum(1, 2))
# print(sum(1, 2))
# print(sum(2, 3))
# print(sum(2, 4))
# print(sum(1, 2))


