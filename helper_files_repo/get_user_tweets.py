# -*- coding: utf-8 -*-
"""
Name:     Gaurav Ghosh
AlbanyID: 001220806
Course:   CSI531 Data Mining
"""

from os import stat
import twitter, sys, json
reload(sys)

myApi=twitter.Api(consumer_key='XFHeXPpxisqXKQtMz1X4Zzc9Y', \
                  consumer_secret='KCV9nW01jiwRPybbhLRLkRUG5BatetveZvGSRdexd8RcsQl861', \
                  access_token_key='1145941135-HmPlhgRPYEY4O0DBdiWGtsHggs5U5VYZhW8jPFw', \
                  access_token_secret='N85VZiA27ZDObXtIxVi4s0nPIoaRXDeJnTSzhghhZ9Nu0')

sys.setdefaultencoding("utf-8")

def main():

    write(get_timeline("MelissaClark"))
    write(get_timeline("EaterNY"))
    write(get_timeline("grubstreet"))
    write(get_timeline("ruthreichl"))
    write(get_timeline("SplendidTable"))
    write(get_timeline("TheCooksCook"))
    write(get_timeline("infatuation"))
    write(get_timeline("thefeednyc"))
    write(get_timeline("TestingTableNYC"))



def fetch(user):

    data = {}

    api = twitter.Api()
    max_id = None
    total = 0
    while True:
        statuses = myApi.GetUserTimeline(screenname=user, count=200, max_id=max_id)
        newCount = ignCount = 0
        for s in statuses:
            if s.id in data:
                ignCount += 1
            else:
                data[s.id] = s
                newCount += 1
        total += newCount
        print >>sys.stderr, "Fetched %d/%d/%d new/old/total." % (
            newCount, ignCount, total)
        if newCount == 0:
            break
        max_id = min([s.id for s in statuses]) 
    return data.values()

def get_timeline(user_name):
    MAX_ID = None
    tweets = []
    for it in range(5):
        bunch_of_statuses = myApi.GetUserTimeline(screen_name=user_name, max_id=MAX_ID, count=200)
        for status in bunch_of_statuses:
            dick_status = status.__dict__
            tweets.append(dick_status)
            print dick_status['_text']
            MAX_ID = dick_status['_id']

    return tweets

def write(statuses):
    with open("influential.txt", 'a+') as f:
        for tweet in statuses:
            f.write(json.dumps(tweet['_text']+'\n'))
        f.write('\n')
    pass

if __name__ == '__main__':
    main()
