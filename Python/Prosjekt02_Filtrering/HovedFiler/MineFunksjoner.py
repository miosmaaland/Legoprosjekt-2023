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
	
	Filtered_IIR = []
	Filtered_IIR.append(a * FilteredValue+ b * Measurement)
		
	return Filtered_IIR

