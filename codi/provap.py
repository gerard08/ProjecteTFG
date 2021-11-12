from multiprocessing import Pool

def prova(x):
    x[0] = x[0] + 1
    print(x)


if __name__ == '__main__':
    pool = Pool()
    x = [0]
    [pool.apply(prova, args=(x,)) for j in range(5)]
