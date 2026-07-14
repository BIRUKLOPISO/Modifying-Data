import numpy as np

my_array1 = np.array("A")
my_array2 = np.array(["A","B","C"])
my_array3 = np.array([["A","B","C"],["D","E","F"],["1","2","3"]])
my_array4 = np.array([[[[1,3,1],[2,4,2]],
                        [[1,5,1],[2,6,2]],
                        [[1,5,1],[2,6,2]],
                        [[1,5,1],[2,6,2]]],

                       [[[1,3,1],[2,4,2]],
                        [[1,5,4],[2,6,5]],
                        [[1,5,4],[2,6,5]],
                        [[1,5,0],[2,6,0]]]])

print(my_array1.ndim)
print(my_array2.ndim)
print(my_array3.ndim)
print(my_array4.ndim)
print(my_array4.shape)
print (my_array4[0,0,0,0])
print (my_array4[0,2,1,1])

num_sum = (my_array4[0,2,1,1]) + (my_array4[0,0,0,0]) + (my_array4[0,2,0,1])
print(num_sum)