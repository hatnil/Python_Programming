from pyspark import SparkContext
import argparse
import math
import numpy as np

def produceStats(args):
    sc = SparkContext("local[%d]" % args.cores)
    data = sc.textFile(args.file)
    values = data.map(lambda l: l.split()).map(lambda l: float(l[2]))

    count = values.count()
    summ=values.reduce(lambda a,b: a+b)
    maxx = values.reduce(lambda a, b: max(a, b))
    minn = values.reduce(lambda a, b: min(a, b))
    mean=summ/count

    #stdv=values.stdv() 

    stdv = math.sqrt(values.map(lambda x: (x - mean)**2).reduce(lambda a, b: a + b) / count)
    bins=10
    bin_edges, counts = values.histogram(10)

    # problem2b  optional part
    sorted_values=values.sortBy(lambda x: x).collect()
    if count%2==0:
        median=(sorted_values[int(count/2)] + sorted_values[int(count/2)+1])/2
    else:
        median=sorted_values[int((count-1)/2)]


    print("Sum",summ )
    print("Max :", maxx)
    print("Minimum :", minn)
    print("Mean",mean)
    print("Standard deviation",stdv)
    print("Median",median)
    print("histogram ",(bin_edges, counts))
    

    
 
  

            
if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Calculate statistics using Spark',
        epilog = 'Example: problem2a.py --file assignment3.dat'
    )
    parser.add_argument('--file', '-f',
                        type = str,
                        help=' enter filename')
    parser.add_argument('--cores', '-c',
                        type = int,
                        default = 1,
                        help='Number of cores')
    args = parser.parse_args()
    produceStats(args)