# Her skriver du funksjoner som skal brukes i MathCalculations
# Etter å ha skrevet dem her kan du kalle på dem i Main.py filen (De blir automatisk importert)
# Her skriver du funksjoner som skal brukes i MathCalculations
# Etter å ha skrevet dem her kan du kalle på dem i Main.py filen (De blir automatisk importert)
def EulerForward(IntValue, FunctionValue, TimeStep):
	if len(IntValue) == 1:
		IntValue.append(0)
	else:
		IntValue.append(IntValue[-1] + TimeStep[-1]*FunctionValue[-1])


def FIR_Filter(Measurements, M):
	Filtered_FIR = (sum(Measurements[k-M+1:k+1]) / M)	
	return Filtered_FIR


def IIR_Filter(FilteredValue, Measurement, alfa):
	# Parameters
	a = 1 - alfa
	b = alfa
	
	Filtered_IIR = []
	Filtered_IIR.append(a * FilteredValue+ b * Measurement)
		
	return Filtered_IIR


def Derivation(FunctionValues, TimeStep):
	k = len(FunctionValues)

	if k == 0:
		derivative = 0
	else:
		derivative = (FunctionValues[k] - FunctionValues[k-1]) / TimeStep
	
	return derivative
		
