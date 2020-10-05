from scipy import integrate
from math import *
import numpy as np
import matplotlib as plt
s = input('Enter : ')
f = lambda x:eval(s)
a = (integrate.quad(f,0,5))
print (a[0])
