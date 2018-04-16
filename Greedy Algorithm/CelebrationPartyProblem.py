#Celebration Party Problem
#Greedy Algorithm

#Made by Gaurav Dua

#Description - 
#We have to assume many people coming to a party
#and we have to divide them in such groups so 
#that members of each group have a max difference
#of 2 in age. We have to tell the minimum number 
#of such groups to be formed.

#Input as:
#<n> <d> <a1> <a2> <a3> .... <an>
#n = number of children
#d = max difference in ages in a group
#a1, a2, ..., an = ages of the children

#Input file used : CPPdataset.txt

#Code

import sys

input = sys.stdin.read()
tokens = input.split()
n = int(tokens[0])
d = int(tokens[1])
x = []
for i in range(2,n+2):
	a = int(tokens[i])
	x.append(a)
x.sort()

segments = []

left = 0
while left < n :
	l = x[left]
	r = x[left] + d
	segments.append((l, r))
	left = left + 1
	while left <n and x[left] <= r :
		left = left + 1
print("Minimum number of Groups = ", len(segments))
print("The Groups to be formed: ", segments)