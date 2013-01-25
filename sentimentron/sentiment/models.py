from collections import namedtuple

from django.db import models


# Generate a histogram of the stats for an entire year (non-leap).
HISTOGRAM = """\
SELECT count(*),
    score, 
    DATE(timestamp)
    FROM sentiment_sentiment
    GROUP BY DATE(timestamp), score
    LIMIT 1000;
"""


SCORES = [
    ('Promoter', 'promoter'),
    ('Passive', 'passive'),
    ('Detractor', 'detractor')
]


class Sentiment(models.Model):
    """An individual record of sentiment."""
    
    score = models.CharField(max_length=15, choices=SCORES)
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
        Day = namedtuple('Day', 'count score date')
        days = map(Day._make, cursor.fetchall())
        return [dict(d._asdict()) for d in days]
