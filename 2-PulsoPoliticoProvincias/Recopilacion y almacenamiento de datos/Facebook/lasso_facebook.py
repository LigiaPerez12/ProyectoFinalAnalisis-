#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import couchdb
from facebook_scraper import get_posts

''' REACCIONES EN 600 PUBLICACIONES '''
''' LASSO GUILLERMO FACEBOOK'''

'''========couchdb'=========='''
server = couchdb.Server('http://admin:admin8675423*@localhost:5984/')

try:
    db = server.create('lasso_facebook')
except:
    db = server['lasso_facebook']

reaction = {}
post1 = {}

suma = 0
cont = 0

for post in get_posts("LassoGuillermo", pages = 100, extra_info = True):
    try:
        reaction = post['reactions']
        for clave in reaction:
            suma += reaction[clave]
        
        post1['likes'] = suma
        post1['commnets'] = post['comments']
        post1['shares'] = post['shares']
            
    except KeyError:
        suma += post['likes']
        post1['likes'] = suma
        post1['commnents'] = post['comments']
        post1['shares'] = post['shares']
    
    cont = cont + 1
    doc = db.save(post1)
    post1 = {}
    
    if cont == 600:
        break


# In[ ]:




