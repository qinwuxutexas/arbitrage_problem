# a program for arbitrage problem solution - find max money value through currancy exchange chain (e.g., USD -> EU -> JPY -> USD, starts and ends at the same currency)
# It uses the Dijkstra’s algorithm to find the money exchange path, wich is faster than the Bellmon-Ford algorithm
# author: Q. Xu, Date: 12/03/2022, Version: 0.0
# time complexity: O(ELogV), where E is number of edges, V is number of vertices/nodes
  
import collections
from typing import List
from heapq import *

class arbitrage_solution:
    def __init__ (self, rates: List[List[float]]):
        self.rates = rates
        self.graph = collections.defaultdict (list)
        self.parents = collections.defaultdict (int)
    def build_graph (self):
        row, col = len(self.rates), len(self.rates[0])
        for i in range (row):
            for j in range (0,col):
                if i!=j:
                    self.graph [i].append ((j,self.rates[i][j]))
    
    def dijisktra (self, source: int, source_value: float, option: int): 
        # inputs: source = 0, source_value = 1 for USD, as an example
        max_values_2source = [float ('inf')]*len(self.rates)
        self.build_graph ()
        max_heap = [(-source_value, -source_value, source)] # the maximum money value heap, use negative value to be a "persudo max" since python only has minimum heap
        visited = set ()
        sources = [source]
        parents = collections.defaultdict (int)
        self.parents [source] = None
        
        max_value_paths = collections.defaultdict (list) # list of path which generates higher money value than the source (starting currency)
        while max_heap:
            val_2source, val_own, node = heappop (max_heap)
            if node not in visited:
                visited.add (node)
            for child, rate_node2child in self.graph [node]:
                    max_val_own = val_own*self.rates[node][child]
                    max_value_2source = max_val_own*self.rates[child][source]
                    if max_value_2source < max_values_2source [child] and child not in visited:
                        max_values_2source [child] = max_value_2source
                        self.parents [child]= node
                        if max_value_2source < -source_value:
                            max_value_paths [max_value_2source] = self.construc_path (child, source)
                        heappush (max_heap, (max_value_2source, max_val_own, child))
        return max_value_paths 
      
    def construc_path (self, node, source):
        path = collections.deque ()
        while node is not None:
            path.appendleft (node)
            parent = self.parents [node]
            node = parent
        path.append (source)
        return path
        
    def print_max_value_path (self, max_value_paths):        
        for value, path in max_value_paths.items ():
            print ('max_value - '+ str(-value)+', path: ')
            for i in range (len(path)-1):
                curr_node = path [i]
                print ( str(curr_node) + '->', end =" ")            
            print (str(path[-1])+'\n')
        
def main ():    
    # test examples, currency rates table, rates [i][j] = rates of currency [i]/currency [j], e.g. rate [0][3] = 135 as 1 USD = 135 JPY
            # USD, EU, LB, JPY 
    rates = [
             [1,0.989, 0.829, 134],            
             [1.011,1,0.848,136], 
             [1.201,1.179,1,163],
             [0.0073,0.0072,0.0061,1]
            ]    
    
    source, source_value = 0, rates[0][0]
    option = 1 # 1: return as long as find a path to get value greater than source; 2: find and return the maximum value among all potential paths                                   
    c_arbitrage =arbitrage_solution (rates)
    max_value_paths = c_arbitrage.dijisktra (source, source_value, option)
    c_arbitrage.print_max_value_path (max_value_paths)
    
if __name__ == "__main__":    
    main ()    
    
                                
                    
        
        
        
                
        
