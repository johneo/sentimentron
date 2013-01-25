#!/usr/bin/env python
import pickle
import utils

import nltk
import nltk.classify
from nltk.classify import NaiveBayesClassifier

class NPSClassifier(object):
    
    def __init__(self):
        self._classifier = None

    def train(self, scored_texts):
        # Train classifier on each of the scored texts provided.
        self._classifier = NaiveBayesClassifier.train(scored_texts)

    def classify(self, tweet):
        # Given a single tweet, extract the text and rate it.
        return self._classifier.classify(tweet)

    def save_to_file(self, filename):
        with open(filename, 'wb') as outf:
            pickle.dump(self._classifier, outf, 1)

    @classmethod
    def load_from_file(cls, filename):
        with open(filename) as inf:
            return pickle.load(inf)
