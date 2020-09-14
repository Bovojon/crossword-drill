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
    if request.method == 'POST':
        ans = request.POST['answer']
        clue_id = request.POST['clue_id']
        clue = get_object_or_404(Clue, id=clue_id)
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
            return render(request, 'drill.html', context)
    else:
        # clue_id = random.randint(1,57970)
        # clue = get_object_or_404(Clue, id=clue_id)
        request.session['total_clues'] += 1
        clue = Clue.objects.order_by('?')[0]
        context = {
            'clue': clue,
            'clue_id': clue.pk,
            'entry_length': len(clue.entry.entry_text)
        }
        return render(request, 'drill.html', context)

def answer(request, clue_id):
    clue = get_object_or_404(Clue, id=clue_id)
    clues = Clue.objects.filter(clue_text__exact=clue.clue_text)
    clue_entries = defaultdict(int)
    try:
        correct = request.session['correct']
        correct_answers = request.session['correct_answers']
        total_clues = request.session['total_clues']
    except:
        correct = False
        correct_answers = 0
        total_clues = 0
    if len(clues) > 1:
        multiple = True
        for c in clues:
            clue_entries[c.entry] += 1
    else:
        multiple = False
    clue_entries_dict = {}
    for k, v in clue_entries.items():
        clue_entries_dict[str(k)] = str(v)
    context = {
        'clue': clue,
        'clue_entries': clue_entries_dict,
        'multiple': multiple,
        'correct': correct,
        'correct_answers': correct_answers,
        'total_clues': total_clues
    }
    return render(request, 'answer.html', context)