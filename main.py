"""This module computes binomial coefficient in various ways to
determine the most efficient method (fastest) in python.

"""

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


test_to_be_run = []
results = {}


def generate_tests():

    n = 10**4
    k = 5 * 10**3
    test_to_be_run.append(("Single evaluation 10^4",
                           [(n, k)]))
    results[(n, k)] = math_fact(n, k)

    n = 10**5
    k = 5 * 10**4
    test_to_be_run.append(("Single evaluation 10^5",
                           [(n, k)]))
    results[(n, k)] = math_fact(n, k)

    test_params = []
    n_test_points = 10000
    for i in range(n_test_points):
        n = randint(10, 1000)
        k = randint(1, n)
        test_params.append((n, k))
        results[(n, k)] = math_fact(n, k)
    test_to_be_run.append(("{} evaluations of order 10^3".format(
        n_test_points, test_params)))


def main():
    soft, hard = 10**9, 2 * 10**9
    resource.setrlimit(resource.RLIMIT_AS, (soft, hard))

    print("Generating test cases...")
    generate_tests()

    for (test_name, test_params) in test_to_be_run:
        fact_buffer.clear()
        bi_buffer.clear()
        print(test_name)
        print("Function\tRuntime [s]")
        for func in functions_to_be_tested:
            start = time.process_time()
            for (x, y) in test_params:
                bi = func(x, y)
                assert(results[(x, y)] == bi)
            duration = time.process_time() - start
            print("{}\t{:.5f}".format(func.__name__, duration))


if __name__ == "__main__":
    main()
