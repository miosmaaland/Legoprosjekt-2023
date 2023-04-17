# Her skriver du funksjoner som skal brukes i MathCalculations
# Etter å ha skrevet dem her kan du kalle på dem i Main.py filen (De blir automatisk importert)
# Her skriver du funksjoner som skal brukes i MathCalculations
# Etter å ha skrevet dem her kan du kalle på dem i Main.py filen (De blir automatisk importert)
def EulerForward(IntValue, FunctionValue, TimeStep):
    NewIntValue = IntValue + (FunctionValue * TimeStep)
    return NewIntValue


def FIR_Filter(Measurements, M):
	Filtered_FIR = []
	for k in range(len(Measurements)):
		if k == 0:
			# Initial values
			Filtered_FIR = [Measurements[0]]
		else:
			# FIR filter calculation
			if k < M:
				M = k

			Filtered_FIR.append(sum(Measurements[k-M+1:k]) / M)
		
		return Filtered_FIR


def IIR_Filter(FilteredValue, Measurement, alfa):
	# Parameters
	a = 1 - alfa
	b = alfa
	Filtered_IIR = a * FilteredValue+ b * Measurement
		
	return Filtered_IIR


def Derivation(FunctionValues, TimeStep):
    derivative = []
    for i in range(len(FunctionValues)-1):
        derivative = (FunctionValues[i+1] - FunctionValues[i]) / TimeStep
    return derivative

