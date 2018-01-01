# header{{{
import numpy as np
# }}}
# shape function{{{
def shape(gpos,x,v,dm):
    dif = gpos - x[:,v].T
    p =
    print dif
    return null
# }}}
# find node{{{
def finode(gpos,x,dm):
    dif = np.abs(np.dot(gpos.T,np.ones((1,x.shape[1]))) - x)
    a = dif - dm
    return np.intersect1d(np.intersect1d(
                          np.where(a[0]<=1.e-15),
                          np.where(a[1]<=1.e-15)),
                          np.where(a[2]<=1.e-15))
# }}}
