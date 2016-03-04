import sys
from multiprocessing import Pool
from time import time

K = 100000
def CostlyFunction((z,)):
    return CostlyFunctionBetter(z)

def CostlyFunctionBetter(z):
    r = 0
    for k in xrange(1, K+2):
        r += z ** (1 / k**1.5)
    return r

if __name__ == "__main__":
    currtime = time()
    N = 10
    po = Pool(int(sys.argv[1]))
    res = po.imap(CostlyFunction,((i,) for i in xrange(N)))
    w = sum(res)
    print w
    print 'time elapsed:', time() - currtime