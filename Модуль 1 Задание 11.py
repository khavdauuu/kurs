import string
from collections import Counter

def process_text(text):
    valid_chars = set(string.ascii_lowercase + ' ')
    text = ''.join(filter(valid_chars.__contains__, text)).lower()
    words = text.split()
    word_count = Counter(words)
    filtered_words = []
    for word, count in word_count.items():
        if len(word) >= 5 and len(set(word)) >= 4 and count > 2:
            filtered_words.append(word)

    return filtered_words
text = "Hello, world! This is a test. This test has many words, some of which are repeated more than twice! Some words have punctuation marks: !,.?;:#$%^&*(), but they should be removed."
print(process_text(text))
