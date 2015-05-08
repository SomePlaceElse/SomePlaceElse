import twitter
import json

user_count = {}  # A dictionary of {"username" : # of tweets by that username}
myApi=twitter.Api(consumer_key='y4kyDOkiaOEF0VRBhBo2O4E2j',
                  consumer_secret='SxuOj26fmlq3Buh7UuGGs9TDEc1JlVVA0S63gaKl4AM4uvzSAd',
                  access_token_key='54665279-J9uu0N20FXEInUokgTrTCeyzXDJ1bghd0lgL8zwgE',
                  access_token_secret='pQwwdcgUvLe6n2jguoU9mwNKCs9use6IXOoQ2YNVxHxuM')


def main():
    rest_query_ex1()
    rest_query_ex2()
    rest_query_ex3()
    users = topUsers()  #top 10 users.
    for user in users:
        get_timeline(user)


def rest_query_ex1():
    query = '((assault OR fraud OR mugging OR rape OR molest OR vandalism)' \
            'OR (mugger OR shoplifter OR smuggler OR thief OR vandal OR scam)' \
            'OR (commit AND (crime OR battery)))'
    geo = ('40.7127', '-74.0059', '15mi')  # City of New York
    MAX_ID = None
    for it in range(2):
        tweets = [json.loads(str(raw_tweet)) for raw_tweet
                  in myApi.GetSearch(query, geo, count=200, max_id=MAX_ID, result_type='recent')]
        if tweets:
            MAX_ID = tweets[-1]['id']
            print '# of tweets from Query-1: ', len(tweets)
            for tweet in tweets:
                countUser(tweet)
            storeOnFile(tweets)


def rest_query_ex2():
    query = '( ("robbery" OR "murder OR armed OR crime OR suspect) OR arrested)' \
            ' AND ' \
            '(manhattan OR (new AND york AND city) OR NYPD OR NYC OR cops OR police)'
    geo = ('40.7127', '-74.0059', '20mi')  # City of New York
    MAX_ID = None
    for it in range(2):  # Retrieve up to 100 tweets
        tweets = [json.loads(str(raw_tweet)) for raw_tweet
                  in myApi.GetSearch(query, geo, count = 100, max_id = MAX_ID, result_type='mixed')]
        if tweets:
            MAX_ID = tweets[-1]['id']
            print '# of tweets from Query-2: ', len(tweets)
            for tweet in tweets:
                countUser(tweet)
        storeOnFile(tweets)


def rest_query_ex3():
    query = ' (burglary OR murderer OR robbery OR terrorist OR (charged AND with) ) ' \
            'AND (manhattan OR (new AND york AND city) OR (new AND york) OR cops OR police OR NYPD)'

    geo = ('40.7127', '-74.0059', '20mi')  # City of New York
    tweets = [json.loads(str(raw_tweet)) for raw_tweet
              in myApi.GetSearch(query, geo, count = 200, result_type='mixed')]
    if tweets:
        print '# of tweets from Query-3: ', len(tweets)
        for tweet in tweets:
            countUser(tweet)
    storeOnFile(tweets)


def storeOnFile(tweets):
    with open("output.txt", 'a') as writer:
        for tweet in tweets:
            writer.write(json.dumps(tweet['text'])+'\n\n')


def countUser(tweet):
    user_name = tweet['user']['screen_name']
    if user_count.has_key(user_name):   # stores and increases count of tweets per username
        user_count[user_name] = user_count.get(user_name) + 1
    else:
        user_count[user_name] = 1


def topUsers():
    n = 10  # top 10 users
    sorted_users = sorted(user_count.items(), key=lambda (k, v) : v, reverse=True)  #Sort based on Values
    for i in range(n):  # prints Top 10 influential users
        print '# of tweets-per-username'
        print sorted_users[i][1], sorted_users[i][0]
    return [sorted_users[i][0] for i in range(n)]


def get_timeline(user_name):
    statuses = myApi.GetUserTimeline(screen_name=user_name, count=200)
    with open('universe_samarth.txt', 'a') as f:
        for status in statuses:
            f.write(json.dumps(status.text) + '\n')


if __name__ == '__main__':
    main()