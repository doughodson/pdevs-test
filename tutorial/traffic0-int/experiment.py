
from pypdevs.simulator import Simulator

from model import TrafficLight

model = TrafficLight("TrafficLight")
sim = Simulator(model)

sim.setTerminationTime(150.0)

sim.setVerbose(None)
sim.setClassicDEVS()
sim.simulate()

print("Simulation terminated!")

