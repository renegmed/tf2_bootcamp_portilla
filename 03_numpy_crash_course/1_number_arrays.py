import numpy as np

mylist = [1,2,3]

print("np.array(mylist) :\n {}".format( np.array(mylist) ))

nested_list = [[1,2], [3,4], [5,6]]

print("nested_list:\n {}".format(nested_list))

print("np.array(nested_list):\n{}".format(np.array(nested_list)))

print("np.arange(0,10):\n {}".format(np.arange(0,10)))

print("with step 2, np.arange(0,11,2):\n {}".format(np.arange(0,11,2)))

print("initial 0 floats, np.zeros(3):\n {}".format(np.zeros(3)))

print("initial 0 floats 2-dimensional, np.zeros(4,10):\n {}".format( np.zeros((4,10)) ) )

print("initial one floats, np.ones(3):\n {}".format(np.ones(3)))

print("initial one floats 2-dimensional, np.ones((4,4)):\n {}".format(np.ones( (4,4) )))

print("np.linspace(0,10,3):\n {}".format( np.linspace(0, 10, 3) ))

print("np.linspace(0,10,20):\n {}".format( np.linspace(0, 10, 20) ))

print("identity matrix np.eye(5): \n{}".format(np.eye(5)))


# Uniform  Distribution,  Random Arrays

print("2 random numbers between 0 aand 1, np.random.rand(2):\n {}".format(np.random.rand(2)))

print("3 rows x 4 columns betwee 0 and 1, np.random.rand(3,4):\n {}".format(np.random.rand(3,4)))


# Standard Normal Distriubtion i.e. mean = 0, variance = 1

print("Normal distribution, np.random.randn(5,5):\n {}".format( np.random.randn(5,5)))

print("Random int, np.random.randint(1, 100, 10):\n {}".format( np.random.randint(1, 100, 10) ))

print("Random int with requested size, np.random.randint(1, 100, (2,3) ):\n {}".format( np.random.randint(1, 100, (2,3) ) ))

# Random number with reproducibility

print("Random with seed, np.random.seed(42):\n {}".format( np.random.seed(42) ) )
print("Seeded random number, np.random.rand(4):\n {}".format( np.random.rand(4) ) )
print("None seeded random number, np.random.rand(4):\n {}".format( np.random.rand(4) ) )


# Reshaing arrays


arr = np.arange(25)
print("arr = np.arande(25):\n{}".format(arr) )
print("arr.shape:\n {}".format(arr.shape))
arr = arr.reshape(5, 5)
print("reahape arr 5 rows x 5 columns, arr.reshape(5, 5):\n {}".format(arr.reshape(5, 5)))

# current shape size is 5 x 5 = 25. Cannot be reshape to size 18
#arr.reshape(3, 6)
#ValueError: cannot reshape array of size 25 into shape (3,6)

ranarr = np.random.randint(0, 20, 10)
print("np.random.randint(0, 20, 10):\n {}".format(np.random.randint(0, 20, 10)))

print("ranarr:\n {}".format(ranarr))
print("ranarr.max():\n {}".format(ranarr.max()))
print("first index location of max arg, ranarr.argmax():\n {}".format(ranarr.argmax()))

print("ranarr.min():\n {}".format(ranarr.min()))
print("first index location of min arg, ranarr.argmin():\n {}".format(ranarr.argmin()))

print("data type of array, ranarr.dtype:\n {}".format(ranarr.dtype))