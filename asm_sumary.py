#!/usr/bin/env python3

import sys

file = sys.argv[1]

def yield_opcode(file):
	with open(file) as f:
		for line in f:
			l = line.split()
			# Check if it's a label.
			# We don't care about label
			if len(l) == 1:
				continue
	
			# Now we check if the instruction have a predicate.
			# We don't care about predicate
			if l[0].startswith('('):
				l.pop(0)
	
			# We are now on form op_code + optionational (execution mask) + ...
			if l[1].startswith('('):
				yield tuple(l[:2])
			else:
				yield tuple(l[:1])

from  collections import Counter
c = Counter(yield_opcode(file))

tot = 0
for k,v in c.most_common():
	print (f"{k}: {v}")
	tot += v

print (f"total: {tot}")