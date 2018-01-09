# header{{{
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import meshfree as mf
import matplotlib.pyplot as plt
from matplotlib import cm
import time
# }}}
# geometry{{{
a = 1.
ndiv = 8
numNode = (ndiv+1)*(ndiv+1)
dmax = 2.5
x = np.zeros((3,numNode))
for j in range(ndiv+1):
    for i in range(ndiv+1):
        iterNode = (ndiv+1)*j + i
        x[0,iterNode] = a/ndiv * i
        x[1,iterNode] = a/ndiv * j
spac = a/ndiv
dm = spac*dmax*np.ones((3,numNode))
# }}}
# consistency condition{{{
inte = 100
xin = np.linspace(0,1,inte)
yin = np.linspace(0,1,inte)
plotu = np.zeros((inte,inte))
xin,yin = np.meshgrid(xin,yin)
timestart = time.clock()
for i in range(inte):
    for j in range(inte):
        gpos = np.array([[xin[i,j],yin[i,j],0]])
        v = mf.finode(gpos,x,dm)
        phi = mf.shape(gpos,x,v,dm)
        plotu[i,j] = np.dot(phi,x[0,v]+x[1,v])
print(time.clock() - timestart)
fig = plt.figure()
ax = fig.gca(projection='3d')
surf = ax.plot_surface(xin,yin,plotu,cmap=cm.coolwarm,linewidth=0,antialiased=False)
plt.show()
# }}}
