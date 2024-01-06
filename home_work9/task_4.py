import re


def censor_text(input_text: str, stop_words: str):
    input_text_lower = input_text.lower()
    words = stop_words.split()
    stop_words_pattern = r'\b(?:' + '|'.join(map(re.escape, words)) + r')\b'
    censored_text = re.sub(stop_words_pattern, '****', input_text_lower)

    return censored_text


def read_censor(stop_words_path: str, censored_file_path: str, text_to_change: str):
    with open(stop_words_path, 'r') as reader:
        content = reader.read()
        censored_text = censor_text(text_to_change, content)
    with open(censored_file_path, 'w') as writer:
        writer.write(censored_text)


censored_text = '''Hello, World! Python
IS the programming language of thE future. My EMAIL is...
PYTHON as AwESOME!'''
read_censor("stop_words.txt", "censored.txt", censored_text)