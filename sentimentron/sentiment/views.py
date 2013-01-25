import json

from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from django.http import HttpResponse
from django import forms

from sentimentron.sentiment.models import Sentiment


class SentimentForm(forms.ModelForm):
    class Meta:
        model = Sentiment


def index(request):
    ctx = {}
    return render(request, 'index.html', ctx)

def data(request):
    data = json.dumps(Sentiment.histogram())
    return HttpResponse(data, mimetype='application/json')


@csrf_exempt
@require_http_methods(["POST"])
def add_sentiment(request):
    form = SentimentForm(request.POST)
    if form.is_valid():
        form.save()
        return HttpResponse(json.dumps({'message': 'Success'}),
                            mime_type="application/json")
    else:
        err = {'errors': form.errors.as_text()}
        return HttpResponse(json.dumps(err),
                            mime_type="application/json",
                            status=400)
    
        