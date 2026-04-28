# Task 4: Optimization Options

`pgm_tools.c` contains the PGM image manipulation program seen in earlier
weeks of the module.

1. Compile the program without any command line options.

2. Compile the program with minimal optimization, timing how long this takes:

       time gcc -O0 pgm_tools.c

   Make a note of the results.
   real    0m0.109s
   user    0m0.049s
   sys     0m0.022s
   21208

3. Check the size in bytes of the executable. You can do this with

       wc -c a.out

4. Repeat Steps 1 & 2 above, using `-O3` instead of `-O0`. You should find
   that compilation takes a bit longer and the resulting executable is
   slightly larger.
   real    0m0.252s
   user    0m0.140s
   sys     0m0.025s
   21240

5. Repeat Steps 1 & 2, using `-Os` instead of `-O0`, to optimize for space.
   You should see that the resulting executable is significantly smaller
   than before.
   real    0m0.366s
   user    0m0.146s
   sys     0m0.022s
   17128
