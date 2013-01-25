# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Sentiment'
        db.create_table(u'sentiment_sentiment', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('score', self.gf('django.db.models.fields.IntegerField')()),
            ('timestamp', self.gf('django.db.models.fields.DateTimeField')()),
            ('message', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal(u'sentiment', ['Sentiment'])


    def backwards(self, orm):
        # Deleting model 'Sentiment'
        db.delete_table(u'sentiment_sentiment')


    models = {
        u'sentiment.sentiment': {
            'Meta': {'object_name': 'Sentiment'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'message': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'score': ('django.db.models.fields.IntegerField', [], {}),
            'timestamp': ('django.db.models.fields.DateTimeField', [], {})
        }
    }

    complete_apps = ['sentiment']