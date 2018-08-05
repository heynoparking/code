import threading
import random
import numpy as np
import multiprocessing
import time


# thread

def thread_func(x, y, result):
    
    for i in range (0,y.shape[1]):
        for j in range (0,x.shape[0]):
            result[i] += x[j] * y[j][i]


def main():
    # How many thread you want to use
    
    matA = np.random.randint(10, size = (10, 10))
    matB = np.random.randint(10, size = (10, 10))
    result = np.zeros((matA.shape[0],matB.shape[1]),dtype=np.int)
    
    thread_num = 10
    threads = []

    print ("matA")
    print(matA)
    print ("matB")
    print(matB)

    start_time = time.time()

    # Assign job to threads
    for row in range(0,matA.shape[0]):
        # Pass argument to function with tuple
            thread = threading.Thread(target = thread_func, args = (matA[row], matB,result[row]))
            threads.append(thread)

    # run all threads
    for thread in threads:
        thread.start()

    # Wait for threads finish
    for thread in threads:
        thread.join()

    print("Result")
    print(result)

    end_time = time.time()
    print('Time elapsed:\t', end_time - start_time)


    
if __name__ == "__main__":
    main()