

from pypdevs.simulator import Simulator
from models import *

from pypdevs.tracer import Tracers
from tracerX import TracerX

model = CQueue()
sim = Simulator(model)

sim.setTerminationTime(5.0)

# tracer configuation - not able to get my custom tracer "registered" or working
#sim.setVerbose(None)
#sim.tracer.registerTracer(["tracer", "TracerVerbose2", []])
sim.setCustomTracer("tracerX", "TracerX", ["my_output"])

sim.setClassicDEVS()
sim.simulate()

print("Simulation terminated!")

