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
import shutil
def result(request):
    q8=request.POST['q8']
    inputvector[7]=int(q8)

    movie_result=Recommendation().movie_recommendation(inputvector, 4)
    movie_id_arr=movie_result['movie_id'].tolist()
    title_arr=movie_result['title'].tolist()
    rating_arr=movie_result['user_rating'].tolist()
    summary_arr=movie_result['summary'].tolist()
    octagon=radar_chart(inputvector)
    octagon_html=codecs.open("render.html", 'r').read()
    filename = 'render.html' 
    src = '' 
    dir = 'static/html/' 
    shutil.move(src + filename, dir + filename)

    octagon_scripttag=octagon_html.split("</title>")[1].split("</head>")[0]
    octagon_content=octagon_html.split("<body>")[1].split("</body>")[0]

    music_result=Recommendation().music_recommendation(inputvector, 4)
    music_id_arr=music_result['id'].tolist()
    music_title_arr=music_result['Title'].tolist()
    music_artist_arr=music_result['Artist'].tolist()
    music_album_arr=music_result['Album'].tolist()
    music_lyric_arr=music_result['Lyric'].tolist()

    return render(request, 'question/result.html', {'movie_id_arr':movie_id_arr, 'title_arr':title_arr, 'rating_arr':rating_arr, 'summary_arr':summary_arr, 
                                                    'music_id_arr':music_id_arr, 'music_title_arr':music_title_arr, 'music_artist_arr':music_artist_arr, 'music_album_arr':music_album_arr, 'music_lyric_arr':music_lyric_arr,
                                                    "oct_script":octagon_scripttag, "oct_content":octagon_content})