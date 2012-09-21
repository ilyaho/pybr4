#!/usr/bin/python

import numpy as np
from matplotlib import pylab

def mksine( f,l,samp_freq=44100):
    f=f*1.
    w=2. * np.pi * f
    t=np.linspace(0,l,samp_freq*l)
    y=np.sin(w * t)
    return (t,y)



def mixtwo(s1,s2):
    return (s1[1]*.5)+(s2[1]*.5)
l=3
(t,y)=mksine(440,l)

s1=mksine(440,l)
s2=mksine(443,l)

s1_s2=mixtwo(s1,s2)

pylab.figure(1)                # the first figure
pylab.subplot(211)             # the first subplot in the first figure
pylab.plot(t, y)
pylab.subplot(212)             # the second subplot in the first figure

pylab.plot(t, s1_s2)           # this is about PYB-2

pylab.show()