import matplotlib.pyplot as plt

def CalculateFlowAndVolume(tid, lys, Ts):
    Flow = []
    Volum = []
    
    for k in range(len(tid)):
        Flow_k = lys[k] - lys[0]
        Flow += [Flow_k]

        if k == 0:
            Volum_k = Volum.append(0)
        else:
            Volum_k = Volum[k-1] + Flow_k * Ts[k]
        Volum += [Volum_k]

    return (Flow, Volum[:-1])
