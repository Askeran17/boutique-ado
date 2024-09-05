from django.shortcuts import render

# Create your views here.

def index(request):
    """ A view to return the index page """

    return render(request, 'home/index.html')

def quiz(request):
    return render(request, 'home/quiz.html')
