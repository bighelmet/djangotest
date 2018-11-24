from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
import msg.models as models
import json
import time
from django.views.decorators.gzip import gzip_page  
 
# Create your views here.

def edit_action(request,article_id,title,content):
    t=time.strftime('%Y-%m-%d %H:%M',time.localtime(time.time()))
    if article_id=='0':
        models.Article.objects.create(title=title,content=content,time=t)
        return HttpResponse(json.dumps({"status":0,"msg":"success"}))
    article=models.Article.objects.get(pk=article_id)
    article.title=title
    article.content=content
    article.save()
    return HttpResponse(json.dumps({"status":0,"msg":"success"}))

def get_article(request,article_id):
    if article_id=='-1':
        articles=models.Article.objects.all()
        data=[]
        for a in articles:
            article={"id":a.id,"title":a.title,"content":a.content,"time":a.time}
            data.append(article)
        return HttpResponse(json.dumps({"code":0,"data":data}))
    article=models.Article.objects.get(pk=article_id)
    data = {"code":0,"data":[{'id': article.id, 'title': article.title,'content':article.content,"time":a.time}]}
    return HttpResponse(json.dumps(data))

def delete_article(request,article_id):
    article=models.Article.objects.get(pk=article_id)
    article.delete()
    return HttpResponse(json.dumps({"status":0,"msg":"success"}))

def formattingData(code,data):
    return json.dumps(
        {
            "status": code,
            "content": data
        }
    )
