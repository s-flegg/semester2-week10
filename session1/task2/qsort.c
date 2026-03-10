/* qsort() benchmark */

#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <time.h>

const int MAX_VALUE = 999999;
const int DEFAULT_SIZE = 5000;
const int DEFAULT_TRIALS = 5;


void generate_random_numbers(int* data, int size)
{
    srand(time(NULL));

    for (int i = 0; i < size; ++i) {
        data[i] = 1 + rand() % MAX_VALUE;
    }
}


int compare_ints(const void* a, const void* b)
{
    int arg1 = *(const int*)a;
    int arg2 = *(const int*)b;
 
    if (arg1 < arg2) return -1;
    if (arg1 > arg2) return 1;
    return 0;
}


int main(int argc, char* argv[])
{
    int* data;
    int size = DEFAULT_SIZE;
    int num_trials = DEFAULT_TRIALS;
    float total_time = 0.0f;

    if (argc > 1) {
        size = atoi(argv[1]);
    }

    if (argc > 2) {
        num_trials = atoi(argv[2]);
    }

    data = calloc(size, sizeof(int));
    if (data == NULL) {
        fprintf(stderr, "Error: failed to allocate memory\n");
        return 1;
    }

    for (int i = 1; i <= num_trials; ++i) {
        generate_random_numbers(data, size);
        clock_t start_time = clock();
        qsort(data, size, sizeof(int), compare_ints);
        total_time += (float)(clock() - start_time) / CLOCKS_PER_SEC;
        printf("Trial %d done\n", i);
    }

    free(data);

    float average_time = total_time / num_trials;
    printf("%d numbers sorted in %.5f seconds\n", size, average_time);

    return 0;
}
