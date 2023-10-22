# cpu benchmark from scratch on python
a cpu benchmark that is made from scratch in python.

## How to use:

for pi calculator pi stress test:
>install newest python with PATH included or not included if you like.\
  open your terminal, go to the location that contains the python file\
  if PATH included. run **`pip install -r requirements.txt`**\
  but if not PATH included, run **`python -m pip install -r requirements.txt`**\
  after is installed all required libraries, run **`python pi_stress_test.py`** if you want the original level that takes 15 min depending on the cpu.\
  but if you want to set the iterations level yourself then run **`python pi_stress_test.py -i 'level'`** or **`python pi_stress_test.py --iterations 'level'`**\
  and if you want to set the iterations level yourself then run **`python pi_stress_test.py -p 'precision multipler'`** or **`python pi_stress_test.py --precision 'precision multipler'`**\
  and if you want to set the iterations level yourself then run **`python pi_stress_test.py -t 'num of threads'`** or **`python pi_stress_test.py --threads 'num of threads'`**\

My CPU i5-12500H score: 1014 (with 10**7 decimal precision, 4 iterations multiplier, 61 processes.)\
this is a stress test so its based on time, the score system is 1000000 / elapsed time
