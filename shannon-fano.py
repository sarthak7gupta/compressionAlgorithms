from bisect import bisect
from collections import Counter
from itertools import accumulate
from math import log2
from sys import argv


def count_and_sort(message):
	return [[k, v, ''] for k, v in sorted(Counter(message).items(), key=lambda x: x[1], reverse=True)]

def split(S):
	if len(S) == 1: return

	a = list(accumulate(x[1] for x in reversed(S)))
	b = len(S) - bisect(a, a[-1] / 2)
	S1, S2 = S[:b], S[b:]

	for i in S1: i[2] += '0'
	for i in S2: i[2] += '1'

	split(S1), split(S2)

# message = "A Shannon–Fano tree is built according to a specification designed to define an effective code table. The actual algorithm is simple: For a given list of symbols, develop a corresponding list of probabilities or frequency counts so that each symbol’s relative frequency of occurrence is known. Sort the lists of symbols according to frequency, with the most frequently occurring symbols at the left and the least common at the right. Divide the list into two parts, with the total frequency counts of the left part being as close to the total of the right as possible. The left part of the list is assigned the binary digit 0, and the right part is assigned the digit 1. This means that the codes for the symbols in the first part will all start with 0, and the codes in the second part will all start with 1. Recursively apply the steps 3 and 4 to each of the two halves, subdividing groups and adding bits to the codes until each symbol has become a corresponding code leaf on the tree."

filename = argv[1]

with open(filename, 'r') as f:
	message = f.read()

l = len(message)

S = count_and_sort(message)
split(S)

freqs = {s[0]: s[1] for s in S}
codes = {s[0]: s[2] for s in S}

# print(freqs)
# print(codes)

H = sum(s[1] * log2(l / s[1]) / l for s in S)
Hc = sum(s[1] * len(s[2]) / l for s in S)
eff = H / Hc

print('Efficiency-', eff)

comp_rat = 8 / H

print('Compression Ratio-', comp_rat)
