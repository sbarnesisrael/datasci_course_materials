import sys

afinnfile = open(sys.argv[1])
#print afinnfile
scores = {}
for line in afinnfile:
  term, score = line.split('\t')
  scores[term] = int(score)

print scores['abhor']