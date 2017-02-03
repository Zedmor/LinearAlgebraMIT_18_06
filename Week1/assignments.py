import numpy as np
from numpy import array as a
from numpy import matrix as m
from numpy import mat
'''
Problem set 1
Do problems:

23 and 28 from section 1.2
'''


A = mat('[1 2 3;2 5 2;6 -3 1]')
A*m([1,1,1]).T

A = mat('1 1 1;1 1 1;1 1 0')
v = mat('4 5 6').T
A*v

I = np.identity(3)
I
I*v


A = mat('1 2 3;4 5 6;7 8 9')
A[:,0]

A = mat('1 2 3; 2 5 2;6 -3 1')
x = mat('0;0;2')
b = A*x

m([A[0,:]*x, A[1,:]*x, A[2,:]*x])


A[2,:] * x


'''


29 and 30 from section 2.1
'''



'''



20 and 32 from section 2.2

22 and 29 from section 2.3

32 and 36 from section 2.4

7 from section 2.5
'''