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

def calc_freq(term_count, sum):
  freq = 0
  term_count = float(term_count)
  freq = term_count / sum
  return freq

def main():
    #sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[1])

    tweets = []
    scores = {}
    hashtags = []
    hashtag_counts = {}
    state_scores = {}
    #for line in sent_file:
    #  term, score = line.split('\t')
    #  scores[term] = int(score)

    for line in tweet_file:
      try:
        tweet_lines = json.loads(line, encoding='utf-8')
	if (tweet_lines['entities']['hashtags'] != None):
            try:
              max_index = len(tweet_lines['entities']['hashtags'])
              counter = 0
              while counter <= max_index:
                hashtags.append(tweet_lines['entities']['hashtags'][counter]['text'])
                counter += 1
            except IndexError:
              # Do nothing...blah blah blah
              pass
      except UnicodeEncodeError:
        # Do nothing, because we don't care about those non-Unicode tweets for now.
        pass
      except KeyError:
        # Do nothing as this seems to indicate the key is either None or missing (non-tweet lines maybe?)
        pass

    for j in range(len(hashtags)-1):
      if hashtags[j] in hashtag_counts:
        tweet_wordcounts[hashtags[j]] += 1
      else:
        tweet_wordcounts[sliced_tweet[j]] = 1
    # Compute sum of each word's count
    tweet_sum = sum(tweet_wordcounts.itervalues())

      for i in range(len(tweets)-1):
        if state in state_scores.keys():
          state_scores[state] += calc_score(tweets[i], scores)
        else:
          state_scores[state] = calc_score(tweets[i], scores)
    #print state_scores
    #for w in sorted(state_scores, key=state_scores.get, reverse=True):
    #  print w, state_scores[w]
      

    #for j in range(len(states)-1):
    #  if states[j] in state_counts:
    #    state_counts[states[j]] += 1
    #  else:
    #    state_counts[states[j]] = 1
    #print state_counts

if __name__ == '__main__':
    main()
