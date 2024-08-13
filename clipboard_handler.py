import pyperclip

def read_clipboard(max_length=500):
    content = pyperclip.paste()
    return content[:max_length] if len(content) > max_length else content

def write_clipboard(text):
    pyperclip.copy(text)
