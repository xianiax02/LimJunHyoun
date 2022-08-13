from rest_framework.views import APIView
from django.conf import settings
import tweepy
from common.views import connect_api, get_tweet_by_keyword
from django.http import HttpResponse
from pprint import pprint

# Create your views here.
