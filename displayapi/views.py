from email.mime import image
from operator import le
from turtle import title
from django.shortcuts import render
import requests
# Create your views here.
def index(request):
    response=requests.get('http://api.nytimes.com/svc/mostpopular/v2/mostviewed/all-sections/7.json?api-key=rvaTKocle9T3ZiV7qfoemG0dZJfddjZZ').json()
    newsList = []
    himakom1 = 'https://http.cat/404'
    print("himakom jaya")
    for i in response['results']:
        for data1 in i['media']:
            print(data1['media-metadata'][2]['url'])
            himakom1 = data1['media-metadata'][2]['url']
            #newsList.append({"image" : data1['media-metadata'][2]['url']})
        newsList.append({
            "title":i['title'],
            "abstract" : i['abstract'],
            "updated" : i['updated'],
            "image" : himakom1 ,
            "tag" : i['des_facet']
              
        })
    print(newsList)
    return render(request,'index.html',{'response':newsList})

def detailData(request):
    template_name = "detail.html"
    