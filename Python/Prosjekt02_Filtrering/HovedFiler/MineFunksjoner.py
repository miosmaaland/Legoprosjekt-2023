def FIR_Filter(Measurements, M):
	Filtered_FIR = (sum(Measurements) / M)	
	return Filtered_FIR


def IIR_Filter(FilteredValue, Measurement, alfa):
	# Parameters
	a = 1 - alfa
	b = alfa
	
	Filtered_IIR = (a * FilteredValue+ b * Measurement)
		
	return Filtered_IIR

