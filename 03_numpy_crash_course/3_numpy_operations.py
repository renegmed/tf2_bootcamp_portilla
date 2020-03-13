import numpy as np 

arr = np.arange(0,10)
print("--- initial array, arr : \n {}".format(arr))
print("add each element by 5, arr + 5:\n {}\n".format(arr + 5))


print("--- initial array, arr : \n {}".format(arr)) 
print("substract each element by 2, arr - 2:\n {}\n".format(arr - 2))

print("--- initial array, arr : \n {}".format(arr))
print("double the value of each element,  arr + arr:\n {}\n".format( arr + arr))

print("--- initial array, arr : \n {}".format(arr))
print("multiply each element by itself (square), arr * arr:\n {}\n".format( arr * arr)) 

# zero is replaced by nan

print("--- initial array, arr : \n {}".format(arr))
print("divide each element (note 0/0 = nan),  arr/arr:\n {}\n".format( arr/arr))

# warning (not crashed) 1/0 with inf (infinity) value

print("--- initial array, arr : \n {}".format(arr))
print("1/each element (note 1/0 = infinity),  1/arr:\n {}\n".format(1/arr))


print("--- initial array, arr : \n {}".format(arr))
print("square root each element,  np.sqrt(arr):\n {}\n".format(np.sqrt(arr)))


print("--- initial array, arr : \n {}".format(arr))
print("sine each element,  np.sin(arr):\n {}\n".format(np.sin(arr)))


print("--- initial array, arr : \n {}".format(arr))
print("log each element,  np.log(arr):\n {}\n".format(np.log(arr)))


print("--- initial array, arr : \n {}".format(arr))
print("sum of all the elements,  arr.sum():\n {}\n".format(arr.sum()))


print("--- initial array, arr : \n {}".format(arr))
print("the mean of the array, arr.mean():\n {}\n".format(arr.mean()))


print("--- initial array, arr : \n {}".format(arr))
print("the maximum value of array, arr.max():\n {}\n".format(arr.max()))

print("--- initial array, arr : \n {}".format(arr))
print("variance of array,  arr.var():\n {}\n".format(arr.var()))
 
print("--- initial array, arr : \n {}".format(arr))
print("standard deviation of array, arr.std():\n {}\n".format(arr.std()))

# axis logic

arr2d = np.arange(0,25).reshape(5,5)

print("--- initial 2-d array, arr2d = np.arange(0,25).reshape(5,5) : \n {}".format(arr2d))
print("sum of 2-d array, arr2d.sum():\n {}\n".format(arr2d.sum()))

# rows represented by axis=0. perform operation across the rows
arr2d.sum(axis=0)
print("--- initial 2-d array, arr2d = np.arange(0,25).reshape(5,5) : \n {}".format(arr2d))
print("rows represented by axis=0. perform sum operation across the rows, arr2d.sum(axis=0):\n {}\n".format(arr2d.sum(axis=0)))
# columns represented by axis=1. perform operation across the columns

print("--- initial 2-d array, arr2d = np.arange(0,25).reshape(5,5) : \n {}".format(arr2d))
print("cols represented by axis=1. perform sum operation across the columns, arr2d.sum(axis=1):\n {}\n".format(arr2d.sum(axis=1)))
