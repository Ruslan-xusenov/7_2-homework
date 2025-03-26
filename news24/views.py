import datetime
from django.contrib import messages
from django.shortcuts import render, redirect
from .models import Category, News, Sponsor
from .forms import ContactForm

def get_date():
    return datetime.datetime.today()

def get_category():
    return Category.objects.all()

def index(request):
    news = News.objects.all().order_by('-date')
    news_lasts = News.objects.all().order_by('-date')
    news_uzb = News.objects.filter(category__name="O'zbekiston").order_by('-date')
    news_jah = News.objects.filter(category__name="Jahon").order_by('-date')
    news_sport = News.objects.filter(category__name="Sport").order_by('-date')
    news_fan = News.objects.filter(category__name="Fan-texnika").order_by('-date')
    sponsor = Sponsor.objects.all()
    popular_news = News.objects.all().order_by('-views')
    context = {
        'ctg': get_category(),
        'news': news,
        'news_lasts': news_lasts[:5],
        'news_uzb': news_uzb,
        'news_jah': news_jah,
        'news_sport': news_sport,
        'news_fan': news_fan,
        'sponsor': sponsor,
        'date': get_date(),
        'popular_news': popular_news[:4],
    }
    return render(request, 'index.html', context)

def about(request):
    news = News.objects.all().order_by('-date')
    news_lasts = News.objects.all().order_by('-date')
    context = {
        'ctg': get_category(),
        'news': news,
        'news_lasts': news_lasts[:5],
        'date': get_date(),
    }
    return render(request, '404.html', context)

def detail(request, pk):
    new = News.objects.get(pk=pk)
    news = News.objects.filter(category__name=new.category).order_by('-date')
    popular_news = News.objects.filter(category__name=new.category).order_by('-views')
    sponsor = Sponsor.objects.all()
    new.views += 1
    new.save()
    context = {
        'ctg': get_category(),
        'new': new,
        'news': news,
        'popular_news': popular_news[:4],
        'date': get_date(),
        'sponsor': sponsor,
    }
    return render(request, 'single_page.html', context)

def contact(request):
    news = News.objects.all().order_by('-date')
    popular_news = News.objects.all().order_by('-views')
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Xabaringiz muvaffaqiyatli yuborildi!")
            return redirect('contact')

    else:
        form = ContactForm()
    context = {
        'ctg': get_category(),
        'news': news,
        'popular_news': popular_news[:4],
        'date': get_date(),
        'form': form,
    }
    return render(request, 'contact.html', context)


def category_detail(request, pk):
    ctg = Category.objects.get(id=pk)
    active_ctg = Category.objects.get(id=pk)
    news = News.objects.filter(category__name=ctg.name ).order_by('-date')
    context = {
        'ctg': get_category(),
        'news': news,
        'date': get_date(),
        'active_ctg': active_ctg,
    }
    return render(request, 'category.html', context)