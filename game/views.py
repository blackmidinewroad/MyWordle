from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.http import require_POST

from .game_logic import compare_with_solution, is_valid_guess
from .models import Word


def board_view(request):
    if not request.session.get('active_game'):
        request.session['solution'] = Word.valid.order_by('?')[0].text
        request.session['guess'] = [''] * 5
        request.session['guess_history'] = []
        request.session['active_game'] = True
        request.session['gameboard'] = [[{'letter': '', 'state': 'empty'} for _ in range(5)] for _ in range(6)]
        request.session['cur_row'] = 0
        request.session['cur_col'] = 0
        request.session['keys_state'] = {}

    context = {
        'gameboard': request.session['gameboard'],
        'cur_row': request.session['cur_row'],
        'cur_col': request.session['cur_col'],
        'keys_state': request.session.get('keys_state', {}),
    }

    return render(request, 'game/index.html', context)


@require_POST
def key_press(request):
    letter = request.POST.get('key').lower()
    row = int(request.POST.get('row'))
    col = int(request.POST.get('col'))

    temp_guess = request.session['guess']

    if col > 0 and not temp_guess[col - 1]:
        return HttpResponse(status=409)

    temp_guess[col] = letter
    request.session['guess'] = temp_guess

    context = {
        'letter': letter,
        'state': 'tbd',
        'row': row,
        'col': col,
        'new_col': col + 1,
    }

    return render(request, 'game/tile.html', context)


@require_POST
def backspace(request):
    row = int(request.POST.get('row'))
    col = int(request.POST.get('col'))

    temp_guess = request.session['guess']

    if col < 5 and temp_guess[col]:
        return HttpResponse(status=409)

    temp_guess[col - 1] = ''
    request.session['guess'] = temp_guess

    context = {
        'letter': '',
        'state': 'empty',
        'row': row,
        'col': col - 1,
        'new_col': col - 1,
    }

    return render(request, 'game/tile.html', context)


@require_POST
def submit(request):
    row = int(request.POST.get('row'))
    col = int(request.POST.get('col'))

    guess = ''.join(request.session['guess'])
    solution = request.session['solution']

    if not is_valid_guess(guess) or guess in request.session['guess_history']:
        return render(request, 'game/invalid_word.html', {'guess': request.session['guess'], 'row': row, 'col': col})

    result, is_win = compare_with_solution(guess, solution)
    game_over = is_win or row == 5

    context = {
        'result': result,
        'row': row,
        'new_row': row + 1,
        'new_col': 0,
        'is_win': is_win,
        'game_over': game_over,
    }

    if game_over:
        request.session['active_game'] = False

    temp_gameboard = request.session['gameboard']
    temp_gameboard[row] = result
    request.session['gameboard'] = temp_gameboard

    for res in result:
        letter = res['letter'].upper()
        if request.session['keys_state'].get(letter) != 'correct':
            request.session['keys_state'].update({letter: res['state']})

    request.session['cur_row'] = row + 1
    request.session['cur_col'] = 0

    request.session['guess_history'].append(guess)

    request.session['guess'] = [''] * 5

    print(f'guess: {guess}\nsolution: {solution}')

    return render(request, 'game/submit.html', context)
