import tweepy
import time

# 1st step to add  Consumer API's Key and Secret to able to get twitter data

auth = tweepy.OAuthHandler('************************','************************')

# 2nd step to access token Key and Secret
# 
secret=auth.set_access_token('********-************************','************************')


api = tweepy.API(auth,wait_on_rate_limit=True,wait_on_rate_limit_notify=True)

class Twitter_Bot_Func:

    '''Function to like recent posts of entered username and entered #tag'''

    def like_post(self):
        user_name = input('Enter Username or Hashtag string only: ')
        if (not user_name[0]  =='#') or (user_name[0] == '@'):
            #check username if exist then likes his posts
            try:
                u = api.get_user(user_name)
                print(u.id_str,u.screen_name)
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

        ''' check #tag string and likes #tag string like #python,#java,#javascript '''
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


    def get_followers(self):

        '''Function to get your follower and likes his recent no. of posts'''

        user_name =input("Enter your username : ")
        # check user exist or not
        try:
            u = api.get_user(user_name)
            print(u.id_str, u.screen_name)
        except tweepy.TweepError as e:
            return e.reason

        followers_list = []
        no_of_tweets = 4

        for follower in tweepy.Cursor(api.followers,screen_name=user_name).items():
            followers_list.append(follower.screen_name)

        for screen_names in followers_list:

            for tweet in tweepy.Cursor(api.user_timeline, screen_name=screen_names, tweet_mode="extended").items(no_of_tweets):
                try:
                    print('tweet liked')
                    print('You liked tweet or status of',screen_names)
                    tweet.favorite()
                    time.sleep(10)
                except tweepy.TweepError as e:
                    print(e.reason)
                except StopIteration:
                    break

obj = Twitter_Bot_Func()
obj1 = obj.like_post()
obj2 = obj.get_followers()
print(obj1)
print(obj2)
