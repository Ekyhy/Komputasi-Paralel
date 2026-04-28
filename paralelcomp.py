import numpy as np
from time import time
import multiprocessing as mp

def howmany_within_range(row, min, max):
    """"""
    count = 0
    for n in row:
        if min <= n <= max:
            count = count + 1
    return count

def howmany_within_range_rowonly(row, minimum=4, maximum=8):
    count = 0
    for n in row:
        if minimum <= n <= maximum:
            count = count + 1
    return count


if __name__ == '__main__':
    np.random.RandomState(100)
    arr = np.random.randint(0, 10, size=[2000, 5])
    data = arr.tolist()
    data[:5]
    # Langkah 1: Init multiprocessing.Pool()
    pool = mp.Pool(mp.cpu_count())

    # Langkah 2: `pool.apply` the `howmany_within_range()`
    # Menggunakan `pool.apply` dan args
    result = [pool.apply(howmany_within_range, args=(row, 4, 8)) for row in data] 
    
    # Menggunakan `pool.map`
    results = pool.map(howmany_within_range_rowonly, [row for row in data])

    # Menggunakan `pool.strmap`
    resultx = pool.starmap(howmany_within_range, [(row, 4, 8) for row in data])
    
    # Langkag 3: Jangan lupa untuk menutup `pool`
    pool.close()

    print(result[:10])
    print(results[:20])
    print(resultx[:30])
