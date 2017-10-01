"""This module computes binomial coefficient in various ways to
determine the most efficient method (fastest) in python.

"""

import logging
from math import factorial
from random import randint
import resource
import time

functions_to_be_tested = []
"List of functions calculating the binomial coefficient."


def py_direct(x, y):
    if y > x or y < 0:
        return 0
    answer = 1
    y = min(y, x - y)
    for z in range(y):
        answer *= (x - z)
        answer //= (z + 1)
    return answer


functions_to_be_tested.append(py_direct)


bi_buffer = {}
"""buffering computed binomial coefficients, like {0: [1, ], 1: [1, ],
2: [1, 2, ]}"""


def py_buffer(x, y):
    if y > x or y < 0:
        return 0
    y = min(y, x - y)

    if x in bi_buffer.keys():
        return bi_buffer[x][y]

    # fill row
    bi_buffer[x] = []
    answer = 1
    for z in range(x//2 + 1):
        bi_buffer[x].append(answer)
        answer *= (x - z)
        answer //= (z + 1)
    bi_buffer[x].append(answer)

    return bi_buffer[x][y]


functions_to_be_tested.append(py_buffer)


def math_fact(x, y):
    if y > x or y < 0:
        return 0
    return factorial(x) // (factorial(y) * factorial(x - y))


functions_to_be_tested.append(math_fact)


fact_buffer = []
"""buffering factorials like [1, 1, 2, 6, ]"""


def buffered_factorial(x):
    if x < len(fact_buffer):
        return fact_buffer[x]
    if not fact_buffer:
        fact_buffer.append(1)
    closest = len(fact_buffer) - 1
    fact = fact_buffer[closest]
    while(closest < x):
        closest += 1
        fact *= closest
        fact_buffer.append(fact)
    return fact


def buf_fact(x, y):
    if y > x or y < 0:
        return 0
    return buffered_factorial(x) // (buffered_factorial(y)
                                     * buffered_factorial(x - y))


functions_to_be_tested.append(buf_fact)


sparse_fact_buffer = {}
"""buffering factorials like {0: 1, 1: 1, 2: 2, 3: 6, }"""


def sparse_buffered_factorial(x):
    if x in sparse_fact_buffer.keys():
        return sparse_fact_buffer[x]
    if not sparse_fact_buffer:
        sparse_fact_buffer[0] = 1
    closest = max(y for y in sparse_fact_buffer.keys() if y < x)
    fact = sparse_fact_buffer[closest]
    while(closest < x):
        closest += 1
        fact *= closest
        if closest % 100 == 0:
            sparse_fact_buffer[closest] = fact
    return fact


def sparse_buf_fact(x, y):
    if y > x or y < 0:
        return 0
    return sparse_buffered_factorial(x) // (
        sparse_buffered_factorial(y)
        * sparse_buffered_factorial(x - y))


functions_to_be_tested.append(sparse_buf_fact)


test_to_be_run = []
results = {}
check_results = True


def add_test(n_test_points=1000, lo=10, hi=1000):
    test_params = []
    for i in range(n_test_points):
        n = randint(lo, hi)
        k = randint(1, n)
        test_params.append((n, k))
        if check_results:
            results[(n, k)] = sparse_buf_fact(n, k)
    test_to_be_run.append(("{} evaluations of order {}".format(
        n_test_points, hi), test_params))


def generate_tests():

    add_test(1, 10**3, 10**3)
    add_test(1, 10**4, 10**4)
    add_test(1, 10**5, 10**5)

    add_test(10**3, 10, 10**3)
    add_test(10**3, 10**2, 10**4)
    add_test(10**2, 10**2, 10**5)


def main():

    #logging.basicConfig(level=logging.DEBUG)

    soft, hard = 2 * 10**9, 3 * 10**9
    resource.setrlimit(resource.RLIMIT_AS, (soft, hard))

    print("Generating test cases...")
    generate_tests()

    logging.debug("tests to be run: %s", test_to_be_run)
    for test_name, test_params in test_to_be_run:
        print()
        print(test_name)
        print("Function\tRuntime [s]")
        for func in functions_to_be_tested:
            fact_buffer.clear()
            bi_buffer.clear()
            sparse_fact_buffer.clear()
            try:
                print(func.__name__, end="\t")
                start = time.process_time()
                for (x, y) in test_params:
                    bi = func(x, y)
                    if check_results:
                        assert(results[(x, y)] == bi)
                duration = time.process_time() - start
                print("{:.5f}".format(duration))
            except MemoryError:
                print("out of memory")


if __name__ == "__main__":
    main()
