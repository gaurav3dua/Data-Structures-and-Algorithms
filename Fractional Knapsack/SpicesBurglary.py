#Fractional Knapsack

#Made by Gaurav Dua

#Description - 
#We have to assume that a burglar has entered a spices shop.
#He can steal only a limited amount of spices in his bag.
#He wants to maximise the total loot that he takes away.
#We have to tell him how much quantities of each spice should
#he steal in order to maximise his loot.

#Input as:
#<n> <W> <w1> <v1> <w2> <v2> .... <wn> <vn>
#n = number of different spices
#W = max weight that the thief can steal
#w1, w2, ..., wn = weights available of different spices
#v1, v2, ..., vn = total value of the available quantity of different spices

#Input file used : SBdataset.txt

#Code
import sys

#INPUT
input = sys.stdin.read()
tokens = input.split()

n = int(tokens[0])
W = int(tokens[1])
w = []
v = []
b = 2
for i in range(0,n):
	a = int(tokens[b])
	b = b+2
	w.append(a)
b = 3
for i in range(0, n):
	a = int(tokens[b])
	b = b + 2
	v.append(a)

#Logic
def BestItem(w, v):
	maxValuePerWeight = 0
	bestItem = 0
	for i in range(0, n):
		if(w[i]>0):
			if (v[i]/w[i])>maxValuePerWeight:
				maxValuePerWeight = v[i]/w[i]
				bestItem = i
	return bestItem
def Knapsack(W, w, v):
	amounts = [0] * n
	totalValue = 0
	for i in range(0, n):
		if W == 0:
			return [totalValue, amounts]
		i = BestItem(w, v)
		a = min(w[i], W)
		totalValue = totalValue + a * v[i]/w[i]
		w[i] = w[i] - a
		amounts[i] = amounts[i] + a
		W = W -a
	return [totalValue, amounts]

#OUTPUT
result = Knapsack(W, w, v)
print("Maximum Possible Price = ", result[0])
print("Quantities to be taken : ")
print("Spice\tQty")
for i in range(0, n):
	print(i+1, "\t", result[1][i])