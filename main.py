#!/usr/bin/env python

import classifier
import streamer
import requests
from time import strftime, strptime

CLASSIFIER_FILE = 'classifier.pickle'
CONFIG_FILE = 'sentimental.conf'


class NPSStreamer(streamer.Streamer):
    def __init__(self, config_file, classy):
        super(NPSStreamer, self).__init__(config_file) 
        self.classifier = classy
        self.dj_url = "http://localhost:8000/post/"

    def post_to_sentimentron(self, date, score, tweet):
        post_data = {'score': score,
                     'timestamp': date,
                     'message': tweet}
        requests.post(self.dj_url, post_data)

    def callback(self, message):
        date = message['created_at'][4:-11]
        # have: Fri Jan 25 23:07:59 +0000 2013
        # want: 2013-01-25 17:07:11
        date_str = "%b %d %H:%M:%S"
        date = strptime(date, date_str)

        date_str = "2013-%m-%d %H:%M:%S"
        date = strftime(date_str, date)

        #date = parse_date(date)
        text = message['text'].encode('ascii', 'ignore')
        score = self.classifier.classify(text)
        if not score:
            return
        print score, text
        self.post_to_sentimentron(date, score, text)


def new_classifier():
    scored_texts = []
    with open('nps_data.tsv', 'r') as inf:
        for line in inf.readlines():
            [score, comment] = line.rstrip().split('\t')[:2]
            bag = classifier.bag_of_words(comment)
            if not bag:
                continue
            nps = 'detractor'
            if score in ['7', '8']:
                nps = 'passive'
            if score in ['9', '10']:
                nps = 'promoter'
            scored_texts.append((bag, nps))
    c = classifier.NPSClassifier()
    c.train(scored_texts)
    c.save_to_file('CLASSIFIER_FILE')
    return c


if __name__ == '__main__':
    #print "Loading classifier from pickle..."
    #classy = classifier.NPSClassifier.load_from_file(CLASSIFIER_FILE)
    classy = new_classifier()
    stream = NPSStreamer(CONFIG_FILE, classy)
    stream.run()
