import pytest
from chapter_002.e05_pig_latin import pig_latin
from chapter_002.e05_pig_latin_fstring import pig_latin_fstring
from chapter_002.e05_pig_latin_punctuation import pig_latin_punctuation
from chapter_002.e05_pig_latin_alternative import pig_latin_alternative
from chapter_002.e06_pig_latin_sentence import pig_latin_sentence


def test_pig_latin_01():
    assert pig_latin("easy") == "easyway"


def test_pig_latin_02():
    assert pig_latin("many") == "anymay"


def test_pig_latin_03():
    assert pig_latin_fstring("easy") == "easyway"


def test_pig_latin_04():
    assert pig_latin_fstring("many") == "anymay"


def test_pig_latin_05():
    assert pig_latin_punctuation("Easy!") == "Easyway!"


def test_pig_latin_06():
    assert pig_latin_punctuation("many%") == "anymay%"


def test_pig_latin_07():
    assert pig_latin_alternative("wine") == "wineway"


def test_pig_latin_08():
    assert pig_latin_alternative("wind") == "indway"


def test_pig_latin_sentence():
    assert pig_latin_sentence("this is a test translation") == "histay isway away esttay ranslationtay"
