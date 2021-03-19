#!/usr/bin/env python
# coding: utf-8

# In[1]:


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
            if(('Arauz' in dictTweet['text']) or ('arauz' in dictTweet['text']) or ('ARAUZ' in dictTweet['text'])):
                doc = db.save(dictTweet)
        except:
            print ("No Information")
            pass
        
    def on_error(self, status):
        print (status)
        
auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)
twitterStream = Stream(auth, listener())

'''========couchdb'=========='''
server = couchdb.Server('http://admin:admin8675423*@localhost:5984/')
try:
    db = server.create('arauz_latacunga')
except:
    db = server['arauz_latacunga']

    
'''===============LOCATIONS=============='''    
# Geolocalización de Latacunga
twitterStream.filter(locations=[-78.844455,-1.143196,-78.389166,-0.72329])

