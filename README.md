# python_binomial_benchmarks
What is the fastest way to compute binomial coefficients in python3?

## Benchmarks ouput:

On some Machine:

    Single evaluation 10^4
    Function        Runtime [s]
    py_direct       0.02209
    py_buffer       0.02304
    math_fact       0.00816
    buf_fact        0.04683
    sparse_buf_fact 0.03037
    
    Single evaluation 10^5
    Function        Runtime [s]
    py_direct       2.03636
    py_buffer       2.13593
    math_fact       0.64340
    buf_fact        out of memory
    sparse_buf_fact 3.33541
    
    10000 evaluations of order 10^3
    Function        Runtime [s]
    py_direct       3.70327
    py_buffer       8.81274
    math_fact       3.08187
    buf_fact        1.04370
    sparse_buf_fact 1.32884
    
    1000 evaluations of order 10^4
    Function        Runtime [s]
    py_direct       3.71293
    py_buffer       8.59942
    math_fact       3.09752
    buf_fact        1.00833
    sparse_buf_fact 1.31754

Hence for this particular test bed, buffering the factorials is the most efficient way to compute the binomial coefficients.

## License

Copyright 2017 Sebastian Schmittner <sebastian@schmittner.pw>

<img alt="GPLV3" style="border-width:0" src="http://www.gnu.org/graphics/gplv3-127x51.png" /><br />

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.
