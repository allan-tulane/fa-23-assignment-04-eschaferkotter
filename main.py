import math, queue
from collections import Counter

####### Problem 3 #######

test_cases = [('book', 'back'), ('kookaburra', 'kookybird'), ('elephant', 'relevant'), ('AAAGAATTCA', 'AAATCA')]
alignments = [('b--ook', 'bac--k'), ('kook-ab-urr-a', 'kooky-bi-r-d-'), ('relev--ant','-ele-phant'), ('AAAGAATTCA', 'AAA---T-CA')]

def MED(S, T):
    # TO DO - modify to account for insertions, deletions and substitutions
    if (S == ""):
        return(len(T))
    elif (T == ""):
        return(len(S))
    else:
        if (S[0] == T[0]):
            return(MED(S[1:], T[1:]))
        else:
            return(1 + min(MED(S, T[1:]), MED(S[1:], T), MED(S[1:], T[1:])))


def fast_MED(S, T, MED={}):
    if (S,T) in MED:
      return MED[(S,T)]
    if (S == ""):
      MED[(S,T)] = len(T)
    elif (T == ""):
      MED[(S,T)] = len(S)
    elif S[0] == T[0]:
      MED[(S,T)] = fast_MED(S[1:], T[1:], MED)
    else:
      MED[(S,T)] = min(fast_MED(S, T[1:], MED), fast_MED(S[1:], T, MED))

    return MED[(S,T)]

def fast_align_MED(S, T, MED={}):
    # TODO - keep track of alignment
    if (S,T) in MED:
      return MED[(S,T)]
    if (S == ""):
      MED[(S,T)] = (len(T), ('-' * len(T), T))
    elif (T == ""):
      MED[(S,T)] = (len(S), (S, '-' * len(S)))
    elif S[0] == T[0]:
      key = fast_align_MED(S[1:], T[1:], MED)
      MED[(S,T)] = (key[0], (S[0] + key[1][0], T[0] + key[1][1]))
    else:
      ins, alignS1, alignT1 = fast_align_MED(S, T[1:], MED)
      dele, alignS2, alignT2 = fast_align_MED(S[1:], T, MED)

      if ins <= dele:
        MED[(S,T)] = (ins + 1, S[0] + alignS1, "-" + alignT1)
      else:
        MED[(S,T)] = (dele + 1, "-" + alignS2, T[0] + alignT2)

    return MED[(S,T)]
  
def test_MED():
    for S, T in test_cases:
        assert fast_MED(S, T) == MED(S, T)
                                 
def test_align():
    for i in range(len(test_cases)):
        S, T = test_cases[i]
        align_S, align_T = fast_align_MED(S, T)
        assert (align_S == alignments[i][0] and align_T == alignments[i][1])
