#Implement the Map-Reduce program for the summary statistics and histogram taking input and producing output

from mrjob.job import MRJob
import statistics
import math
import numpy as np
import time
import tempfile
from mrjob.step import MRStep



class stat_summary(MRJob):
    def mapper(self,_, line):
        yield None, float(line.split('\t')[2])
           

    def reducer_stat(self, _, values):
        data=list(values)
        count=0
        sum_all=0
        min_all=np.inf
        max_all=-np.inf
        for i in data:
            count=count+1
            sum_all=sum_all+i
            if min_all>i: min_all=i
            if max_all<i: max_all=i

        first_edge, last_edge = min_all, max_all
        bins = 10
        bin_width=(last_edge-first_edge)/bins
        bin_edges = np.linspace(start=first_edge, stop=last_edge,num=bins + 1, endpoint=True).tolist()
        
        bin_counts = [0]*bins
        for data_point in data:
            for i in range(len(bin_edges)-1):
                if i==0:
                    if data_point>=bin_edges[0] and data_point<bin_edges[1]: bin_counts[0] += 1
                else :
                    if data_point>bin_edges[i] and data_point<=bin_edges[i+1]:
                     bin_counts[i] += 1

        ### problem 1e optional part
        data=sorted(data)  
        if count % 2 == 0:     
            median = (data[int(count / 2)] + data[int(count / 2)+1]) / 2    
        else:
            median = (data[int(count / 2)]) 
        
        yield "sum", sum_all
        yield "mean", sum_all/count
        yield "min", min_all
        yield "max", max_all
        yield "median", median
        yield "standard deviation", statistics.stdev(data)
        yield "hist", (bin_counts,bin_edges)

    def steps(self):
            return [
                MRStep(mapper=self.mapper,
                       reducer=self.reducer_stat)
            ]

if __name__ == '__main__':
    #tempfile.tempdir = '/data/tmp'
    stat_summary.run()



