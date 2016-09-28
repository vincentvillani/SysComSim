import numpy as np
import math
from pylab import *

class Signal:
    
    def __init__(self, length):
        self.length = length
        self.dataArray = np.zeros(length)
        
    
    






def AddSignals(sig1, sig2):
    
    #Are the signals the same length?
    if sig1.length != sig2.length:
        print "Signal.py::addSignals(): signal lengths are different %d vs %d" % (sig1.length, sig2.length)
        exit(1)
    
    #Add the two signals together and return the result    
    result = Signal(sig1.length)    
    
    for i in range(0, sig1.length):
        result.dataArray[i] = sig1.dataArray[i] + sig2.dataArray[i]
        
    return result




def SignalScalarMultiply(signal, scalar):
    
    for i in range(0, signal.length):
        signal.dataArray[i] *= scalar
        
        
        

def DelaySignal(signal, delayD):
    
    if delayD > signal.length:
        print "Signal.py::DelaySignal(): Can't delay greater than the signal length"
        exit(1)
        
    dataArrayCopy = np.copy(signal.dataArray)
    
    for i in range(0, delayD):
        signal.dataArray[i] = 0
    
    for i in range(delayD, signal.length):
        signal.dataArray[i] = dataArrayCopy[i - delayD]
        

def DelaySignalOutOfPlace(signal, delayD):
    
    if delayD > signal.length:
        print "Signal.py::DelaySignal(): Can't delay greater than the signal length"
        exit(1)
        
    result = Signal(signal.length)
    
    for i in range(0, delayD):
        result.dataArray[i] = 0
    
    for i in range(delayD, signal.length):
        result.dataArray[i] = signal.dataArray[i - delayD]
        
    return result



def GenerateUnitStep(delayD, lengthN, amplitudeA = 1):
    
    result = Signal(lengthN)
    
    for i in range(delayD, lengthN):
        result.dataArray[i] = 1.0 * amplitudeA;
        
    return result



def GenerateExponentialStepResponse(amplitudeK, blurringA, lengthN, delayD = 0, offsetC = 0):
    
    result = Signal(lengthN)
    
    #generate the unity unit step response
    unityUnitStepSignal = GenerateUnitStep(delayD, lengthN, 1)
    
    
    #exponentialStepResponse(n) = k(1 - a^(n + 1)unitStep(n)
    #k = changes in amplitude
    #a = blurring of transitions, a < 1.0, closer to one the slower the step response
    exponentIterator = 0
    for i in range(delayD, lengthN):
        result.dataArray[i] = amplitudeK * (1.0 - math.pow(blurringA, exponentIterator + 1)) * unityUnitStepSignal.dataArray[i] + offsetC;
        exponentIterator += 1
        
        
    return result




def GraphSignal(signal):
    
    stem(signal.dataArray)
    show()
    
    