def clear_and_reverse(text):
    assert isinstance(text, str)
    assert " " in text
    text = text.replace(" ", "")[::-1]
    return text
