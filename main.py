#!/usr/bin/env python

import classifier
import utils

CLASSIFIER_FILE = 'classifier.pickle'
NPS_FILE = 'nps_data.tsv'

def build_classifier(scored_data):
    c = classifier.NPSClassifier()
    c.train(scored_data)
    c.save_to_file(CLASSIFIER_FILE)

def load_classifier(classifier_file):
    return classifier.NPSClassifier.load_from_file(classifier_file)

def main():
    z = utils.load_tsv_file(NPS_FILE)
    build_classifier(z)

def drill():
    from random import shuffle
    scored_texts = utils.load_tsv_file(NPS_FILE)
    #shuffle(scored_texts)
    c = classifier.NPSClassifier()
    bar = int(len(scored_texts) * 0.75)
    shuffle(scored_texts)
    train, test = scored_texts[:bar], scored_texts[bar:]
    c.train(train)
    tested = 0
    correct = 0
    for comment, score in test:
        guessed_score = c.classify(comment)
        print '%8s (%8s) %s' % (guessed_score, score, sorted(comment.keys()))
        tested += 1
        if guessed_score == score:
            correct += 1
    print '\n' * 5
    print "Tested: %d" % tested
    print "Correct: %d" % correct
    print "Accuracy: %0.3f" % (float(correct) / float(tested))
    

if __name__ == '__main__':
    drill()
