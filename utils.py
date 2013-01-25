#!/usr/bin/env python
import nltk

def bag_of_words(text):
    tokens = nltk.wordpunct_tokenize(text)
    lemma = nltk.WordNetLemmatizer()
    tokens = [lemma.lemmatize(token.lower()) for token in tokens]
    tokens = [token for token in tokens if len(token) >= 6]
    if len(tokens) == 0:
        return None
    return dict([(word, True) for word in nltk.Text(tokens)])

def load_tsv_file(filename):
    nps_scores = []
    with open(filename, 'r') as inf:
        for line in inf.readlines():
            [score, comment] = line.rstrip().split('\t')[:2]
            bag = bag_of_words(comment)
            if not bag:
                continue
            nps = 'detractor'
            if score in ['7', '8']:
                nps = 'passive'
            if score in ['9', '10']:
                nps = 'promoter'
            nps_scores.append((bag, nps))
    return nps_scores

if __name__ == '__main__':
    load_tsv_file('nps_data.tsv')
