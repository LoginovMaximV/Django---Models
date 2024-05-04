from django import template

register = template.Library()


def censor(value):
    if not isinstance(value, str):
        raise ValueError("Фильтр censor применим только к строкам.")

    censored_words = ["редиска", "плохое слово", "очень плохое слово", "пирожки"]  # Нежелательные слова для цензуры

    for word in censored_words:
        value = value.replace(word, '*' * len(word))

    return value


register.filter('censor', censor)