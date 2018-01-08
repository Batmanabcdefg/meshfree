# header{{{
import numpy as np
# }}}
# shape function{{{
def shape(gpos,x,v,dm):
    L = v.size
    won = np.ones((1,L))
    nv = x[:,v]
    dif = np.dot(gpos.T,won) - nv
    p = np.concatenate((won,dif[0:2],[dif[0]**2,dif[0]*dif[1],dif[1]**2]),axis = 0)
    w = cubwgt(dif,v,dm);
    B = p*np.array([w,w,w,w,w,w])
    aa = np.zeros((6,6))
    for i in range(L):
        pp = np.dot(p[:,i].reshape(1,6).T,p[:,i].reshape(1,6))
        aa = aa + w[i]*pp
    pg = np.array([1,0,0,0,0,0])
    invaa = np.linalg.inv(aa)

    return np.dot(np.dot(pg,invaa),B)
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
# cubwgt{{{
def cubwgt(dif,v,dm):
    L = v.size
    w = np.zeros(L)
    for i in range(L):
        rx = abs(dif[0,i])/dm[0,v[i]]
        ry = abs(dif[1,i])/dm[1,v[i]]
        if rx > 1:
            wx = 0
        elif rx < 0.5:
            wx = (2./3) - 4*rx**2 + 4*rx**3
        else:
            wx = (4./3) - 4*rx + 4*rx**2 - (4./3)*rx**3
        if ry > 1:
            wy = 0
        elif ry < 0.5:
            wy = (2./3) - 4*ry**2 + 4*ry**3
        else:
            wy = (4./3) - 4*ry + 4*ry**2 - (4./3)*ry**3
        w[i] = wx*wy
    return w
# }}}
