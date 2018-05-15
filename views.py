from django.shortcuts import render, redirect, HttpResponse
from django.utils.crypto import get_random_string
word = get_random_string(length=14)
def index(request):
    if not 'attempt' in request.session:
        request.session['attempt'] = 1
    #if 'attempt' in session:
    #    session['attempt'] += 1
    return render(request,'generate_word/index.html')
def generate_a_word(request):
    if request.form == "clickbox":
        word = get_random_string(length=14)
        request.session["attempt"] += 1
        return redirect(request, '/', word = word)
