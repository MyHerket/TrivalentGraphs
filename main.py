from strat2 import *

G1 = b111()
G2 = b12()

Graph = [G2] 
All_graphs =  [Graph]

Graph = build_sub_O2(G2)
Graph.append(G1)
All_graphs.append(Graph)
#-------------------------------------------
"""while(1):
	print("Ingresa la cantidad de vertices blancos hasta la cual quiere construir sus graficas:")
	n = input()
	if int(n)>3:
		build_until_m(All_graphs, int(n))
		for List in All_graphs:
			for g in List:
				g.draw()
		break"""

print(G1.degree([n for n in G1]))
for i in G1: 
	if G1.degree(i) == 1:
		print(i)
print(G1.leaves())