import multiprocessing # See https://docs.python.org/3/library/multiprocessing.html
import argparse # See https://docs.python.org/3/library/argparse.html
import random
from math import pi
import time
import matplotlib.pyplot as plt



def sample_pi(n):
    """ Perform n steps of Monte Carlo simulation for estimating Pi/4.
        Returns the number of sucesses."""
    random.seed()
    print("Hello from a worker")
    s = 0
    for i in range(n):
        x = random.random()
        y = random.random()
        if x**2 + y**2 <= 1.0:
            s += 1
    return s


def compute_pi(args):
    random.seed(1)
    n = int(args.steps / args.workers)
    
    p = multiprocessing.Pool(args.workers)
    s = p.map(sample_pi, [n]*args.workers)

    n_total = n*args.workers
    s_total = sum(s)
    pi_est = (4.0*s_total)/n_total
    print(" Steps\tSuccess\tPi est.\tError")
    print("%6d\t%7d\t%1.5f\t%1.5f" % (n_total, s_total, pi_est, pi-pi_est))


def measured_speed(start,end,base,worker):
    baseline=base
    return (baseline/(end-start))

def theoretical_speed(base,worker):
    baseline=base
    return baseline /(baseline/worker) #which means worker



if __name__ == "__main__":
    cores=[1,2,4,8,16,32]
    measured=[]
    theoretical=[]
    for i in cores:
        parser = argparse.ArgumentParser(description='Compute Pi using Monte Carlo simulation.')
        parser.add_argument('--workers', '-w',
                            default=i,
                            type = int,
                            help='Number of parallel processes')
        parser.add_argument('--steps', '-s',
                            default='10000000',
                            type = int,
                            help='Number of steps in the Monte Carlo simulation')
        args = parser.parse_args()
        start=time.time()
        compute_pi(args)
        end=time.time()
        if args.workers==1: baseline=end-start
        measured.append(measured_speed(start,end,baseline,args.workers))
        theoretical.append(theoretical_speed(baseline,args.workers))
    
    fig = plt.figure()
    plt.plot(cores, measured, 'o', label='measured',color='green')
    plt.plot(cores, theoretical,linewidth=3, label='theoretical', color='darkred')
    plt.xlabel('Number of cores')
    plt.ylabel('Speedup')
    plt.legend(loc="upper left")
    plt.margins(0.05)
    fig.savefig('plot.png')    
    plt.show()
    



