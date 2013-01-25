#!/usr/bin/env python
import pickle

import nltk
import nltk.classify
from nltk.classify import NaiveBayesClassifier

def bag_of_words(text):
    tokens = nltk.wordpunct_tokenize(text)
    lemma = nltk.WordNetLemmatizer()
    tokens = [lemma.lemmatize(token.lower()) for token in tokens]
    tokens = [token for token in tokens if len(token) >= 6]
    if len(tokens) == 0:
        return None
    bag = dict([(word, True) for word in nltk.Text(tokens)])
    return bag


class NPSClassifier(object):
    
    def __init__(self):
        self._classifier = None

    def train(self, scored_texts):
        # Train classifier on each of the scored texts provided.
        self._classifier = NaiveBayesClassifier.train(scored_texts)

    def classify(self, tweet):
        bag = bag_of_words(tweet)
        if not bag:
            return None
        try:
            return self._classifier.classify(bag)
        except Exception:
            return None

    def save_to_file(self, filename):
        with open(filename, 'wb') as outf:
            pickle.dump(self._classifier, outf, 1)

    @classmethod
    def load_from_file(cls, filename):
        with open(filename) as inf:
            return pickle.load(inf)
