import collections
import numpy
import random
import re, string, random  
from nltk.stem.wordnet import WordNetLemmatizer
from nltk.corpus import twitter_samples, stopwords
from nltk.tag import pos_tag
from nltk.tokenize import word_tokenize
from nltk import FreqDist, classify, NaiveBayesClassifier
from nltk.metrics.scores import (precision, recall)
import spacy
from pandas import DataFrame, read_csv

class SentimentEstimatorV2:

    def __init__(self, language = 'english'):
        self.train(language)

    def remove_noise(self, tweet_tokens, stop_words = ()):

        cleaned_tokens = []

        for token, tag in pos_tag(tweet_tokens):
            token = re.sub('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+#]|[!*\(\),]|'\
                        '(?:%[0-9a-fA-F][0-9a-fA-F]))+','', token)
            token = re.sub("(@[A-Za-z0-9_]+)","", token)

            if tag.startswith("NN"):
                pos = 'n'
            elif tag.startswith('VB'):
                pos = 'v'
            else:
                pos = 'a'

            lemmatizer = WordNetLemmatizer()
            token = lemmatizer.lemmatize(token, pos)

            if len(token) > 0 and token not in string.punctuation and token.lower() not in stop_words:
                cleaned_tokens.append(token.lower())
        return cleaned_tokens

    def get_all_words(self, cleaned_tokens_list):
        for tokens in cleaned_tokens_list:
            for token in tokens:
                yield token

    def get_tweets_for_model(self, cleaned_tokens_list):
        for tweet_tokens in cleaned_tokens_list:
            yield dict([token, True] for token in tweet_tokens)

    def train(self, language):
        df = read_csv("./dataset/SentiWordNet_3.0.0.tsv", sep="\t", header = 0, index_col='ID')

        labeled = []
        for row in df.iterrows():
            score = 0
            if float(row[1]['NegScore']) > 0 :
                score = float(numpy.tanh(row[1]['PosScore']) / -float(-row[1]['NegScore']))
            else:
                score = float(numpy.tanh(row[1]['PosScore']))
            try:
                tokenized = word_tokenize(row[1]['Gloss'])
            except:
                continue
            
            item = (
                tokenized,
                score
            )
            labeled.append(item)

        stop_words = stopwords.words(language)
        
        # positive_tweet_tokens = twitter_samples.tokenized('positive_tweets.json')
        # negative_tweet_tokens = twitter_samples.tokenized('negative_tweets.json')

        # positive_cleaned_tokens_list = []
        # negative_cleaned_tokens_list = []

        # for tokens in positive_tweet_tokens:
        #     positive_cleaned_tokens_list.append(self.remove_noise(tokens, stop_words))

        # for tokens in negative_tweet_tokens:
        #     negative_cleaned_tokens_list.append(self.remove_noise(tokens, stop_words))

        # labeled_cleaned_tokens_list = self.remove_noise(labeled, stop_words)
        # all_pos_words = self.get_all_words(labeled_cleaned_tokens_list)

        # freq_dist_pos = FreqDist(all_pos_words)

        # positive_tokens_for_model = self.get_tweets_for_model(positive_cleaned_tokens_list)
        # negative_tokens_for_model = self.get_tweets_for_model(negative_cleaned_tokens_list)

        # positive_dataset = [(tweet_dict, "Positive")
        #                         for tweet_dict in positive_tokens_for_model]

        # negative_dataset = [(tweet_dict, "Negative")
                                # for tweet_dict in negative_tokens_for_model]

        dataset = labeled

        random.shuffle(dataset)

        train_data = dataset[:7000]
        test_data = dataset[7000:]
        self.classifier = NaiveBayesClassifier.train(train_data)
        self.total_accuracy = classify.accuracy(self.classifier, test_data)

        self.refsets = collections.defaultdict(set)
        self.testsets = collections.defaultdict(set)
        print('Total accuracy: ',self.total_accuracy)

    def estimate(self, text):
       custom_tokens = self.remove_noise(word_tokenize(text))
       bow = dict([token, True] for token in custom_tokens)
       sentiment = self.classifier.classify(bow)
       accuracy = -1 # precision(self.refsets[sentiment], self.testsets[sentiment])
       return sentiment, accuracy
