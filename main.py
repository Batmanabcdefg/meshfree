# header{{{
import numpy as np
import meshfree as mf
# }}}
# {{{
a = 1.
ndiv = 8
numNode = (ndiv+1)*(ndiv+1)
dmax = 1.5
x = np.zeros((3,numNode))
for j in range(ndiv+1):
    for i in range(ndiv+1):
        iterNode = (ndiv+1)*j + i
        x[0,iterNode] = a/ndiv * i
        x[1,iterNode] = a/ndiv * j
spac = a/ndiv
dm = spac*dmax*np.ones((3,numNode))

# test
gpos = np.array([[0,0,0]])
# print np.dot(gpos.T,np.zeros((1,x.shape[1])))
v = mf.finode(gpos,x,dm)
phi = mf.shape(gpos,x,v,dm)
# }}}
