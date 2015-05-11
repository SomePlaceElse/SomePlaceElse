import twitter, json, Orange


class Project:
    user_count = {}  # A dictionary of {"username" : # of tweets by that username}
    '''
        item_set = Keeps record of the itemSet generated so far, in the end, dumps it into data.bucket
        queryList = List of all the Queries disjoint by 550-some characters.
    '''
    item_set, append_item_set, queryList, restaurantList, input_user_item = [], [], [], [], []
    INPUT_USERNAME = ''
    topK, SUPPORT = 0, 0.0
    ranked_recommendations, ranked_restaurants = {}, {}
    geo = ('40.7127', '-74.0059', '25mi')  # City of New York

    myApi=twitter.Api(consumer_key='y4kyDOkiaOEF0VRBhBo2O4E2j',
                  consumer_secret='SxuOj26fmlq3Buh7UuGGs9TDEc1JlVVA0S63gaKl4AM4uvzSAd',
                  access_token_key='54665279-J9uu0N20FXEInUokgTrTCeyzXDJ1bghd0lgL8zwgE',
                  access_token_secret='pQwwdcgUvLe6n2jguoU9mwNKCs9use6IXOoQ2YNVxHxuM')

    def __init__(self, user_name, topK=20, SUPPORT=0.3):
        self.INPUT_USERNAME = user_name
        self.topK = topK
        self.SUPPORT = SUPPORT


    def shoot_eager(self):
        self.restAPI_query()
        users = self.topUsers()  #top 20 users.
        for user in users:
            self.get_timeline(user)
            self.createItemSet(user)
        self.inputUserItemSet(self.INPUT_USERNAME)
        self.getRecommendation()
        self.getRestaurants()
        for k in self.ranked_restaurants.keys():
            print k


    def shoot_lazy(self):
        self.get_timeline(self.INPUT_USERNAME)              # Will create a file Users/user_name.txt
        user_name = self.INPUT_USERNAME
        print 'Creating ItemSet for', user_name
        '''
        itemList = ALL the items from our Query
        words_by_user = ALL the words in the itemList that the user wrote in their tweets.
        '''
        words_by_user, itemList = [], []
        with open('Files/Items.txt', 'r') as r:
            for items in r.readlines():
                itemList = items.split(',')
        with open('Users/'+user_name+'.txt', 'r') as r:
            for line in r.readlines():
                for word in line.strip().split():
                    for i in range(len(itemList)):
                        if itemList[i] in word:
                            words_by_user.append(itemList[i])
        # print 'Appending these words by user {} : {} to the itemSet'.format(user_name, words_by_user)
        self.append_item_set.append(list(set(words_by_user)))
        self.dumpToBasket('lazy')
        self.getRecommendation()
        self.getRestaurants()


    def populateQueryList(self):
        query1 = 'meat OR chicken OR beef OR pork OR ham OR burger OR hamburger OR pizza OR egg OR omelet OR turkey OR ' \
                 'shrimp OR lobster OR crabs OR oyster OR sausage OR salami OR "turkey sausage" OR pancake OR "apple pie" ' \
                 'OR kebab OR kabab OR bacon OR sandwich OR steak OR dumplings OR "fish n chips" OR "hot dog" OR pasta ' \
                 'OR salad OR rice OR pudding'
        query2 = 'cake OR corn OR cookie OR flatbread OR doughnut OR stew OR noodles OR "smoked fish" OR wrap OR ' \
                 'roll OR "buffalo wings" OR "roasted salmon" OR baklava OR schezwan OR "pepperoni sausage" OR "pepperoni ' \
                 'pizza" OR "chicken biryani" OR "crumb pie" OR cheesecake OR "dim sum" OR barbecue OR pita OR "mashed potato"' \
                 ' OR cheeseburger'
        query3 = '"chicken wings" OR nachos OR curry OR tandoori OR sizzler OR lasagna OR tofu OR spaghetti OR ravioli OR ' \
                 'burrito OR tacos OR "black beans" OR sushi OR quesadilla OR falafel OR shawarma OR tortillas OR meatball OR' \
                 ' poutine OR "BBQ chicken" OR "BBQ lamb" OR "chicken teriyaki" OR "chicken nuggets" OR cannelloni OR "fried rice" ' \
                 'OR biryani'
        query4 = '"schezwan fried rice" OR "schezwan rice" OR "shrimp rice" OR "lemon rice" OR "fish curry" OR "shrimp curry" ' \
                 'OR "roasted lamb" OR "lamb biryani" OR "shrimp biryani" OR "indian bread" OR "garlic naan" OR "chicken curry" ' \
                 'OR "lamb curry" OR "curry rice" OR "hot pot" OR "caesar salad" OR "stir fried" OR brigadeiro OR bossam OR "rice casserole"'
        self.queryList.append(query1)
        self.queryList.append(query2)
        self.queryList.append(query3)
        self.queryList.append(query4)


    def restAPI_query(self):
        self.populateQueryList()
        MAX_ID = None
        for idx in range(len(self.queryList)):
            print 'Query = {}'.format(self.queryList[idx])
            tweets = [json.loads(str(raw_tweet)) for raw_tweet
                      in self.myApi.GetSearch(self.queryList[idx], self.geo, count=200, max_id=MAX_ID, result_type='mixed')]
            if tweets:
                MAX_ID = tweets[-1]['id']
                print '# of tweets from this Query: ', len(tweets)
                for tweet in tweets:
                    self.countUser(tweet)


    def storeOnFile(self, tweets):
        with open("Files/tweets_crawled_by_query.txt", 'a') as writer:
            for tweet in tweets:
                writer.write(json.dumps(tweet['text'])+'\n')


    def countUser(self, tweet):
        user_name = tweet['user']['screen_name']
        # stores and increases count of tweets per username
        self.user_count[user_name] = self.user_count[user_name] + 1 if self.user_count.has_key(user_name) else 1


    def topUsers(self):
        print 'Calculating top',self.topK,'Users!!!!'
        sorted_users = sorted(self.user_count.items(), key=lambda (k, v) : v, reverse=True)  #Sort based on Values
        return [sorted_users[i][0] for i in range(self.topK)]


    def get_timeline(self, user_name):
        print 'Crawling timeline of', user_name
        MAX_ID = None
        with open('Users/'+user_name+'.txt', 'w') as w:
            for itr in range(2):                        # 400 tweets per user
                bunch_of_statuses = self.myApi.GetUserTimeline(screen_name=user_name, max_id=MAX_ID, count=200)
                for userStatus in bunch_of_statuses:
                    tweet = userStatus.__dict__['_text']
                    MAX_ID = userStatus.__dict__['_id']
                    w.write(json.dumps(tweet) + '\n')


    def createItemSet(self, user_name):
        print 'Creating ItemSet for', user_name
        '''
        itemList = ALL the items from our Query
        words_by_user = ALL the words in the itemList that the user wrote in their tweets.
        '''
        words_by_user, itemList = [], []
        with open('Files/Items.txt', 'r') as r:
            for items in r.readlines():
                itemList = items.split(',')
        with open('Users/'+user_name+'.txt', 'r') as r:
            for line in r.readlines():
                for word in line.strip().split():
                    for i in range(len(itemList)):
                        if itemList[i] in word:
                            words_by_user.append(itemList[i])
        # print 'Appending these words by user {} : {} to the itemSet'.format(user_name, words_by_user)
        self.item_set.append(list(set(words_by_user)))       # Removes duplicates and appends it to our itemSet.


    def inputUserItemSet(self, user_name):
        self.get_timeline(user_name)                         # Will create a file Users/user_name.txt
        self.createItemSet(user_name)
        self.dumpToBasket('eager')


    def dumpToBasket(self, type):
        if type == 'eager':
            with open('Basket/data.basket', 'w') as w:      # Writes it into data.basket
                for idx, item in enumerate(self.item_set):
                    result = ''
                    for idx, iii in enumerate(item):        # iii = items in ItemSet
                        result += (iii + ',') if (idx < len(item)-1) else iii
                    w.write(result + '\n')
            print 'Dumped the itemset in to data.basket'

        else:     #   Lazy
            with open('Basket/data.basket', 'a') as a:      # Appends it into data.basket
                for idx, item in enumerate(self.append_item_set):
                    result = ''
                    for idx, iii in enumerate(item):        # iii = items in ItemSet
                        result += (iii + ',') if (idx < len(item)-1) else iii
                    a.write(result + '\n')
            print 'Appended the itemset to data.basket'


    def getRecommendation(self):
        data = Orange.data.Table("Basket/data.basket")     #  Load data from the text file: data.basket
        data_instance = data[len(data)-1]   # The last item in the bucket is the one of userinput!
        rules = Orange.associate.AssociationRulesSparseInducer(data, support=self.SUPPORT)
        with open('Files/number_of_rules.txt', 'a') as a:
            a.write(json.dumps((self.SUPPORT, len(rules))) + ',')       # Records the support and number of rules created
        print 'Finding recommendations for', self.INPUT_USERNAME,'...'
        print 'User data',data_instance
        for rule in rules:
            if rule.applies_left(data_instance) and not rule.applies_right(data_instance):
                rec_list = rule.right.get_metas(str).keys()
                for item in rec_list:
                    if self.ranked_recommendations.has_key(item):
                        self.ranked_recommendations[item] += 1
                    else:
                        self.ranked_recommendations[item] = 1


    def getRestaurants(self):
        queryItemList = []
        for k in self.ranked_recommendations.keys():
            queryItemList.append(k)
        query = ' OR '.join(queryItemList)      # concoct a query magically
        print 'Query =', query
        MAX_ID = None
        for idx in range(3):        # Get about 600 tweets using that query
            tweets = [json.loads(str(raw_tweet)) for raw_tweet
                      in self.myApi.GetSearch(query, self.geo, count=200, max_id=MAX_ID, result_type='mixed')]
            if tweets:
                MAX_ID = tweets[-1]['id']
                print '# of tweets from this Query: ', len(tweets)
                for tweet in tweets:
                    self.countUser(tweet)
                self.storeOnFile(tweets)
        self.populateRestaurantList()
        self.rankRestaurants()


    def rankRestaurants(self):
        with open('Files/tweets_crawled_by_query.txt', 'r') as r:
            for line in r.readlines():                          # Go through every tweet
                for idx in range(len(self.restaurantList)):
                    restaurant_name = self.restaurantList[idx]
                    if restaurant_name in line:                 # If it is present in the line
                        print restaurant_name
                        if self.ranked_restaurants.has_key(restaurant_name):
                            self.ranked_restaurants[restaurant_name] += 1
                        else:
                            self.ranked_restaurants[restaurant_name] = 1


    def populateRestaurantList(self):
        with open('Files/restaurants_list.txt', 'r') as r:
            for line in r.readlines():
                self.restaurantList = json.loads(line)
                print 'Res list = ',self.restaurantList