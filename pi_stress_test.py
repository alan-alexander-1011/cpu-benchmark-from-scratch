"""
just dont modify the original code, pls, just play fair.

LICENSE For software code and distribution and advertising materials:
 
MIT/GU-NNoA-PEC License

Copyright (c) 2023 alan_alexander

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

After the MIT License terms, the name of alan_alexander SHALL NOT be used in advertising
or to promote the sale, to use or other dealings in this Software without the prior written
of authorization and acceptance from alan_alexander.

The Distributor of this Software is required to provide a clear explanation and conspicuous notice
of any modification made to the original code (the "Software") when distributing their modified version.
This notice should clearly indicate the changes made and provide proper attribution and provide proper
explanation of the changes made to the original version of the Software. And the Distributor may give credits
to the original owner.

----------------------------------------------------------------
"""
import multiprocessing, threading, sys
import math
import time
import os, argparse
from decimal import Decimal as d, getcontext, MAX_PREC
import psutil, platform
from timeit import default_timer as timer
from addtional import *
from colorama import Fore
running = True

score=0.0

os.system("cls") if sys.platform.startswith("win") else os.system("clear")

__all__ = ['calculate_pi', 'calculate_pi_with_threads']

try:
    from numba import jit, cuda
    from numba.core.errors import NumbaDeprecationWarning, NumbaPendingDeprecationWarning
    import warnings 
except ImportError:
    support_conda = False
else:
    __all__.append('calculate_pi_GPU'); __all__.append('calculate_pi_with_threads_on_GPU')
    support_conda = True

if support_conda:
    @jit(target_backend='cuda', forceobj=True)  
    def calculate_pi_GPU(start, end) -> d:
        #Chudnovski's algorithm
        getcontext().prec = 100  # Set the precision to desired value
        pi = d(0)

        for k in range(start, end):
            numerator = d((-1) ** k) * math.factorial(6 * k) * (13591409 + 545140134 * k)
            denominator = math.factorial(3 * k) * (math.factorial(k) ** 3) * (640320 ** (3 * k))
            pi += d(numerator) / d(denominator)

        return pi

def arccot(x, unity):
    sum = xpower = unity // x
    n = 3
    sign = -1
    while 1:
        xpower = xpower // (x*x)
        term = xpower // n
        if not term:
            break
        sum += sign * term
        sign = -sign
        n += 2
    return sum

def calculate_pi(start, end, queue):
    score = 0.0
    # Chudnovski's algorithm
    pi = d(0)
    time = round(timer(), 2)
    for k in range(int(start), int(end)):
        numerator = d((-1) ** k) * math.factorial(6 * k) * (13591409 + 545140134 * k)
        denominator = math.factorial(3 * k) * (math.factorial(k) ** 3) * (640320 ** (3 * k))
        pi += d(numerator) / d(denominator)


    score += 100000 / time
    queue.put(score)  # Put the score into the queue instead of returning it


def calculate_pi_with_threads(num_threads, iterations_multiplier, gpu_bool=False):
    try:
        calc_func = calculate_pi if not gpu_bool and not support_conda else calculate_pi_GPU
        num_iterations = 10 ** iterations_multiplier
        chunk_size = num_iterations // num_threads
        results = []
        pi=[]
        processes = []
        queue = multiprocessing.Queue()  # Create a queue to collect results

        tasks = [(j*chunk_size, (j + 1)*chunk_size) for j in range(num_threads)]
        for task in tasks:
            start, end = task
            process = multiprocessing.Process(target=calc_func, args=(start, end, queue))  # Pass the queue as an argument
            process.start()
            processes.append(process)
        
        for process in processes:
            process.join()
        
        while not queue.empty():  # Retrieve results from the queue
            results.append(queue.get())
        
    except KeyboardInterrupt:
        for process in processes:
            process.terminate()
            process.join()
        print("Exited by interruption.")
        exit(1)

    return results
    # pi_estimate
if __name__ == "__main__":
    multiprocessing.freeze_support()
    print("Welcome to the PI stress test for your CPU/GPU.")
    print("Made by alan_alexander. With a customized License(MIT/GU-NNoA-PEC License).")
    print(f"GPU Benchmark Supported(just for NVIDIA CUDA supported GPU.): {'Yes' if support_conda else 'No'}")
    try:
        if support_conda:
            a = input("Type 'yes' if you want to run this on your NVIDIA gpu.").lower() == "yes"
        else:
            a = False
            input("press enter to continue...")
    except KeyboardInterrupt:
        exit(1)

    col = [Fore.LIGHTYELLOW_EX, Fore.RESET]

    ops = [f"Low: {col[0]}10 000{col[1]} numbers of pi", f"Low-Med: {col[0]}17 000{col[1]} numbers of pi", f"Medium: {col[0]}25 000{col[1]} numbers of pi", f"Med-High: {col[0]}50 000{col[1]} numbers of pi", f"High: {col[0]}100 000{col[1]} numbers of pi",\
        f"Extreme: {col[0]}1 000 000{col[1]} numbers of pi", f"Mega-Xtreme: {col[0]}10 000 000{col[1]} numbers of pi", f"Ultra-High Xtreme: {col[0]}100 000 000{col[1]} numbers of pi", f"related: {col[0]}20 000 000 000 000{col[1]} numbers of pi",\
            f"CPU Killer: {col[0]}100 000 000 000 000 000{col[1]} numbers of pi", f"MAX: {col[0]}{MAX_PREC}{col[1]} numbers of pi"]
    ans = [10000,17000,25000,50000,100000,1000000,10000000,100000000,20000000000000,100000000000000000,MAX_PREC]
    chosen = arrow_key_menu(ops, "Numbers of pi:")

    getcontext().prec = ans[chosen]

    ops = [f"Low: {col[0]}10{col[1]} threads", f"Low-Med: {col[0]}20{col[1]} threads", f"Medium: {col[0]}45{col[1]} threads", f"Med-High: {col[0]}75{col[1]} threads", f"High: {col[0]}128{col[1]} threads",\
        f"Extreme: {col[0]}196{col[1]} threads", f"Ultra-High: {col[0]}256{col[1]} threads", f"Ultra-High Xtreme: {col[0]}512{col[1]} threads", f"CPU Killer: {col[0]}1024{col[1]} threads", "Custom"]
    ans = [10,20,45,75,128,196,256, 512, 1024]
    chosen = arrow_key_menu(ops, "Numbers of threads:")
    if chosen+1 > len(ans):
        no_threads = custom_int_counter(1, -1, "Numbers of threads:")
    else:
        no_threads = ans[chosen]

    ops = ["Low: n=4", "Low-Med: n=5", "Medium: n=6", "Med-High: n=8", "High: n=10",\
        "Extreme: n=15", "Ultra-High: n=20", "Ultra-High Xtreme: n=35", "CPU Killer: n=50", "Custom"]
    ans = [4,5,6,8,10,15,20,35,50]
    chosen = arrow_key_menu(ops, "Iteration multiplier (10^n | 10**n):")
    if chosen+1 > len(ans):
        iterations_multiplier = custom_int_counter(1, -1, "Iteration multiplier:")
    else:
        iterations_multiplier = ans[chosen]

    sys.stdout.write("\033[H\033[J")
    sys.stdout.write("Benchmark is running, please don't quit this program.\n\n")
    sys.stdout.flush()
    time.sleep(1)
    start = round(timer(), 2)

    sc = calculate_pi_with_threads(no_threads, iterations_multiplier, a)

    end = round(timer(), 2)
    try:
        print(f"Elapsed time: {end - start}\nScore: {col[0]}{sum(sc)}{col[1]} , depends how fast your computer completes a cycle of calculating pi")
    except Exception as e:
        print(str(e))
        sys.stdout.flush()
    sys.stdout.flush()
