import tweepy
import time

# 1st step to add  Consumer API's Key and Secret to able to get twitter data

auth = tweepy.OAuthHandler('kl5Ehf39JCpFfkSV7VHni2fi6','rbIosuLhFi2mCdB8YUhJC6TILcCoGWGg7MjyFHLx5xBBOb6rpd')

# 2nd step to access token Key and Secret
# 
secret=auth.set_access_token('4255368433-sc0Ir8bv8JE9NCezeSSAJxOpG6fEQsQcczsohGJ','ktHfXQhc7RQJINUkSWjoEohgftzladhSw2eQQfrO7WM7q')


api = tweepy.API(auth,wait_on_rate_limit=True,wait_on_rate_limit_notify=True)

'''Function to like recent posts of entered username and entered #tag'''
def twitter_bot():
    user_name = input('Enter Username or Hashtag string only: ')
    if user_name[0].isalpha() or user_name[0] == '@':
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


n=twitter_bot()

'''Function to get your follower and likes his recent no. of posts'''

def get_followers():
    username = input("enter your username : ")
    followers_list = []
    no_of_tweets = 3
    count = 0
    count_loop = 0
    likes = 0


    for follower in tweepy.Cursor(api.followers,screen_name=username).items():
        followers_list.append(follower.screen_name)
        count_loop  +=1


        for tweet in tweepy.Cursor(api.user_timeline, screen_name=followers_list[0], tweet_mode="extended").items(no_of_tweets):
            count +=1
            if count == 1:
                followers_list.pop()
            try:
                print('tweet liked')
                likes += 1
                print(count_loop)
                print(likes,'tweet_liked')
                # print(tweet.screen_name)

                tweet.favorite()
                time.sleep(1)
            except tweepy.TweepError as e:
                print(e.reason)
            except StopIteration:
                break




print(get_followers())