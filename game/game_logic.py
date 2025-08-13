from .models import Word


def is_valid_guess(guess: str) -> bool:
    if len(guess) != 5:
        return False

    if not Word.objects.filter(text=guess).exists():
        return False

    return True


def compare_with_solution(guess: str, solution: str):
    res = [None] * 5
    is_win = True

    for i, (guess_letter, sol_letter) in enumerate(zip(guess, solution)):
        if guess_letter == sol_letter:
            res[i] = {'letter': guess_letter, 'state': 'correct', 'final_bg': '#538d4e'}
            solution = solution[:i] + '-' + solution[i + 1 :]

    for i, (guess_letter, sol_letter) in enumerate(zip(guess, solution)):
        if res[i] is not None:
            continue

        is_win = False
        if guess_letter in solution:
            res[i] = {'letter': guess_letter, 'state': 'present', 'final_bg': '#b59f3b'}
            solution = solution.replace(guess_letter, '-', 1)
        else:
            res[i] = {'letter': guess_letter, 'state': 'absent', 'final_bg': '#3a3a3a'}

    return res, is_win
