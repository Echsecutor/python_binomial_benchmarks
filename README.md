# python_binomial_benchmarks
What is the fastest way to compute binomial coefficients in python3?

## Benchmarks ouput:

On some Machine (Ubuntu 16.04.3 (Xenial), Linux 4.4.0-96-generic, x86_64) running python 3.5.2:

    1 evaluations of order 1000
    Function        Runtime [s]
    py_direct       0.00003
    py_buffer       0.00044
    math_fact       0.00012
    buf_fact        0.00049
    sparse_buf_fact 0.00052

    1 evaluations of order 10000
    Function        Runtime [s]
    py_direct       0.00196
    py_buffer       0.02204
    math_fact       0.00732
    buf_fact        0.03957
    sparse_buf_fact 0.02705

    1 evaluations of order 100000
    Function        Runtime [s]
    py_direct       0.00268
    py_buffer       2.12051
    math_fact       0.37641
    buf_fact        out of memory
    sparse_buf_fact 3.05091

    1000 evaluations of order 1000
    Function        Runtime [s]
    py_direct       0.04664
    py_buffer       0.09956
    math_fact       0.03750
    buf_fact        0.01008
    sparse_buf_fact 0.06344

    1000 evaluations of order 10000
    Function        Runtime [s]
    py_direct       3.04249
    py_buffer       7.81648
    math_fact       2.77650
    buf_fact        0.87586
    sparse_buf_fact 1.15784

    100 evaluations of order 100000
    Function        Runtime [s]
    py_direct       16.42086
    py_buffer       out of memory
    math_fact       15.28324
    buf_fact        out of memory
    sparse_buf_fact 8.67895


### Conclusions:

- Only use buffering, if you have many evaluations.
- Buffer factorials rather than the full coefficients.
- Use a sparse buffer, iff memory becomes an issue.

## License

Copyright 2017 Sebastian Schmittner <sebastian@schmittner.pw>

<img alt="GPLV3" style="border-width:0" src="http://www.gnu.org/graphics/gplv3-127x51.png" /><br />

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.
