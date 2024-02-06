def upper_str(value):
    """Функция которая делает все буквы в слове заглавными"""
    return value.upper()


def capitalize_words(input_string):
    """Функция которая первые буквы слов делает заглавными"""
    words = input_string.split()
    capitalized_words = [word.capitalize() for word in words]
    return ' '.join(capitalized_words)
