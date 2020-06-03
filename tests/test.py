import numpy as np
from convexity_check import is_not_concave, is_not_convex

def convex_f(x):
    return x[:,0]**2+x[:,1]**2

def concave_f(x):
    return -x[:,0]**2-x[:,1]**2

def bohachevsky1(x):
    return x[:,0]**2+2*x[:,1]**2-0.3*np.cos(3*np.pi*x[:,0])-0.4*np.cos(4*np.pi*x[:,1])+0.7
def bohachevsky2(x):
    return x[:,0]**2+2*x[:,1]**2-0.3*np.cos(3*np.pi*x[:,0])*np.cos(4*np.pi*x[:,1])+0.3

bounds = np.array([[0,0],[1,1]])
assert is_not_concave(bohachevsky1,2,bounds)
assert is_not_convex(bohachevsky1,2,bounds)
assert is_not_concave(bohachevsky2,2,bounds)
assert is_not_convex(bohachevsky2,2,bounds)
try: 
    assert not is_not_convex(convex_f,2,bounds)
except:
    pass
try: 
    assert not is_not_concave(concave_f,2,bounds)
except:
    pass