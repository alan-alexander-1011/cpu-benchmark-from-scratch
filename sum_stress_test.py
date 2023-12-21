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
import multiprocessing
from addtional import arrow_key_menu, custom_int_counter
import time

# try:
#     from numba import jit, cuda
#     from numba.core.errors import NumbaDeprecationWarning, NumbaPendingDeprecationWarning
# except ImportError as e:
#     support_conda = False
#     print(f"Error importing required module: {e}")
# else:
#     support_conda = True

class Benchmark:
    def __init__(self):
        self.queue = multiprocessing.Queue()

    def sum(self, level: int, timelimit: int):
        start_time = time.perf_counter()
        cycles = 0
        while time.perf_counter() - start_time < timelimit * 60:
            sum(range(10**level))
            cycles += 1
        self.queue.put(cycles)

    def run_benchmark(self):
        ops_levels = ["10**6", "10**7", "10**8", "10**9", "10**10", "10**11", "10**12", "10**13", "10**14", "10**15",
                      "10**16", "10**17", "10**18", "10**19", "10*20", "custom"]
        level_index = arrow_key_menu(ops_levels, "Levels")
        level = level_index + 6 if not ops_levels[level_index].lower() == "custom" else \
            custom_int_counter(min=1, max=1000, start_message="lvl as power of 10")

        ops_times = ["10", "15", "20", "25", "30", "40", "50", "60", "custom"]
        time_index = arrow_key_menu(ops_times, "stress time as min")
        stress_time = custom_int_counter(min=1, max=1000, start_message="stress time as min") if \
            ops_times[time_index].lower() == "custom" else int(ops_times[time_index])

        num_processes = custom_int_counter(min=1, max=10000, start_message="number of process")

        procs = []
        for _ in range(num_processes):
            proc = multiprocessing.Process(target=self.sum, args=(level, stress_time))
            proc.start()
            procs.append(proc)

        print("\n")

        live_timer = time.perf_counter()
        while any(proc.is_alive() for proc in procs):
            elapsed_time = time.perf_counter() - live_timer
            remaining_time = max(0, stress_time * 60 - elapsed_time)
            print(f"Time remaining: {remaining_time:.2f} seconds", end='\r', flush=True)
            time.sleep(1)

        for proc in procs:
            proc.join()
        reses = [] #results
        while not self.queue.empty():
            reses.append(self.queue.get())

        print(f"\n\n\nBenchmark completed. Cycles done in {stress_time} mins, level 10**{level}: {sum(reses)}", end='\r', flush=True)


if __name__ == "__main__":
    benchmark = Benchmark()
    benchmark.run_benchmark()