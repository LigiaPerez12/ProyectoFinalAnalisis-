#!/usr/bin/env python
# coding: utf-8

# ### Delete null user location

# In[ ]:


import couchdb

'''========couchdb'=========='''
server = couchdb.Server('http://admin:admin8675423*@localhost:5984/')
db = server['lasso_words']


for docid in db.view('_all_docs'):
    doc = db.get(docid['id'])
    if(doc['user']['location'] is None):
        db.delete(doc)


# ### Organice the location info

# In[2]:


import couchdb

'''========couchdb'=========='''
server = couchdb.Server('http://admin:admin8675423*@localhost:5984/')
db = server['lasso_words']


for docid in db.view('_all_docs'):
    doc = db.get(docid['id'])
    if(('Quito' in doc['user']['location']) or ('Quito - Ecuador' in doc['user']['location']) or ('Pichincha, Ecuador' in doc['user']['location']) or ('Quito Ecuador' in doc['user']['location']) or ('Quito-Ecuador' in doc['user']['location']) or ('UIO' in doc['user']['location'])):
        doc['user']['location'] = 'Quito, Ecuador'
    elif(('Guayaquil' in doc['user']['location']) or ('Guayaquil-Ecuador' in doc['user']['location']) or ('Guayaquil - Ecuador' in doc['user']['location']) or ('GYE' in doc['user']['location']) or ('guayaquil' in doc['user']['location']) or ('Chile (Guayaquileño)' in doc['user']['location'])):
         doc['user']['location'] = 'Guayaquil, Ecuador'
    elif(('Loja' in doc['user']['location']) or ('loja' in doc['user']['location'])):
        doc['user']['location'] = 'Loja, Ecuador'
    elif(('Cuenca' in doc['user']['location']) or ('Cuenca-Ecuador' in doc['user']['location']) or ('Sigsig, Ecuador' in doc['user']['location'])):
        doc['user']['location'] = 'Cuenca, Ecuador'
    elif(('Quevedo' in doc['user']['location'])):
        doc['user']['location'] = 'Quevedo, Ecuador'
        
    save1 = db.save(doc)


# ### Delete other location data

# In[3]:


import couchdb

'''========couchdb'=========='''
server = couchdb.Server('http://admin:admin8675423*@localhost:5984/')
db = server['lasso_words']

for docid in db.view('_all_docs'):
    doc = db.get(docid['id'])
    if('Ecuador' not in doc['user']['location']):
        db.delete(doc)

