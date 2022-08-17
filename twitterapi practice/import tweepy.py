import sys
sys.path.append('/Users/wuchi/Limjunhyoun/twitterapi practice/myvenv/Lib')
import tweepy
from common import *
import json
secretkey='django-insecure-54_)h8mpwy*j^p0u93^-bqyjtel06#s0ke4uh(br1b_@+yd0yp'
apikey='GTXHIZKs2B6kpsOwgFvpBmGb1'
apikeysecret='MiDErYRlw7iPkiFLCK4GBp4sfb7TENBwgIWm6adUVGm0di92Qu'
accesstoken='1544839648220188672-GhJsKSMc59wsObdotenSMe3eSaJvTT'
accesstokensecret='W8qDgUOxOlsaQm4LlnMCGBZv8U4jpjkAvlvIVyP2n1R68'

keyword=input('typekeyword')
api=connect_api()
tweets=get_tweet_by_keyword(api,keyword)
# tweets=parse_tweet_response(tweets)
for a in tweets:
    print(parse_tweet_response(a._json))


# "SECRET_KEY": "django-insecure-54_)h8mpwy*j^p0u93^-bqyjtel06#s0ke4uh(br1b_@+yd0yp",
#     "API_KEY": "GTXHIZKs2B6kpsOwgFvpBmGb1",
#     "API_KEY_SECRET": "MiDErYRlw7iPkiFLCK4GBp4sfb7TENBwgIWm6adUVGm0di92Qu",
#     "ACCESS_TOKEN": "1544839648220188672-GhJsKSMc59wsObdotenSMe3eSaJvTTs",
#     "ACCESS_TOKEN_SECRET": "W8qDgUOxOlsaQm4LlnMCGBZv8U4jpjkAvlvIVyP2n1R68"











