from collections import Counter
import string


punc = set(string.punctuation)


def swapchars(text):
    mcounter = Counter(text.lower()).most_common()[0][0]
    lcounter = Counter(text.lower()).most_common()[-1][0]
    swp = ""
    for word in range(len(text)):
        if text[word].islower():
            if text[word] == mcounter:
                swp += lcounter
            elif text[word] == lcounter:
                swp += mcounter
            else:
                swp += text[word]
        elif text[word].isupper():
            if text[word] == mcounter.upper():
                swp += lcounter.upper()
            elif text[word] == lcounter.upper():
                swp += mcounter.upper()
        else:
            swp += text[word]
    print swp
swapchars(raw_input())
