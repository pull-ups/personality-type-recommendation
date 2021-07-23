from django.shortcuts import render, get_object_or_404, redirect
from .models import Question
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
def main(request):

    return render(request, 'question/main.html')

def question(request):

    return render(request, 'question/question.html')

def result(request):
    q1=request.POST['q1']
    q2=request.POST['q2']
    q3=request.POST['q3']
    q4=request.POST['q4']
    q5=request.POST['q5']
    q6=request.POST['q6']
    q7=request.POST['q7']
    q8=request.POST['q8']

    inputvector=[q1,q2,q3,q4,q5,q6,q7,q8]
    return render(request, 'question/result.html', {'inputvector':inputvector})