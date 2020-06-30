import tweepy
import time

# 1st step to add  Consumer API's Key and Secret to able to get twitter data

auth = tweepy.OAuthHandler('********************','******************************')

# 2nd step to access token Key and Secret
# 
secret=auth.set_access_token('*******************','**************************')


api = tweepy.API(auth,wait_on_rate_limit=True,wait_on_rate_limit_notify=True)

def chatbot():
    user_name = input('Enter Username or Hashtag string only: ')
    if user_name[0] == '@':
        # check username if exist then likes his posts

        try:
            u = api.get_user(user_name)
            print(u.id_str)
            print(u.screen_name)
        except tweepy.TweepError as e:
            return e.reason

        for tweet in tweepy.Cursor(api.user_timeline, screen_name=user_name, tweet_mode="extended").items():
            try:
                print('tweet liked')
                tweet.favorite()
                time.sleep(10)
            except tweepy.TweepError as e:
                print(e.reason)
            except StopIteration:
                break
    # check #tag string and likes #tag string like #python,#java,#javascript

    if user_name[0] == '#':

        no_of_tweets = 4
        for tweet in tweepy.Cursor(api.search, user_name).items(no_of_tweets):
            try:
                print('tweet liked')
                tweet.favorite()
                time.sleep(10)
            except tweepy.TweepError as e:
                print(e.reason)
            except StopIteration:
                break
    else:
        return 'please enter username or hashtags only'

n=chatbot()
print(n)

