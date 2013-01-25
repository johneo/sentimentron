import tweetstream
from ConfigParser import SafeConfigParser

#The filter that you would like to apply
SEARCH_TXT = 'One%20Way%20Trigger'

parser = SafeConfigParser()
parser.read('sentimental.conf')
'''
    The conf file should look like this:

    [twit_auth]
    twitter_consumer_secret = <VALUE>
    twitter_consumer_key = <VALUE>
    twitter_access_token_secret = <VALUE>
    twitter_access_token = <VALUE>
'''

def callback(message):

    # this will be called every message
    print message['created_at'], message['user']['description']

configuration = {
    "twitter_consumer_secret": parser.get('twit_auth', 'twitter_consumer_secret'),
    "twitter_consumer_key": parser.get('twit_auth', 'twitter_consumer_key'),
    "twitter_access_token_secret": parser.get('twit_auth', 'twitter_access_token_secret'),
    "twitter_access_token": parser.get('twit_auth', 'twitter_access_token')
}

stream = tweetstream.TweetStream(configuration)

stream.fetch("/1/statuses/filter.json?track=%s" % SEARCH_TXT, callback=callback)

# if you aren't on a running ioloop...
from tornado.ioloop import IOLoop
IOLoop.instance().start()
