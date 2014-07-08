import sys
import json

def hw():
    print 'Hello, world!'

def lines(fp):
    print str(len(fp.readlines()))

def bigrams(text):
  input_list = text.split(' ')
  bigram_list = []
  for i in range(len(input_list)-1):
    bigram_list.append((input_list[i], input_list[i+1]))
  return bigram_list

def calc_score(tweet, scores):
  sum = 0
  # Eliminate a bunch of non-alpha-numeric characters and lowercase everything
  tweet = tweet.replace('.','')
  tweet = tweet.replace('?','')
  tweet = tweet.replace(':','')
  tweet = tweet.replace('(','')
  tweet = tweet.replace(')','')
  tweet = tweet.replace('#','')

  split_tweet = tweet.split(' ')
  split_list = []
  for i in range(len(split_tweet)):
	  split_list.append(split_tweet[i])

  for i in range(len(split_list)):
    if split_list[i] in scores:
      sum += scores[split_list[i]]
  return sum

def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])

    scores = {}
    tweets = []
    for line in sent_file:
      term, score = line.split('\t')
      scores[term] = int(score)

    for line in tweet_file:
      try:
        tweet_lines = json.loads(line, encoding='utf-8')
        if (tweet_lines.get('lang') == 'en'):
          tweets.append(tweet_lines.get('text',''))
      except UnicodeEncodeError:
        # Do nothing, because we don't care about those non-Unicode tweets for now.
        pass

    for i in range(len(tweets)-1):
      print calc_score(tweets[i], scores)

    #index = 0
    #while index <= len(tweets):
    #  bigrams(tweets[index])
    #  index += 1
    

if __name__ == '__main__':
    main()
