from django.shortcuts import render,redirect,get_object_or_404
from .models import Article,Category,About,Sosial
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
# Create your views here.
def index(request):
    sosial = Sosial.objects.all()
    category = Category.objects.all()
    keyword = request.GET.get("keyword")
    if keyword:
        article = Article.objects.filter(name__contains = keyword)
        return render(request,"index.html",{"articles":article,"sosials":sosial,"categories":category})
    article = Article.objects.all()[:20]
    context = {
        "sosials":sosial,
        "articles":article,
        "categories":category,
    }
    return render(request,"index.html",context)

def about(request):
    about = About.objects.all()[:1]
    sosial = Sosial.objects.all()
    categories = Category.objects.all()
    keyword = request.GET.get("keyword")
    if keyword:
        article = Article.objects.filter(name__contains = keyword)
        return render(request,"index.html",{"articles":article,"sosials":sosial,"categories":categories})
    context = {
        "about":about,
        "sosials":sosial,
        "categories":categories,
    }
    return render(request,"about.html",context)

def detail(request,id):
    categories = Category.objects.all()
    sosial = Sosial.objects.all()
    keyword = request.GET.get("keyword")
    if keyword:
        article = Article.objects.filter(name__contains = keyword)
        return render(request,"index.html",{"articles":article,"sosials":sosial,"categories":categories})
    article = get_object_or_404(Article, id = id)
    context = {
        "sosials":sosial,
        "categories":categories,
        "articles":article,
    }
    return render(request,"single.html",context)

def category(request,id):
    categories = Category.objects.all()
    sosial = Sosial.objects.all()
    keyword = request.GET.get("keyword")
    if keyword: 
        article = Article.objects.filter(name__contains = keyword )
        return render(request,"index.html",{"articles":article,"sosials":sosial,"categories":categories})
    cate = Category.objects.filter(id = id).first()
    posts_list = Article.objects.filter(category = cate)
    paginator = Paginator(posts_list,20)
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    context = {
        "sosials":sosial,
        "posts":posts,
        "categories":categories,
    }
    return render(request,"category.html",context)
