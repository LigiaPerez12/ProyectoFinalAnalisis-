import requests
import pandas as pd
from bs4 import BeautifulSoup
import pymongo
import json

def find_2nd(string, substring):
    return string.find(substring, string.find(substring) + 1)
def find_1st(string, substring):
    return string.find(substring, string.find(substring))   

response = requests.get("https://www.linkedin.com/jobs")
soup = BeautifulSoup(response.content, "lxml")

company_name=[]
job=[]
place=[]

company_name=soup.find_all("a",class_="disabled ember-view job-card-container__link job-card-list__title")
job=soup.find_all("a", class_="job-card-container__link job-card-container__company-name ember-view")
place=soup.find_all("li",class_="job-card-container__metadata-item")


for element in company_name:
    element=str(element)
    limpio=str(element[find_1st(element, '>')+1:find_2nd(element, '<')])
    Tittle.append(limpio.strip())

for element in job:
    element=str(element)
    limpio=str(element[find_1st(element, '>')+1:find_2nd(element, '<')])
    Price.append(limpio.strip())

for element in place:
    element=str(element)
    limpio=str(element[find_1st(element, '>')+1:find_2nd(element, '<')])
    Description.append(limpio.strip())

dfDS=pd.DataFrame({'company_name':Company,'job':Job,'place':Place})


#=====================mongoDB=============================
myclient = pymongo.MongoClient("mongodb://localhost:27017")  
try:
    mydb=myclient['datos_empleos']
    mycol=mydb['empleo']
except:
    mydb=myclient['datos_empleos']
    mycol=mydb['empleo']

doc={}
for i in range(len(dfDS)): 
    i= i+1
    try:
        doc['_id']=i

        doc['company_name']=dfDS.iloc[i,0]
        doc['job']=dfDS.iloc[i,1]
        doc['place']=dfDS.iloc[i,2]

        mycol.insert_one(doc)
        print(doc)
        print("guardado exitosamente")

    except Exception as e:    
            print("no se pudo grabar:" + str(e))