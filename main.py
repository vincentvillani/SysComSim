from Signal import *
from Channel import *




signalLength = 40
delays = [0, 10, 30]
attenuations = [1, -1, 1]

exponentialStepResponse =  GenerateExponentialStepResponse(1, 0.8, signalLength, 0)

outputSignal = ChannelResponse(delays, attenuations, exponentialStepResponse)


GraphSignal(outputSignal)

#firstSig = GenerateUnitStep(0, signalLength, 1)
#secondSig = GenerateUnitStep(5, signalLength, -1.0)

#stem(exponentialStepResponse.dataArray)
#show()