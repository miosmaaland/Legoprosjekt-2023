# Her skriver du funksjoner som skal brukes i MathCalculations
# Etter å ha skrevet dem her kan du kalle på dem i Main.py filen (De blir automatisk importert)
from ev3dev2.sound import Sound

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
		

def play_tune(light_value):
    sound = Sound()

    # Play different sounds based on light value
    if light_value < 50:
        sound.play_file("low_pitch_sound.wav")
    elif light_value < 100:
        sound.play_file("medium_pitch_sound.wav")
    else:
        sound.play_file("high_pitch_sound.wav")
