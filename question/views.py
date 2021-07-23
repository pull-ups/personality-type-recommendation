from django.shortcuts import render, get_object_or_404, redirect
from .models import Question
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from .Recommendation import Recommendation
from .make_octagon import radar_chart
def main(request):

    return render(request, 'question/main.html')

inputvector=[0,0,0,0,0,0,0,0]
def question1(request):

    return render(request, 'question/question1.html')
def question2(request):
    q1=request.POST['q1']
    inputvector[0]=int(q1)
    return render(request, 'question/question2.html')
def question3(request):
    q2=request.POST['q2']
    inputvector[1]=int(q2)
    return render(request, 'question/question3.html')
def question4(request):
    q3=request.POST['q3']
    inputvector[2]=int(q3)
    return render(request, 'question/question4.html')
def question5(request):
    q4=request.POST['q4']
    inputvector[3]=int(q4)
    return render(request, 'question/question5.html')
def question6(request):
    q5=request.POST['q5']
    inputvector[4]=int(q5)
    return render(request, 'question/question6.html')
def question7(request):
    q6=request.POST['q6']
    inputvector[5]=int(q6)
    return render(request, 'question/question7.html')
def question8(request):
    q7=request.POST['q7']
    inputvector[6]=int(q7)
    return render(request, 'question/question8.html')

import codecs

def result(request):
    q8=request.POST['q8']
    inputvector[7]=int(q8)

    #result=Recommendation.movie_recommendation(inputvector, 4)
    result=Recommendation().movie_recommendation(inputvector, 4)
    movie_id_arr=result['movie_id'].tolist()
    title_arr=result['title'].tolist()
    rating_arr=result['user_rating'].tolist()
    summary_arr=result['summary'].tolist()
    octagon=radar_chart(inputvector)
    octagon_html=codecs.open("render.html", 'r').read()

    octagon_scripttag=octagon_html.split("</title>")[1].split("</head>")[0]
    octagon_content=octagon_html.split("<body>")[1].split("</body>")[0]
    #return render(request, 'question/result.html', {'movie_id_arr':movie_id_arr, 'title_arr':title_arr, 'rating_arr':rating_arr, 'summary_arr':summary_arr})
    return render(request, 'question/result.html', {'movie_id_arr':movie_id_arr, 'title_arr':title_arr, 'rating_arr':rating_arr, 'summary_arr':summary_arr, "oct_script":octagon_scripttag, "oct_content":octagon_content})