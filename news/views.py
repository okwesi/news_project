from django.core.paginator import Paginator
from django.db import models
from django.http.response import HttpResponse
from django.views import generic
from django.shortcuts import redirect, render
from .models import News
import requests

count = News.objects.count()


class HomeNews(generic.ListView):
    template_name = "home.html"
    context_object_name = 'news'
    paginate_by = int(count/6) 
    model = News
    print(count)
    def get_queryset(self):
        return News.objects.order_by('?')

    def get_queryset(self):
        query = self.request.GET.get('search')
        if query:
            object_list = self.model.objects.filter(title__contains=query)
        else:
            object_list = self.model.objects.order_by('-datetime')
        return object_list


def save(request):
    all_news = {}
    response = requests.get(f'https://saurav.tech/NewsAPI/top-headlines/category/technology/in.json')
    newsdata = response.json()
    news = newsdata['articles']

    for i in news:
        news_data = News(
            source=i['source'],
            author=i['author'],
            title=i['title'],
            description=i['description'],
            url=i['url'],
            image=i['urlToImage'],
            datetime=i['publishedAt'],
            content=i['content'],
            category= 'technology'
        )
        news_data.save()
        all_news = News.objects.all().order_by('?')

    url = "https://free-news.p.rapidapi.com/v1/search"
    querystring = {"q":"hacking","lang":"en"}
    headers = {
        'x-rapidapi-host': "free-news.p.rapidapi.com",
        'x-rapidapi-key': "11bed60f33msh9bc53743f06ae92p11fd8ajsn8349ac59142e"
        }
    response = requests.request("GET", url, headers=headers, params=querystring)
    hackingdata = response.json()
    hackingnews = hackingdata['articles']

    for i in hackingnews:
        news_data = News(            
            author=i['author'],
            title=i['title'],
            description=i['summary'],
            image=i['media'],
            datetime=i['published_date'],
            category= 'hacking'
        )
        news_data.save()
        all_news = News.objects.all().order_by('?')




    url = "https://news-search4.p.rapidapi.com/news"
    payload = "find=programming%20language&sortby=match"
    headers = {
        'content-type': "application/x-www-form-urlencoded",
        'x-rapidapi-host': "news-search4.p.rapidapi.com",
        'x-rapidapi-key': "11bed60f33msh9bc53743f06ae92p11fd8ajsn8349ac59142e"
        }
    response = requests.request("POST", url, data=payload, headers=headers)
    programmingdata = response.json()
    programmingnews = programmingdata['response']

    for i in programmingnews:
        news_data = News(            
            author=i['author'],
            title=i['title'],
            description=i['description'],
            image=i['image'],
            datetime=i['publishedAt'],
            category= 'programming'
        )
        news_data.save()
        all_news = News.objects.all().order_by('?')


    return  redirect('home')



def hacking(request):
    url = "https://free-news.p.rapidapi.com/v1/search"
    querystring = {"q":"hacking","lang":"en"}
    headers = {
        'x-rapidapi-host': "free-news.p.rapidapi.com",
        'x-rapidapi-key': "11bed60f33msh9bc53743f06ae92p11fd8ajsn8349ac59142e"
        }
    response = requests.request("GET", url, headers=headers, params=querystring)
    data = response.json()
    hackingnews = data['articles']
    all = {
        'hacking': hackingnews
        }
    return render(request, 'hacking.html', all)



def tech(request):
    url = "https://free-news.p.rapidapi.com/v1/search"
    querystring = {"q":"technology","lang":"en"}
    headers = {
        'x-rapidapi-host': "free-news.p.rapidapi.com",
        'x-rapidapi-key': "11bed60f33msh9bc53743f06ae92p11fd8ajsn8349ac59142e"
        }
    response = requests.request("GET", url, headers=headers, params=querystring)
    data = response.json()
    technews = data['articles']
    all = {
        'tech': technews
        }
    return render(request, 'tech.html', all)



class Programming(generic.ListView):
    template_name = "programming.html"
    context_object_name = 'programming'
    paginate_by = int(count/12)
    
    def get_queryset(self):
        return News.objects.filter(category__contains='programming')


# url = "https://saurav.tech/NewsAPI/top-headlines/category/health/in.json"

# payload={}
# headers = {}

# response = requests.request("GET", url, headers=headers, data=payload)

# print(response.text)