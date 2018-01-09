# header{{{
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import meshfreef as mf
import types
import matplotlib.pyplot as plt
from matplotlib import cm
import time
# }}}
# geometry{{{
a = 1.
ndiv = 8
numNode = (ndiv+1)*(ndiv+1)
dmax = 2.5
x = np.zeros((3,numNode),dtype='float32')
for j in range(ndiv+1):
    for i in range(ndiv+1):
        iterNode = (ndiv+1)*j + i
        x[0,iterNode] = a/ndiv * i
        x[1,iterNode] = a/ndiv * j
spac = a/ndiv
dm = spac*dmax*np.ones((3,numNode))
# }}}
# test{{{
gpos = np.zeros(3)
#nip = np.zeros(2)
#ipnode = np.zeros(10)
#mf.finode(gpos,numNode,x,dm)
#b = [1,2,3]
#b = [[1],[2],[3]]
b = [[1,2,3],[4,5,6],[7,8,9]]
print(mf.foo.__doc__)
mf.foo(b)
# }}}
