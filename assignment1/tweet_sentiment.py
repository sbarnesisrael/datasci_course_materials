import sys
import json

def hw():
    print 'Hello, world!'

def lines(fp):
    print str(len(fp.readlines()))

def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    hw()
    #lines(sent_file)
    #lines(tweet_file)
    #scores = {}
    tweets = {}
    #for line in sent_file:
    #  term, score = line.split('\t')
    #  scores[term] = int(score)
    #print scores.items()
    for line in tweet_file:
      tweets = json.loads(line, encoding="UTF-8")
      try:
        print tweets.get('text','')
      except UnicodeEncodeError:
        #print "Got UnicodeEncodeError. Moving on."
        # Do nothing, because we don't care about those non-Unicode tweets for now.
        pass
		
    #print type(json.load(tweet_file))
		
		#r = json.load(tweet_file)
		#r.keys() 'this should show the keys inside the r object

if __name__ == '__main__':
    main()
