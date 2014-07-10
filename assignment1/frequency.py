import sys
import json

def hw():
    print 'Hello, world!'

def lines(fp):
    print str(len(fp.readlines()))

def slice_n_dice(tweet):
  # Eliminate a bunch of non-alpha-numeric characters and lowercase everything
  tweet = tweet.replace('.','')
  tweet = tweet.replace('?','')
  tweet = tweet.replace(':','')
  tweet = tweet.replace('(','')
  tweet = tweet.replace(')','')
  tweet = tweet.replace('#','')
  tweet = tweet.replace('*','')

  split_tweet = tweet.split(' ')
  split_list = []
  for i in range(len(split_tweet)):
	  split_list.append(split_tweet[i])
  return split_list

def print_dict(dict_to_print):
  for i in range(len(dict_to_print)):
    print dict_to_print[i] dict_to_print

def main():
    tweet_file = open(sys.argv[1])

    tweets = []
    tweet_counts = {}

    for line in tweet_file:
      try:
        tweet_lines = json.loads(line, encoding='utf-8')
        if (tweet_lines.get('lang') == 'en'):
          tweets.append(tweet_lines.get('text',''))
      except UnicodeEncodeError:
        # Do nothing, because we don't care about those non-Unicode tweets for now.
        pass

    for i in range(len(tweets)-1):
      sliced_tweet = slice_n_dice(tweets[i])
      for j in range(len(sliced_tweet)-1):
        if sliced_tweet[j] in tweet_counts:
          tweet_counts[sliced_tweet[j]] += 1
        else:
          tweet_counts[sliced_tweet[j]] = 1
    print tweet_counts
    

if __name__ == '__main__':
    main()
