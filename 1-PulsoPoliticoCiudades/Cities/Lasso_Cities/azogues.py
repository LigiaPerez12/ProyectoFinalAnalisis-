#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import couchdb
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import json


###API ########################
ckey = "ya1iJhS7OyQRdCHwGT5B3aoUg"
csecret = "H0pgELBgPnxFj41HSRv6nnAbc5MQRaq1u6PEuRwUChi9saxVnv"
atoken = "247529219-Xx28XuCPLa66LzUCe2JEoWz6TCDD9vdvVnoglSj4"
asecret = "cu90qqOIsYC5XvkRBliqLOIacmCuYsJeuMGoJJPuXHmRY"
#####################################

class listener(StreamListener):
    
    def on_data(self, data):
        dictTweet = json.loads(data)
        try:
            if(('Lasso' in dictTweet['text']) or ('lasso' in dictTweet['text']) or ('LASSO' in dictTweet['text']) ('CREO21' in dictTweet['text']))
                doc = db.save(dictTweet)
        except:
            print ("No Lasso Information")
            pass
        
    def on_error(self, status):
        print (status)
        
auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)
twitterStream = Stream(auth, listener())

'''========couchdb'=========='''
server = couchdb.Server('http://admin:admin8675423*@localhost:5984/')
try:
    db = server.create('lasso_azogues')
except:
    db = server['lasso_azogues']

    
'''===============LOCATIONS=============='''    
# Geolocalización de Azogues
twitterStream.filter(locations=[-78.897335,-2.80199,-78.79392,-2.659469])
