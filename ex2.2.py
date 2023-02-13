import sys
import json
import timeit
import matplotlib.pyplot as plt
import threading
threading.stack_size(33554432)
sys.setrecursionlimit(20000)

def func1(arr, low, high):
    if low < high:
        pi = func2(arr, low, high)
        func1(arr, low, pi-1)
        func1(arr, pi + 1, high)
def func2(array, start, end):
    p = array[start]
    low = start + 1
    high = end
    while True:
        while low <= high and array[high] >= p:
            high = high - 1
        while low <= high and array[low] <= p:
            low = low + 1
        if low <= high:
            array[low], array[high] = array[high], array[low]
        else:
            break
    array[start], array[high] = array[high], array[start]
    return high



with open("a2q2.json", "r") as exercise_data:
    data = json.load(exercise_data)

execution_times = []

for i in range(len(data)):
    inputs = data[i][:]
    execution_times.append(timeit.repeat('func1(data_copy, 0, len(data_copy)-1)', setup='data_copy = inputs[:]', globals={'inputs': inputs, 'func1': func1}, repeat=1, number=1))

inputs = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
plt.plot(inputs, execution_times)
plt.xlabel("Inputs")
plt.ylabel("Time")
plt.show()

