import sys
import json

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
        tweets.append(tweet_lines.get('text','').encode('utf-8'))
        pass

    for i in range(len(tweets)-1):
      print calc_score(tweets[i], scores)

if __name__ == '__main__':
    main()
