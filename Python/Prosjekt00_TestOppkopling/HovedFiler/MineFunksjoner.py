# Funksjon hvor detaljene i beregningene står i funksjonskallet.
# Denne er å foretrekke siden kallet i Main.py gir mye informasjon
def SumBasedOnElements(Arg1, Arg2):
    return Arg1 + Arg2


# Funksjon hvor detaljene i beregningene er kodet i funksjonen
# Denne er ikke å foretrekke siden kallet i Main.py gir lite informasjon
def SumBasedOnLists(Arg1, Arg2, a, k):
    Arg1.append(Arg1[k-1] + a*Arg2[k])

