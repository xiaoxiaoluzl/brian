"""
Separation of an array of synapses into a list of arrays with no
repeated postsynaptic neurons
"""
from numpy import *
from time import time

'''
Testing whether we have repeated indexes.

OPTION 1
--------
x=all(bincount(post)<2)

This is very slow with bincount if the number of synapses is large.
And it's a memory expensive way to do it. In principle, we don't need
memory allocation for this test.

OPTION 2
--------
x=len(unique(post))<len(post)

This is much faster and less memory expensive. But it's still significant
(about 0.25 s for the CUBA example).
'''
Nsyn=100000
post=random.randint(Nsyn,size=160) # post neurons
t1=time()
for _ in range(10000): # 1s with dt=0.1 ms 
    #x=all(bincount(post)<2)
    x=len(unique(post))<len(post)
t2=time()
print t2-t1

'''
Dispatching.

We just use unique repeatedly. It returns indexes of the first occurrence of
each post neuron. We put a flag saying that we processed these indexes and
we iterate.
(Note that here we could save one iteration)

The code prints synapses and corresponding post neurons at each iteration. This
would be replaced by executing the pre or post code in Synapses.
'''
synapses=array([1,2,3,4,5,6,7,8,9],dtype=int) # numbers don't matter
post=array([7,1,3,4,1,3,6,1,2],dtype=int) # post neurons

#k=0 # number of iterations
u,i=unique(post,return_index=True)
print synapses[i],post[i]
while (len(u)<len(post)) & (len(u)>1):
    post[i]=-1 # flag meaning we've processed them
    u,i=unique(post,return_index=True)
    #k+=1
    print synapses[i[1:]],u[1:]
