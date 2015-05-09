# -*- coding: utf-8 -*-
"""
Name:     Gaurav Ghosh
AlbanyID: 001220806
Course:   CSI531 Data Mining
"""

from os import stat
import twitter, sys, json
reload(sys)
sys.setdefaultencoding("utf-8")

def main():
    write(fetch("MidtownLunch"))
    #write(get_user_tweets("huylerje"))
    #write(get_user_tweets("Octavius_13"))
    #write(get_user_tweets("Nilsaaa_"))
    #write(get_user_tweets("NewYorkCP"))


def fetch(user):

    myApi=twitter.Api(consumer_key='XFHeXPpxisqXKQtMz1X4Zzc9Y', \
                  consumer_secret='KCV9nW01jiwRPybbhLRLkRUG5BatetveZvGSRdexd8RcsQl861', \
                  access_token_key='1145941135-HmPlhgRPYEY4O0DBdiWGtsHggs5U5VYZhW8jPFw', \
                  access_token_secret='N85VZiA27ZDObXtIxVi4s0nPIoaRXDeJnTSzhghhZ9Nu0')
    data = {}

    api = twitter.Api()
    max_id = None
    total = 0
    while True:
        statuses = myApi.GetUserTimeline(user, count=200, max_id=max_id)
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


def write(statuses):
    with open("influential.txt", 'a+') as f:
        for tweet in statuses:
            f.write(json.dumps(tweet.text)+'\n')
        f.write('\n')
    pass

if __name__ == '__main__':
    main()
