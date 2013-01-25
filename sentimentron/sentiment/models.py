from collections import namedtuple

from django.db import models


# Generate a histogram of the stats for an entire year (non-leap).
HISTOGRAM = """\
SELECT AVG(sentiment_sentiment.score), 
    DATE(sentiment_sentiment.timestamp)
    FROM sentiment_sentiment
    GROUP BY DATE(sentiment_sentiment.timestamp)
    LIMIT 365;
"""


class Sentiment(models.Model):
    """An individual record of sentiment."""
    
    score = models.IntegerField()
    timestamp = models.DateTimeField()
    message = models.CharField(max_length=255)
    
    def __unicode__(self):
        return self.message
    
    @property
    def histogram(self):
        """Return a histogram of the average sentiment on each day"""
        from django.db import connection
        cursor = connection.cursor()
        cursor.execute(HISTOGRAM, [self.pk])
        Day = namedtuple('Day', 'score timestamp')
        return map(Day._make, cursor.fetchall())
