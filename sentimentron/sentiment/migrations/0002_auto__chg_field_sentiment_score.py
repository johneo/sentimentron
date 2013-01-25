# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Sentiment.score'
        db.alter_column(u'sentiment_sentiment', 'score', self.gf('django.db.models.fields.CharField')(max_length=15))

    def backwards(self, orm):

        # Changing field 'Sentiment.score'
        db.alter_column(u'sentiment_sentiment', 'score', self.gf('django.db.models.fields.IntegerField')())

    models = {
        u'sentiment.sentiment': {
            'Meta': {'object_name': 'Sentiment'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'message': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'score': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            'timestamp': ('django.db.models.fields.DateTimeField', [], {})
        }
    }

    complete_apps = ['sentiment']