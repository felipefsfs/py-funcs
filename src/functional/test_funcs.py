from funcs import compose, pipe

if __name__ == '__main__':
    ff = compose(lambda a: a+1, lambda a: a*1000, lambda a: a - 10)
    print(ff(11))
    ff = pipe(lambda a: a+1, lambda a: a*1000, lambda a: a - 10)
    print(ff(11))