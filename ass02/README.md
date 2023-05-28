![alt text](https://github.com/baeziy/pdc-ass/ass02/image.png?raw=true)
# Assignment 02 Report

This report provides an analysis of a program designed to determine whether points lie inside various geometric shapes. The program consists of three main files: `seq.py`, `mul.py`, and `main.py`. The purpose of this analysis is to evaluate the performance and speedup achieved by the multithreaded version of the program compared to the sequential version.

## File Analysis

### seq.py
- Contains the sequential implementation of the program.
- Defines functions for point-in-polygon and point-in-semicircle calculations.
- Implements the `main()` function to read coordinates from a file, perform the calculations, and update the category counts.

### mul.py
- Represents the multithreaded version of the program.
- Shares similar functions for point-in-polygon and point-in-semicircle calculations as `seq.py`.
- Implements the `main()` function to divide the points into separate lists and assign them to different threads for parallel processing.

### main.py
- Serves as the main driver program to measure the execution time and calculate the speedup.
- Calls `seq.py` and `mul.py` using the `subprocess` module.
- Measures the execution time of each version and calculates the speedup based on the proportion of the program that can be parallelized.

## Output Analysis

The program's output is as follows:

**Sequential Execution:**
- countA: 1458
- countB: 713
- countC: 851
- countNone: 6978

**Multithreaded Execution:**
- Count A: 1458
- Count B: 713
- Count C: 851
- Count None: 6978

The counts obtained from both the sequential and multithreaded versions are identical, indicating that the multithreading implementation is correct.

## Performance Evaluation

### Execution Times
The execution times for each version are as follows:

**Sequential Execution Time:** 1.7416 seconds

**Multithreaded Execution Time:** 0.0943 seconds

### Speedup Calculation
The speedup is calculated as follows:

**Speedup: 3.44**

The speedup of 3.44 indicates that the multithreaded version is approximately 3.44 times faster than the sequential version. Speedup measures the performance improvement gained by parallelizing the program. In this case, the multithreaded version demonstrates a significant improvement in execution time.

## Conclusion

The program successfully showcases the benefits of multithreading in parallelizing point-in-polygon and point-in-semicircle calculations. The multithreaded version outperforms the sequential version, achieving a speedup of 3.44. The implementation effectively utilizes available threads, leading to improved performance. However, it's important to consider factors such as the number of threads, workload nature, and hardware architecture, as the achieved speedup may vary. Overall, the program demonstrates the advantages of parallel execution in enhancing performance.