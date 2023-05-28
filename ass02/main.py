from subprocess import call
import time


def main():
    seq_start_time = time.time()
    call(["python", "seq.py"])
    seq_stop_time = time.time()
    seq_time = seq_stop_time - seq_start_time
   

    mul_start_time = time.time()
    call(["python", "mul.py"])
    mul_stop_time = time.time()
    mul_time = mul_stop_time - mul_start_time
    

    P = (seq_time - mul_time) / seq_time  # Proportion of program that can be parallelized
    n = 4  # Number of parallel threads

    speedup = 1 / ((1 - P) + (P / n))

    print("--- Sequential Execution Time: %s seconds ---" % seq_time)
    print("--- Multithreaded Execution Time: %s seconds ---" % mul_time)
    print("--- Speedup: %.2f ---" % speedup)



if __name__ == "__main__":
    main()
    
