# Her skriver du funksjoner som skal brukes i MathCalculations
# Etter å ha skrevet dem her kan du kalle på dem i Main.py filen (De blir automatisk importert)
def EulerForward(IntValue, FunctionValue, TimeStep):
		IntNewValue = IntValue + (FunctionValue * TimeStep)
		return IntNewValue


def FIR_Filter(Measurements, M):
	Filtered_FIR = (sum(Measurements) / M)	
	return Filtered_FIR


def IIR_Filter(FilteredValue, Measurement, alfa):
	# Parameters
	a = 1 - alfa
	b = alfa
	
	Filtered_IIR = (a * FilteredValue+ b * Measurement)
		
	return Filtered_IIR


def Derivation(FunctionValues, TimeStep):
	derivative = (FunctionValues[1] - FunctionValues[0]) / TimeStep
	
	return derivative