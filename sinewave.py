#!/usr/bin/python

import numpy as np
from matplotlib import pylab

def mksine( f,l,samp_freq=44100):
    f=f*1.
    w=2. * np.pi * f
    t=np.linspace(0,l,samp_freq*l)
    y=np.sin(w * t)
    return (t,y)

(t,y)=mksine(440,10)
pylab.plot(t, y)
pylab.show()