
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

        # PORTS:
        #  Declare as many input and output ports as desired
        #  (usually store returned references in local variables):
        self.INTERRUPT = self.addInPort(name="INTERRUPT")

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
  
      def extTransition(self, inputs):
        """
        External Transition Function.
        """
        # Compute the new state 'Snew' based (typically) on current
        # State, Elapsed time parameters and calls to 'self.peek(self.IN)'.
        input = inputs.get(self.INTERRUPT)

        state = self.state.get()

        if input == "toManual":
            if state == "manual":
                # staying in manual mode
                return TrafficLightMode("manual")
            elif state in ("red", "green", "yellow"):
                return TrafficLightMode("manual")
        elif input == "toAutonomous":
            if state == "manual":
                return TrafficLightMode("red")
            elif state in ("red", "green", "yellow"):
                # If toAutonomous is given while still autonomous, just stay in this state
                return self.state
        raise DEVSException(\
            "unknown state <%s> in TrafficLight external transition function"\
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

