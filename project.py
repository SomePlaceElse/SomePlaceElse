import twitter
import json

user_count = {}  # A dictionary of {"username" : # of tweets by that username}
myApi=twitter.Api(consumer_key='y4kyDOkiaOEF0VRBhBo2O4E2j',
                  consumer_secret='SxuOj26fmlq3Buh7UuGGs9TDEc1JlVVA0S63gaKl4AM4uvzSAd',
                  access_token_key='54665279-J9uu0N20FXEInUokgTrTCeyzXDJ1bghd0lgL8zwgE',
                  access_token_secret='pQwwdcgUvLe6n2jguoU9mwNKCs9use6IXOoQ2YNVxHxuM')


def main():
    restAPI_query()
    users = topUsers()  #top 10 users.
    for user in users:
        get_timeline(user)


def restAPI_query():
    itemList, queryList = [], []
    query = ''
    with open('Items.txt', 'r') as r:
        for items in r.readlines():
            itemList = items.split(',')
    for idx in range(len(itemList)):
        if not idx:     # idx = 0
            query = itemList[idx].strip()
        else:
            if not idx % 43:    # if idx is a multiple of 43
                queryList.append(query)
                query = ''
            else :
                if idx % 43 == 1:
                    query = itemList[idx].strip()
                else:
                    query += ' OR ' + itemList[idx].strip()
    queryList.append(query)
    geo = ('40.7127', '-74.0059', '25mi')  # City of New York
    MAX_ID = None
    for idx in range(len(queryList)):
        tweets = [json.loads(str(raw_tweet)) for raw_tweet
                  in myApi.GetSearch(queryList[idx], geo, count=200, max_id=MAX_ID, result_type='mixed')]
        if tweets:
            MAX_ID = tweets[-1]['id']
            print '# of tweets from this Query: ', len(tweets)
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
    MAX_ID = None
    list_of_chefs = []
    with open('influential.txt', 'a') as w:
        for itr in range(2):
            bunch_of_statuses = myApi.GetUserTimeline(screen_name=user_name, max_id=MAX_ID, count=200)
            for userStatus in bunch_of_statuses:
                tweet = userStatus.__dict__['_text']
                MAX_ID = userStatus.__dict__['_id']
                w.write(json.dumps(tweet) + '\n')


def get_textFile(user_name):
    MAX_ID = None
    list_of_chefs = []
    with open('influential_plaintext.txt', 'a') as w:
        bunch_of_statuses = myApi.GetUserTimeline(screen_name=user_name, count=10)
        for userStatus in bunch_of_statuses:
            userID = userStatus.__dict__['_user'].id
            tweet = userStatus.__dict__['_text']
            # MAX_ID = userStatus.__dict__['_id']
            w.write(json.dumps(tweet) + '\n')
            # list_of_chefs.append([userID, tweet])
    # print 'Number of tweets crawled', len(list_of_chefs)


if __name__ == '__main__':
    main()
    # get_textFile('grubstreet')
    # get_timeline('MidtownLunch')
    # get_timeline('firstwefeast')
    # get_timeline('ruthreichl')
    # get_timeline('EaterNY')
    # get_timeline('MelissaClark')
    # get_timeline('SplendidTable')
    # get_timeline('TheCooksCook')
    # get_timeline('infatuation')
    # get_timeline('CookingChannel')