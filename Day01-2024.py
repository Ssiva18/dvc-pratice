from typing import List

Immutability = 'String and Tuple'

list_values : List = ['siva','Naga','Raju',1998]
list_values[0] ='Boyina'

print(list_values)

#   Tuple dosnt support item assingemnt and supports indexing

Tuple_values = (1,2,3,'siva')
#   Tuple_values[0] = 'Boyina'

print(Tuple_values[0])

#   How to optimize your code.
    #   Optimizing code saves lot of time - just assume u have to run a code 20 times per day.
    #   The code u written have been effeciet and it reduced 1sec so u can save 20sec.

from timeit import repeat, timeit

        #  Points to be remembered.
        #   with in the repeat function the operation has to be passed in string format.
        #   we are doing the list comprehension 1M times and repeating for 5 times.
        #   Disabiling the garbage collector bg to boost the time for execution.
        #   we can do things with time module
import time

start_time: float = time.perf_counter()
...#"putting code here"
end_time: float = time.perf_counter()
print(end_time-start_time)


list_comp = "[i for i in range(10)]"
Normal_comprehension = """
result = []
for i in range(10):
    result.append(i)
"""
list_comp_time = min(repeat(list_comp,repeat =5, number = 1000000))
Nrml_comp_time = min(repeat(Normal_comprehension,repeat =5, number = 1000000))

        #   Timeit does only number of times it doesnt repeat the process.
        #   with in the timeit function the operation has to be passed in string format.
        #   warmup the interpretor with code execution.

list_comp_timeit = timeit(list_comp, number = 1000000)
Nrml_comp_timeit = timeit(Normal_comprehension, number = 1000000)

#   Result with Repeat
print(list_comp_time)
print(Nrml_comp_time)

#   Result with timeit

print(list_comp_timeit)
print(Nrml_comp_timeit)

"""-------------------------"""#Spaceship Operator.

x, y = 1,2 



"""-------------------------"""#NoReturn Never Operator.

from typing import NoReturn
from enum import Enum

#   we use NoReturn or Never when a function doesnt return anything.

def func(msg: str)-> NoReturn:
    raise Exception(msg)
