'''
Reliability of spike timing.
See e.g. Mainen & Sejnowski (1995) for experimental results in vitro.

R. Brette
'''
from brian import *

# The common noisy input
N=25
tau_input=5*ms
input=NeuronGroup(1,model='dx/dt=-x/tau_input+(2./tau_input)**.5*xi:1')
Min=StateMonitor(input,'x',record=True)

# The noisy neurons receiving the same input
tau=10*ms
sigma=.05
eqs_neurons='''
dx/dt=(1.1+.5*I-x)/tau+sigma*(2./tau)**.5*xi:1
I : 1
'''
neurons=NeuronGroup(N,model=eqs_neurons,threshold=1,reset=0,refractory=5*ms)
neurons.x=rand(N)
spikes=SpikeMonitor(neurons)

@network_operation
def inject():
    neurons.I=input.x[0]
#neurons.I=linked_var(input,'x')

run(500*ms)
raster_plot(spikes)
show()
