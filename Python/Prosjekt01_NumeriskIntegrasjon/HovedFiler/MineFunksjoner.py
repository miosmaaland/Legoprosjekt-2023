# Her skriver du funksjoner som skal brukes i MathCalculations
# Etter å ha skrevet dem her kan du kalle på dem i Main.py filen (De blir automatisk importert)
def EulerForward(IntValue, FunctionValue, TimeStep):
    IntNewValue = IntValue + (FunctionValue * TimeStep)
    return IntNewValue

    