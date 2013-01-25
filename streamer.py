#!/usr/bin/env python
import tweetstream
from ConfigParser import SafeConfigParser
from tornado.ioloop import IOLoop

class Streamer(object):

    def __init__(self, config_file):
        parser = SafeConfigParser()
        parser.read(config_file)
        configuration = {
            "twitter_consumer_secret": parser.get('twit_auth', 'twitter_consumer_secret'),
            "twitter_consumer_key": parser.get('twit_auth', 'twitter_consumer_key'),
            "twitter_access_token_secret": parser.get('twit_auth', 'twitter_access_token_secret'),
            "twitter_access_token": parser.get('twit_auth', 'twitter_access_token'),
        }
        self.stream = tweetstream.TweetStream(configuration)
        search_for = parser.get('filter', 'search_for')
        url = "/1/statuses/filter.json?track=%s" % search_for
        self.stream.fetch(url, callback=lambda message:self.callback(message))

    def callback(self, message):
        print message['created_at'], message['user']['description']

    def run(self):
        IOLoop.instance().start()

if __name__ == '__main__':
    s = Streamer('sentimental.conf')
    s.run()
