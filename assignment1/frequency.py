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

def calc_freq(term_count, sum):
  freq = 0
  term_count = float(term_count)
  freq = term_count / sum
  return freq

def main():
    tweet_file = open(sys.argv[1])

    tweets = []
    tweet_wordcounts = {}
    tweet_wordfreqs = {}
    tweet_sum = 0

    # Take each line in the tweet dump and grab just the tweet itself, no metadata.
    for line in tweet_file:
      try:
        tweet_lines = json.loads(line, encoding='utf-8')
        if (tweet_lines.get('lang') == 'en'):
          tweets.append(tweet_lines.get('text',''))
      except UnicodeEncodeError:
        # Do nothing, because we don't care about those non-Unicode tweets for now.
        pass

    # Chop each word in the tweet and compute the sum of the words
    for i in range(len(tweets)-1):
    # Get counts for each word
      sliced_tweet = slice_n_dice(tweets[i])
      for j in range(len(sliced_tweet)-1):
        if sliced_tweet[j] in tweet_wordcounts:
          tweet_wordcounts[sliced_tweet[j]] += 1
        else:
          tweet_wordcounts[sliced_tweet[j]] = 1
    # Compute sum of each word's count
    tweet_sum = sum(tweet_wordcounts.itervalues())

    # Compute the frequency of each word
    for key in tweet_wordcounts:
      tweet_wordfreqs[key] = calc_freq(tweet_wordcounts[key], tweet_sum)
    for k,v in tweet_wordfreqs.items():
      try:
        print "%s %f" % (k, v)
      except UnicodeEncodeError:
        # Not sure how to correct this error
        pass
    

if __name__ == '__main__':
    main()