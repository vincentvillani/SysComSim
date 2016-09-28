import numpy as np
from Signal import *

def ChannelResponse(delays, attenuations, unityChannelResponseSignal):
    
    #This is kind of silly, should just calculate the output via a convolution or something
    
    if len(delays) != len(attenuations):
        print "Channel.py::ChannelResponse: delays and attentuation lengths don't match"
        exit(1)
        
    #delays and attentuations should be the same
    inputLength = len(delays)
        
    intermediateResponses = []
    
    #Go through each input step function and calculate the intermediate output
    for i in range(0, inputLength):
        
        #Delay the unityResponse, then apply the attenuation
        currentSignalResponse = DelaySignalOutOfPlace(unityChannelResponseSignal, delays[i])
        SignalScalarMultiply(currentSignalResponse, attenuations[i])
        intermediateResponses.append(currentSignalResponse)
    
    
    #Add all the intermediate responses together and return the result
    result = Signal(unityChannelResponseSignal.length)
    
    
    for i in range(0, inputLength):
        
        result = AddSignals(result, intermediateResponses[i])
    
    
    return result
    