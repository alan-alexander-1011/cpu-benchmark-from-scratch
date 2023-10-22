import multiprocessing
import math
import time
import os, argparse
from decimal import Decimal, getcontext
import psutil

parser = argparse.ArgumentParser()
parser.add_argument('-i', "--iterations", type=int, default=4, help="number of iterations")
parser.add_argument('-p', "--precision", type=int, default=7, help="precision of decimal point")

args = parser.parse_args()

level = args.iterations
precision_multiplier = args.precision

getcontext().prec = 10**precision_multiplier 
def calculate_pi(start, end) -> Decimal:
    getcontext().prec = 100  # Set the precision to desired value
    pi = Decimal(0)
    for k in range(start, end):
        numerator = Decimal((-1) ** k) * math.factorial(6 * k) * (13591409 + 545140134 * k)
        denominator = math.factorial(3 * k) * (math.factorial(k) ** 3) * (640320 ** (3 * k))
        pi += Decimal(numerator) / Decimal(denominator)
    
    return pi

def calculate_pi_with_threads(num_threads, iterations_multiplier):
    
    #setting piority of this program
    psutil.Process().nice(psutil.HIGH_PRIORITY_CLASS) if os.name == 'nt' else os.nice(-19)
    r'''
    i use high priority/-19 niceness but not realtime priority/-20 niceness
    because i want the os to have cpu time and cpu usage to be avalible so that it will a little bit
    more stable for the os.
    '''

    with multiprocessing.Pool(num_threads) as pool:
        num_iterations = 10 ** iterations_multiplier
        chunk_size = num_iterations // num_threads
        results = pool.starmap(calculate_pi, [(i * chunk_size, (i + 1) * chunk_size) for i in range(num_threads)])
        pi_estimate = 1 / (12 * sum(results))

    return pi_estimate

def score(sc: float):
    return int(1000000 / sc)

if __name__ == '__main__':
    try:
        multiprocessing.freeze_support()
        start = round(time.time(), 2)
        calculate_pi_with_threads(61, level)
        end = round(time.time(), 2)
        print(f"Elapsed time: {end - start}\nScore (1000000 / elapsed time): {score(end - start)}")
    except KeyboardInterrupt:
        exit(0)
