import sys
sys.path.append('/Users/wuchi/Limjunhyoun/twitterapi practice/myvenv/Lib')
import tweepy
def connect_api() :
    secretkey='django-insecure-54_)h8mpwy*j^p0u93^-bqyjtel06#s0ke4uh(br1b_@+yd0yp'
    apikey='GTXHIZKs2B6kpsOwgFvpBmGb1'
    apikeysecret='MiDErYRlw7iPkiFLCK4GBp4sfb7TENBwgIWm6adUVGm0di92Qu'
    accesstoken='1544839648220188672-GhJsKSMc59wsObdotenSMe3eSaJvTTs'
    accesstokensecret='W8qDgUOxOlsaQm4LlnMCGBZv8U4jpjkAvlvIVyP2n1R68'

    # 트위터에 접근하기
    auth = tweepy.OAuthHandler(apikey, apikeysecret)
    auth.set_access_token(accesstoken, accesstokensecret)
    api = tweepy.API(auth, wait_on_rate_limit=True)
    
    return api

def get_tweet_by_keyword(api, keyword) :
    cursor = tweepy.Cursor(api.search_tweets, keyword, tweet_mode = 'extended')
    return cursor.items()
