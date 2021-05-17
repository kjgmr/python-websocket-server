import numpy as np
from multiprocessing import Queue

test_q = Queue()
for i in range(20):
    test_q.put(i)

current_val = test_q.get()
prev_val = current_val
cum_list = []
while current_val + prev_val < 16:
    cum_list.append(current_val)
    prev_val = current_val
    current_val = test_q.get()

print(cum_list)
print(f'current_val = {current_val:.0f}')
print(f'prev_val = {prev_val:.0f}')
