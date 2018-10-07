

from pypdevs.DEVS import *
from pypdevs.infinity import INFINITY

class Generator(AtomicDEVS):
    def __init__(self):
        AtomicDEVS.__init__(self, "Generator")
        self.state = True
        self.outport = self.addOutPort("outport")

    def timeAdvance(self):
        if self.state:
            return 1.0
        else:
            return INFINITY

    def outputFnc(self):
        # Our message is simply the integer 5, though this could be anything
        return {self.outport: 5}

    def intTransition(self):
        self.state = False
        return self.state

class Queue(AtomicDEVS):
  def __init__(self):
      AtomicDEVS.__init__(self, "Queue")
      self.state = None
      self.processing_time = 1.0
      self.inport = self.addInPort("input")
      self.outport = self.addOutPort("output")

  def timeAdvance(self):
      if self.state is None:
          return INFINITY
      else:
          return self.processing_time

  def outputFnc(self):
      return {self.outport: self.state}

  def extTransition(self, inputs):
      self.state = inputs[self.inport]
      return self.state

  def intTransition(self):
      self.state = None
      return self.state

class CQueue(CoupledDEVS):
    def __init__(self):
        CoupledDEVS.__init__(self, "CQueue")
        self.generator = self.addSubModel(Generator())
        self.queue = self.addSubModel(Queue())
        self.connectPorts(self.generator.outport, self.queue.inport)


