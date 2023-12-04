import numpy as np
import random

arr1d = np.array([1, 2])
print("arr.size:", arr1d.size)

arrRange = np.arange(5)
print("arrRange:", arrRange)

arrRandom = np.random.random(10)
print("arrRandom:", arrRandom)

arrZeroes = np.zeros(5)
print("arrZeroes:", arrZeroes)

arrOnes = np.ones(5)
print("arrOnes:", arrOnes)

arr2d = np.array([[0,2],[1,3]])
print("arr2d:", arr2d)

arrRandom2d = np.random.random((2,2))
print("arrRandom2d:", arrRandom2d)

arrRandInt2d = np.random.randint(0,10,(2,2))
print("arrRandInt2d:", arrRandInt2d)

arrZeroes2d = np.zeros((2,2))
print("arrZeroes2d:", arrZeroes2d)

print("arr2d.shape:", arr2d.shape)
print("arr2d.ndim:", arr2d.ndim)
print("arr2d.size:", arr2d.size)

arr0d = np.array(1)
print("arr0d.size:", arr0d.size)
print("arr0d.ndim:", arr0d.ndim)
print("arr0d.shape:", arr0d.shape)

arrZeroes2d_reshaped = arrZeroes2d.reshape((1,4))
print("arrZeroes2d_reshaped.size:", arrZeroes2d_reshaped.size)

arrZeroes2d_reshaped = arrZeroes2d.reshape(1,4)
print("arrZeroes2d_reshaped.shape:", arrZeroes2d_reshaped.shape)

arr1d = np.arange(10)
arr1d_sliced = arr1d[::2]
print("arr1d:", arr1d)
print("arr1d_sliced:", arr1d_sliced)

arr1d_reverse = arr1d[::-1]
print("arr1d_reverse:", arr1d_reverse)

condition = (arr1d > 4) & (arr1d < 8)
arr1d_filtered = arr1d[condition]
print("condition:", condition)
print("type(condition):", type(condition))
print("arr1d_filtered:", arr1d_filtered)

arrCondition = np.array([False if random.random() < 0.5 else True for x in range(10)])
arr1d_filtered = arr1d[arrCondition]
print("arr1d_filtered:", arr1d_filtered)

arr2d = np.array([[26, 1, 4], [0, 0, 6], [0, 2, 8], [0, 3, 2]])
print("arr2d[0, 0]:", arr2d[0, 0])
print("type(arr2d[0, 0]):", type(arr2d[0, 0]))
print("arr2d[-1, -1]:", arr2d[-1, -1])
print("arr2d[2, :]:", arr2d[2, :])
print("arr2d[:, 1]:", arr2d[:, 1])
print("type(arr2d[:, 1]):", type(arr2d[:, 1]))
print("arr2d[-2:, -2:]:", arr2d[-2:, -2:])
arrCondition = np.array([False if x % 2 == 0 else True for x in arr2d[:, 1]])
print("arr2d[arrCondition, 1]:", arr2d[arrCondition, 1])
A = arr2d[2:, 1:] # view
print("A:", A)
A[0, 0] = 100
print("A:", A)
print("arr2d[2, 1]:", arr2d[2, 1])
arr2d[2, 1] = 2
print("A[0, 0]:", A[0, 0])
B = arr2d[2:, 1:].copy()
print("B:", B)
arrCondition = arr2d % 2 == 0
print("arrCondition:", arrCondition)
print("arr2d:", arr2d)
print("arr2d[arrCondition]:", arr2d[arrCondition])


t = (0, 1)
print("t[0]:", t[0])
output_array = np.empty_like(arr2d) + 10
print("arr2d + 10:", output_array)


