from io import StringIO
import random
import pytest
import chapter_001


def test_correct(monkeypatch, capsys):
    random.seed(0)              # first randint will be 100
    monkeypatch.setattr('sys.stdin', StringIO('49\n'))
     guess_the_number()
    captured_out, captured_err = capsys.readouterr()

    assert captured_out.endswith('Just right! I had the number 49 in mind.')
