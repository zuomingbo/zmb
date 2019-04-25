from django.shortcuts import render
from creep import models
from django.shortcuts import render

def movie(request):
    movie_list = models.Movie.objects.all()
    return render(request,'creep/movie.html',{'movie_list':movie_list})

def weather(request):
    weather_list = models.Weather.objects.all()
    return render(request,'creep/weather.html',{'weather_list':weather_list})

def jdphone(request):
    jdphone_list = models.JDphone.objects.all()
    return render(request,'creep/jdphone.html',{'jdphone_list':jdphone_list})

def mainPage(request):
    return render(request,'creep/mainPage.html')