
from pypdevs.DEVS import *
from pypdevs.infinity import INFINITY

class TrafficLightMode:
    """
    Encapsulates the system's state
    """

    def __init__(self, current="red"):
        """
        Constructor (parameterizable).
        """
        self.set(current)

    def set(self, value="red"):
        self.__colour=value

    def get(self):
        return self.__colour

    def __str__(self):
        return self.get()

class TrafficLight(AtomicDEVS):
    """
    A traffic light 
    """
  
    def __init__(self, name=None):
        """
        Constructor (parameterizable).
        """
        # Always call parent class' constructor FIRST:
        AtomicDEVS.__init__(self, name)
    
        # STATE:
        #  Define 'state' attribute (initial state):
        self.state = TrafficLightMode("green") 

        # ELAPSED TIME:
        #  Initialize 'elapsed time' attribute if required
        #  (by default, value is 0.0):
        self.elapsed = 0


    def intTransition(self):
        """
        Internal Transition Function.
        """

        state = self.state.get()

        if state == "red":
            return TrafficLightMode("green")
        elif state == "green":
            return TrafficLightMode("yellow")
        elif state == "yellow":
            return TrafficLightMode("red")
        else:
            raise DEVSException(\
                "unknown state <%s> in TrafficLight internal transition function"\
                % state)
  
    def timeAdvance(self):
        """
        Time-Advance Function.
        """
        # Compute 'ta', the time to the next scheduled internal transition,
        # based (typically) on current State.
        state = self.state.get()
        if state == "red":
            return 60 
        elif state == "green":
            return 50 
        elif state == "yellow":
            return 10 
        elif state == "manual":
            return INFINITY 
        else:
            raise DEVSException(\
                "unknown state <%s> in TrafficLight time advance transition function"\
                % state)

