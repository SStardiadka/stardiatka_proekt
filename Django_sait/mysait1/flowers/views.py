from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, Http404
from .models import*

menu = [{'title':'О сайте', 'url_name':'novosti'},
         {'title':'Добавить статью', 'url_name':'add_page'},
         {'title': "Обратная связь", 'url_name': 'contact'},
        {'title': "Войти", 'url_name': 'login'}
        ]


def index(request):
    post = News.objects.all()
    return render(request, 'flowers/index.html', {'post': post,'menu': menu, 'title': 'Главная страница'})

def novosti(request):
    return render(request, 'flowers/novosti.html', {'menu': menu,'title': 'Новости'})
    
    
def index(request):
    posts = News.objects.all()
    cats = Category.objects.all()

    context = {
        'posts': posts,
        'cats': cats,
        'menu': menu,
        'title': 'Главная страница',
        'cat_selected': 0,
    }

    return render(request, 'flowers/index.html', context=context)

def novosti(request):
    return render(request, 'flowers/novosti.html', {'menu': menu, 'title': 'О сайте'})


def addpage(request):
    return HttpResponse("Добавление статьи")

def contact(request):
    return HttpResponse("Обратная связь")

def login(request):
    return HttpResponse("Авторизация")


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')

def show_post(request, post_id):
    return HttpResponse(f"Отображение статьи с id = {post_id}")

def show_category(request, cat_id):
    posts = News.objects.filter(cat_id=cat_id)
    cats = Category.objects.all()

    if len(posts) == 0:
        raise Http404()

    context = {
        'posts': posts,
        'cats': cats,
        'menu': menu,
        'title': 'Отображение по рубрикам',
        'cat_selected': cat_id,
    }

    return render(request, 'women/index.html', context=context)

