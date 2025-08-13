import os

from django.core.management.base import BaseCommand
from game.models import Word


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('file_path', type=str)
        parser.add_argument('--answer-words', action='store_true')

    def handle(self, *args, **kwargs):
        file_path = kwargs['file_path']
        is_answer = kwargs['answer_words']

        if not os.path.exists(file_path):
            self.stderr.write(self.style.ERROR(f'File not found: {file_path}'))
            return

        with open(file_path, encoding='utf-8') as file:
            words = [Word(text=line.strip(), answer=is_answer) for line in file]
            Word.objects.bulk_create(words, ignore_conflicts=True)
            self.stdout.write(self.style.SUCCESS(f'Successfully loaded {len(words)} words'))
