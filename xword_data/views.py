from django.shortcuts import render

from xword_data.models import (Entry, Puzzle, Clue)

def drill(request):
    return render(request, 'tdd_exercise/drill.html')

def answer(request, clue_id):
    return render(request, 'tdd_exercise/answer.html')