from django.shortcuts import render
from .models import Question

def main(request):

    return render(request, 'question/main.html')

def question(request):

    return render(request, 'question/question.html')

def result(request):

    return render(request, 'question/result.html')