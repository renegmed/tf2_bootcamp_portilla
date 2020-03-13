import numpy as np 

# Grabbing single element
arr = np.arange(0, 11)
print("arr = np.arange(0, 11): \n{}".format(arr))

print("arr[8]:\n {}".format(arr[8]))


# Grabbing a slice of elements

print("arr[1:5]: \n{}".format(arr[1:5]))

print("arr[0:5]:\n{}".format(arr[0:5]))
print("same as arr[:5]:\n {}".format(arr[:5]))

print("arr[5:]:\n{}".format(arr[5:]))
print("same as arr[5:11]:\n{}".format(arr[5:11]))

arr[0:5] = 100
print("arr[0:5] = 100\n {}".format(arr))


# Broadcasting selections 

   # slice acts as a pointer to origin array
arr = np.arange(0, 11)
print("arr = np.arange(0, 11): \n {}".format(arr))

slice_of_arr = arr[0:5]
print("slice_of_arr = arr[0:5]: \n{}".format(slice_of_arr))

slice_of_arr[:] = 99
print("slice_of_arr[:] = 99, slice_of_arr: \n {}".format(slice_of_arr))
print("arr new value: \n {}".format(arr))

print("-----------")

print("arr original values: \n{}".format(arr))
arr_copy = arr.copy()
print("arr_copy = arr.copy(), arr_copy: \n {}".format(arr_copy))
arr_copy[:] = 100
print("arr_copy[:] = 100, arr_copy: \n{}".format(arr_copy))
print("no change in arr values: \n{}".format(arr))

# Indexing and selection in 2-dimensions

arr_2d = np.array([[5,10,15],[20,25,30],[35,40,45]])
print("arr_2d = np.array([[5,10,15],[20,25,30],[35,40,45]]), arr_2d:\n{}".format(arr_2d))

print("index 1 is rows, index 2 is columns, arr_2d.shape:\n{}".format(arr_2d.shape))

print("arr_2d[0]:\n{}".format(arr_2d[0]))

print("arr_2d[2]:\n{}".format(arr_2d[2]))

print("arr_2d[1][1]:\n{}".format(arr_2d[1][1]))

print("arr_2d[1,1]:\n{}".format(arr_2d[1,1]))

print("arr-2d[0,2]:\n{}".format(arr_2d[0,2]))

# slicing

print("arr_2d[:2]:\n{}".format(arr_2d[:2]))

print("arr_2d[:2,1:]:\n{}".format(arr_2d[:2,1:]))



# Conditional Selection

ar = np.arange(1,11)
print("ar = np.arange(1,11):\n{}".format(ar))

print("arr > 4:\n{}".format(arr > 4))
bool_arr = arr > 4

print("bool_arr = arr > 4:\n{}".format(bool_arr))
print("arr[bool_arr]:\n{}".format(arr[bool_arr]))
# shortcut

print("shortcut arr[arr>4]:\n{}".format(arr[arr>4]))