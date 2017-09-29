# python_binomial_benchmarks
What is the fastest way to compute binomial coefficients in python3?

## Benchmarks ouput:

On some Machine:

    Function        Runtime [s]
    py_direct       1.21438
    py_buffer       0.17275
    math_fact       0.36779
    buf_fact        0.10847

Hence for this particular test bed, buffering the factorials is the most efficient way to compute the binomial coefficients.

## License

Copyright 2017 Sebastian Schmittner <sebastian@schmittner.pw>

<img alt="GPLV3" style="border-width:0" src="http://www.gnu.org/graphics/gplv3-127x51.png" /><br />

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.
