import numpy as np
from time import time



def is_not_convex(f,num_variables,bounds=None,max_time=1,min_points=1000):
    """
    Input:
        f: a callable function, should take arguments of the form (n,x) where n is the number of samples
        and return a scalar
        num_variables: the number of variables in x
        bounds: optional (2,num_variables) array of bounds for the input variables
    Output:
        result: bool, true if the function is not convex
    Raises:
        TimeoutError
    """
    t0 = time()
    while time()-t0 < max_time:
        if bounds is None:
            pts = np.random.randn(2,min_points,num_variables)
        else:
            pts = (np.random.rand(2,min_points,num_variables)+bounds[0])*(bounds[1]/(1+bounds[0]))
        mean_pt = np.mean(pts,axis=0)
        if np.any((f(pts[0])+f(pts[1]))/2<f(mean_pt)):
            return True
    raise TimeoutError(f"Could not find any counterexamples, function \"{f.__name__}\" may be convex.")

def is_not_concave(f,num_variables,bounds=None,max_time=1,min_points=1000):
    """
    Input:
        f: a callable function, should take arguments of the form (n,x) where n is the number of samples
        and return a scalar
        num_variables: the number of variables in x
        bounds: optional (2,num_variables) array of bounds for the input variables
    Output:
        result: bool, true if the function is not concave
    Raises:
        TimeoutError
    """
    negf = lambda x : -f(x)
    try:
        return is_not_convex(negf,num_variables,bounds,max_time,min_points)
    except:
        raise TimeoutError(f"Could not find any counterexamples, function \"{f.__name__}\" may be concave.")


