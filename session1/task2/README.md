# Task 2: Benchmarking Python & C

## Bubble Sort

1. Examine `bubblesort.py`. This program implements the bubble sort algorithm
   and provides the ability to benchmark it by sorting a list of random
   integer values.

   The size of the list defaults to 5000 but can be changed via the command
   line. The program does 5 separate trials by default, but this number can be
   changed via the command line. The average of the measured execution times
   is displayed as the benchmark.

2. Run the program with no command line arguments. Note the time that it
   displays.

3. Edit `bubblesort.c`. This is the C equivalent of `bubblesort.py`, except
   that sorting algorithm hasn't yet been implemented.

   Replace the two comments inside the function `bubble_sort()` with an
   implementation of the algorithm, using the code from `bubblesort.py` as
   your code.

4. Compile the program. You can do this with `make bubblesort`. Run it and
   compare the results with those from the Python version.

## Other Algorithms

1. Examine `powersort.py`. This is similar to `bubblesort.py`, except that
   it uses Python's built-in list sorting method, which implements the
   [Powersort algorithm][psort].

2. Run `powersort.py` with no command line arguments. Then try specifying
   a much larger list size on the command line. You should see that this is
   much, much faster than bubble sort!

3. Examine `qsort.c`. This is similar to `bubblesort.c`, except that it uses
   [the `qsort()` function][qsfunc] from the C standard library to sort the
   array of integers. The GNU C library (glibc) implementation of this
   function uses a variant of the [quicksort algorithm][qsort].

4. Compile the program. You can do this with `make qsort`. Run the program
   and compare the results with the benchmarks produced by `bubblesort.c`
   and `powersort.py`.

   Why is the `powersort.py` benchmark comparable with that of `qsort.c`?


[psort]: https://en.wikipedia.org/wiki/Powersort
[qsfunc]: https://en.cppreference.com/w/c/algorithm/qsort.html
[qsort]: https://en.wikipedia.org/wiki/Quicksort
