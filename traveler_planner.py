from combinations import printCombinations
from combinations_on_list import printCombinationsArray
from depth_first_traversal import find_all_paths2
from permutations_origin import printPermutationsOrigin
from permutations_origin import gimmePermutationsOrigin
from collections import defaultdict
from random import uniform
from list_of_dates import printListOfDates
from graph import Graph
import timeit

graph = {'MADRID': ['GRECE','LISBONNE'],
             'GRECE': ['LISBONNE','MADRID'],
             'LISBONNE': ['GRECE','MADRID']}

routes = [('MADRID','GRECE'),('MADRID','LISBONNE'),('GRECE','LISBONNE'),('GRECE','MADRID'),('LISBONNE','GRECE'),('LISBONNE','MADRID')]

graph2 = Graph(routes, directed=True)

d = graph2.getDictlist()
print(d)


# print(graph2)
# print(graph)
# print(graph2 == graph)

key1=["MADRID","LISBONNE","GRECE"]

keys = ["MADRID-LISBONNE","LISBONNE-GRECE","GRECE-MADRID", "MADRID-GRECE","GRECE-LISBONNE","LISBONNE-MADRID"]
dictLists = {key:[int(round(uniform(20, 180))) for _ in range(5)] for key in keys}


#def printAll(keys,dictLists,dateList):


def printRoutePossibilities(keys):
	for n in printCombinationsArray(keys):
		s = list(n)[0]
		d= list(n)[1]
		yield find_all_paths2(graph,s, d)[0]

def printRoutesAndStepsForEach(keys):
	for n in printRoutePossibilities(keys):
		#print(list(n),"possibility")
		for a, b in printPermutationsOrigin(n):
			yield a + "-"+b
		print("permutation origin finished")

#print(key1[0] in graph[key1[2]])


def gimmeRoutePossibilities(keys):
	
	def gimme(key):
		for a, b in gimmePermutationsOrigin(key):
			yield a + "-"+b

	listn=[]
	for n in printRoutePossibilities(keys):
		lenN = len(n)
		#print(n,"route possibilities before test")
		#print(n[0] in graph[n[lenN-1]])
		if(n[0] in graph[n[lenN-1]]):
			listn += [list(gimme(n))]

	return(listn)


def printMinPossibility(keys):

	def gimmePossibilities(keys):
		dList = printListOfDates()
		g = gimmeRoutePossibilities(keys)
		#print(dictLists)
		for i in range(0, len(g)):
			yield dictLists[g[i][0]][0] + dictLists[g[i][1]][1] + dictLists[g[i][2]][2]
			print("\n"+"For the possibility " + str(i+1))
			print("Price for " +g[i][0]+" for date ",dList[0]," is ",dictLists[g[i][0]][0],"\n"+"Price for " +g[i][1]+" for date ",dList[1]," is ",dictLists[g[i][1]][1],"\n"+"Price for " +g[i][2]+" for date ",dList[2],"is",dictLists[g[i][2]][2],"\n")
	
	for n in gimmePossibilities(keys):
		if n is not None:
			yield int(n)

def printMin(keys):
	listn=[]
	for n in printMinPossibility(keys):
		listn += [n]
	print(listn,"Sum of the prices in array \n")
	print(min(listn),"Min of the sum \n")
	return min(listn)

#printMin(key1)

#wrapped = wrapper(printMin, key1)

#print(timeit.timeit(wrapped, number=1000))

for n in printRoutesAndStepsForEach(key1):
	print(n)