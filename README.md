# cpu benchmark from scratch on python
a cpu benchmark that is made from scratch in python.

## How to use:

for pi calculator pi stress test:
>install newest python with PATH included or not included if you like.\
  open your terminal, go to the location that contains the python file\
  if PATH included. run **`pip install -r requirements.txt`**\
  but if not PATH included, run **`python -m pip install -r requirements.txt`**\
  \
  after is installed all required libraries, run **`python pi_stress_test.py`** if you want the original level that takes 15 min depending on the cpu.\
  \
  but if you want to set the iterations multiplier yourself then run **`python pi_stress_test.py -i 'multiplier'`** or **`python pi_stress_test.py --iterations 'multiplier'`**\
  \
  and if you want to set the precision multiplier yourself then run **`python pi_stress_test.py -p 'precision multipler'`** or **`python pi_stress_test.py --precision 'precision multipler'`**\
  \
  and if you want to set the num of threads/processes yourself then run **`python pi_stress_test.py -t 'num of threads/processes'`** or **`python pi_stress_test.py --threads 'num of threads/processes'`**\

My CPU i5-12500H score: 1014 (with 10**7 decimal precision or level 7 precision multiplier, 4 iterations multiplier, 61 processes.)\
this is a stress test so its based on time, the score system is 1000000 / elapsed time
