from io import StringIO
import random
import pytest
from e01_guessing_game import guessing_game


def test_correct(monkeypatch, capsys):
    random.seed(0)              # first randint will be 100
    monkeypatch.setattr('sys.stdin', StringIO('49\n'))
    guessing_game()
    captured_out, captured_err = capsys.readouterr()

    assert captured_out.endswith('Just right! I had the number 49 in mind.')
