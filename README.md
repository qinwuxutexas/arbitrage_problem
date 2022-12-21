
A program for arbitrage - find max money value through currancy exchange chain (e.g., USD-> JPY -> EU -> USD).
It uses the Dijkstra’s algorithm to find the money exchange path for each currency with the maximum money value. It is faster than the Bellmon-Ford algorithm.

Author: Q. Xu 
Date: 12/03/2022 
Version: 0.0
Time complexity: O(ELogV), where E is number of edges, V is number of vertices or graph nodes

''' other solutions:
1) Program to Find Out Currency Arbitrage, time cmplexity: o(V^3), V: number of vertices, a Brute solution
    https://www.tutorialspoint.com/program-to-find-out-currency-arbitrage-in-python
2) Bellman-Ford algorithm, time complexity: O(V*E), V: number of vertices, E: number of edges
    https://etrain.github.io/finance/2013/06/08/currency-arbitrage-in-python

'''
