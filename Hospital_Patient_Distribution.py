import math as m
# this class is for anything pertaining to amount of people at a hospital at a given time

def poisson(x):
    """
        :param x: the amount of patients going to the hospital
        :type x: int
        :return: probability of x patients going to hospital in 1 hour period
        :rtype: float
    """
    lam = 6.0
    prob = m.exp(-lam) * ((lam)**x/m.factorial(x))
    return prob
    
