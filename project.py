import twitter
import json

user_count = {}  # A dictionary of {"username" : # of tweets by that username}
'''
    item_set = Keeps record of the itemSet generated so far, in the end, dumps it into data.bucket
    queryList = List of all the Queries disjoint by 550-some characters.
'''
item_set, queryList, input_user_item = [], [], []

INPUT_USERNAME = 'testspe'
def setINPUT_USERNAME(user_name):
    INPUT_USERNAME = user_name


myApi=twitter.Api(consumer_key='y4kyDOkiaOEF0VRBhBo2O4E2j',
                  consumer_secret='SxuOj26fmlq3Buh7UuGGs9TDEc1JlVVA0S63gaKl4AM4uvzSAd',
                  access_token_key='54665279-J9uu0N20FXEInUokgTrTCeyzXDJ1bghd0lgL8zwgE',
                  access_token_secret='pQwwdcgUvLe6n2jguoU9mwNKCs9use6IXOoQ2YNVxHxuM')


def main():
    restAPI_query()
    users = topUsers()  #top 20 users.
    for user in users:
        get_timeline(user)
        createItemSet(user)
    '''
        This is the part where the input taken from user will be set to method.
    '''
    inputUserItemSet(INPUT_USERNAME)

def populateQueryList():
    query = ''
    itemList = []
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


def restAPI_query():
    populateQueryList()
    geo = ('40.7127', '-74.0059', '25mi')  # City of New York
    MAX_ID = None
    for idx in range(len(queryList)):
        print 'Querying twitter. Query = {}'.format(queryList[idx])
        tweets = [json.loads(str(raw_tweet)) for raw_tweet
                  in myApi.GetSearch(queryList[idx], geo, count=200, max_id=MAX_ID, result_type='mixed')]
        if tweets:
            MAX_ID = tweets[-1]['id']
            print '# of tweets from this Query: ', len(tweets)
            for tweet in tweets:
                countUser(tweet)
            storeOnFile(tweets)


def storeOnFile(tweets):        # Saves all the tweets crawled by Query
    with open("tweets_crawled_by_query.txt", 'a') as writer:
        for tweet in tweets:
            writer.write(json.dumps(tweet['text'])+'\n\n')


def countUser(tweet):
    user_name = tweet['user']['screen_name']
    if user_count.has_key(user_name):   # stores and increases count of tweets per username
        user_count[user_name] = user_count.get(user_name) + 1
    else:
        user_count[user_name] = 1


def topUsers():
    n = 20  # top 20 users
    print 'Calculating top',n,'Users!!!!'
    sorted_users = sorted(user_count.items(), key=lambda (k, v) : v, reverse=True)  #Sort based on Values
    # for i in range(n):  # prints Top n influential users
    #     print '# of tweets-per-username'
    #     print sorted_users[i][1], sorted_users[i][0]
    return [sorted_users[i][0] for i in range(n)]


def get_timeline(user_name):
    print 'Crawling timeline of',user_name
    MAX_ID = None
    with open('Users/'+user_name+'.txt', 'w') as w:
        for itr in range(2):    # 400 tweets per user
            bunch_of_statuses = myApi.GetUserTimeline(screen_name=user_name, max_id=MAX_ID, count=200)
            for userStatus in bunch_of_statuses:
                tweet = userStatus.__dict__['_text']
                MAX_ID = userStatus.__dict__['_id']
                w.write(json.dumps(tweet) + '\n')


def createItemSet(user_name):
    print 'Creating ItemSet for',user_name
    '''
    itemList = ALL the items from our Query
    words_by_user = ALL the words in the itemList that the user wrote in their tweets.
    '''
    words_by_user, itemList = [], []
    with open('Items.txt', 'r') as r:
        for items in r.readlines():
            itemList = items.split(',')
    with open('Users/'+user_name+'.txt', 'r') as r:
        for line in r.readlines():
            for word in line.strip().split():
                for i in range(len(itemList)):
                    if itemList[i] in word:
                        words_by_user.append(itemList[i])
    print 'Appending these words by user {} : {} to the itemSet'.format(user_name, words_by_user)
    item_set.append(list(set(words_by_user)))       # Removes duplicates and appends it to our itemSet.


def inputUserItemSet(user_name):
    get_timeline(user_name)                         # Will create a file Users/user_name.txt
    createItemSet(user_name)
    with open('orange/data.basket', 'w') as w:      # Writes it into data.basket
        for idx, item in enumerate(item_set):
            result = ''
            for idx, iii in enumerate(item):        # iii = items in ItemSet
                if idx < len(item)-1:
                    result += iii + ','
                else:
                    result += iii
            w.write(result + '\n' if (idx < len(item_set)-1) else result)
    print 'Dumped the itemset in to data.basket'


if __name__ == '__main__':
    main()