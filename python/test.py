import requests
import pymysql,json

def getWitticism():
    response = requests.get('http://api.tianapi.com/txapi/sentence/index?key=75f59f3f6f98a4a4e3c0c869cb303614').json()
    #print(response)
    if(response['code'] == 200):
        #print(response['newslist'][0]['content'])
        content = response['newslist'][0]['content']
        return content