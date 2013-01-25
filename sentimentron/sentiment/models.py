from collections import namedtuple

from django.db import models
from django.contrib import admin


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
    ('promoter', 'Promoter'),
    ('passive', 'Passive'),
    ('detractor', 'Detractor')
]


class Sentiment(models.Model):
    """An individual record of sentiment."""
    
    score = models.CharField(max_length=15, choices=SCORES)
    timestamp = models.DateTimeField()
    message = models.CharField(max_length=255)
    
    def __unicode__(self):
        return self.message
    
    @classmethod
    def histogram(cls):
        """Return a histogram of the average sentiment on each day"""
        from django.db import connection
        cursor = connection.cursor()
        cursor.execute(HISTOGRAM)
        Day = namedtuple('Day', 'value key date')
        days = map(Day._make, cursor.fetchall())
        return [dict(d._asdict()) for d in days]

admin.site.register(Sentiment)
