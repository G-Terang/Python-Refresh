def the_args(*args):
    total = 0
    for item in args:
        total += item
    return total

print(the_args(1, 4, 10))