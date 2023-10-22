# pi-stress-test
a pi calculator benchmark that is made from scratch in python.

## How to use:
install newest python with PATH included or not included if you like.\
open your terminal, go to the location that contains the python file\
if PATH included. run **`pip install -r requirements.txt`**\
but if not PATH included, run **`python -m pip install -r requirements.txt`**\
after is installed all required libraries, run **`python pi_stress_test.py`** if you want the original level that takes 15 min depending on the cpu.\
but if you want to set the iterations level yourself then run **`python pi_stress_test.py -i 'level'`** or **`python pi_stress_test.py --iterations 'level'`**\
and if you want to set the iterations level yourself then run **`python pi_stress_test.py -p 'level'`** or **`python pi_stress_test.py --precision 'level'`**\

My CPU i5-12500H score: 1014
this is a stress test so its based on time, the score system is 1000000 / elapsed time
