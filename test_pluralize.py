from pluralize import pluralize, is_es_word


def test_s_words():
    assert pluralize("cat") == "cats"
    assert pluralize("dog") == "dogs"


def test_es_word_pluralization():
    assert pluralize("box") == "boxes"
    assert pluralize("guess") == "guesses"


def test_words_with_double_consonants():
    assert pluralize("gas") == "gasses"


def test_irregular_words():
    assert pluralize("ox") == "oxen"
    assert pluralize("goose") == "geese"
    assert pluralize("moose") == "moose"
    assert pluralize("deer") == "deer"


def test_es_words():
    assert is_es_word("box")
    assert is_es_word("guess")
    assert not is_es_word("cat")
