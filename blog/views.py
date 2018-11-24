from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
import blog.models
import json

from django.views.decorators.gzip import gzip_page  
 
# Create your views here.

def index(request):
    articles=blog.models.Article.objects.all()
    return render(request,'blog/index.html',{'articles':articles})


def article_page(request,article_id):
    article = blog.models.Article.objects.get(pk=article_id)
    return render(request,'blog/article_page.html',{'article':article})

def edit_page(request,article_id):
    if str(article_id)=='0':
        return render(request,'blog/edit_page.html')
    article = blog.models.Article.objects.get(pk=article_id)
    return render(request,'blog/edit_page.html',{'article':article})

def edit_action(request,article_id,title,content):
    #title = request.POST.get('title','TITLE')
    #content = request.POST.get('content','CONTENT')
    #article_id=request.POST.get('article_id',0)
    if article_id=='0':
        blog.models.Article.objects.create(title=title,content=content)
        articles = blog.models.Article.objects.all()
        #return render(request,'blog/index.html',{'articles':articles})
        return HttpResponse(json.dumps({"status":0,"msg":"success"}))
    article=blog.models.Article.objects.get(pk=article_id)
    article.title=title
    article.content=content
    article.save()
    #return render(request,'blog/article_page.html',{'article':article})
    return HttpResponse(json.dumps({"status":0,"msg":"success"}))

def get_article(request,article_id):
    if article_id=='-1':
        articles=blog.models.Article.objects.all()
        data=[]
        for a in articles:
            article={"id":a.id,"title":a.title,"content":a.content}
            data.append(article)
        return HttpResponse(json.dumps({"code":0,"data":data}))
    article=blog.models.Article.objects.get(pk=article_id)
    data = {"code":0,"data":[{'id': article.id, 'title': article.title,'content':article.content},{'id': article.id, 'title': article.title,'content':article.content}]}
    return HttpResponse(json.dumps(data))
    #return JsonResponse({'id': article.id, 'title': article.title,'content':article.content})
   

def formattingData(code,data):
    return json.dumps(
        {
            "status": code,
            "content": data
        }
    )