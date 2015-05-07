irregulars = {
    "ox": "oxen",
    "goose": "geese",
    "gas": "gasses"
}

collectives = ["moose", "deer"]

es_suffixes = ["sh", "ch", "s", "x", "z"]


def is_es_word(word):
    for suffix in es_suffixes:
        if word.endswith(suffix):
            return True
    return False


def pluralize(word):
    if word in collectives:
        return word

    elif word in irregulars:
        return irregulars[word]

    elif is_es_word(word):
        return word + "es"

    else:
        return word + "s"
