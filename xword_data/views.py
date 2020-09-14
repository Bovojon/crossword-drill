from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.http import HttpResponseRedirect
from collections import defaultdict
import random

from xword_data.models import (Entry, Puzzle, Clue)

def drill(request):
    request.session['correct'] = False
    try:
        correct_answers = request.session['correct_answers']
        total_clues = request.session['total_clues']
    except:
        request.session['total_clues'] = 0
        request.session['correct_answers'] = 0
    request.session['total_clues'] += 1
    if request.method == 'POST':
        ans = request.POST['answer']
        clue_id = request.POST['clue_id']
        clue = get_object_or_404(Clue, pk=clue_id)
        if ans.upper() == clue.entry.entry_text:
            request.session['correct_answers'] += 1
            request.session['correct'] = True
            return HttpResponseRedirect(reverse('xword-answer', args=(clue_id,)))
        else:
            context = {
                'clue': clue,
                'entry_length': len(clue.entry.entry_text),
                'error_message': "Sorry, that was not correct. Please try again."
            }
            return render(request, 'tdd_exercise/drill.html', context)
    else:
        clue_id = random.randint(1,57970)
        clue = get_object_or_404(Clue, pk=clue_id)
        context = {
            'clue': clue,
            'clue_id': clue_id,
            'entry_length': len(clue.entry.entry_text)
        }
        return render(request, 'tdd_exercise/drill.html', context)

def answer(request, clue_id):
    return render(request, 'tdd_exercise/answer.html', context)