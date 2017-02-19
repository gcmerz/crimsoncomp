from collections import Counter


def swapchars(text):
    cnt = Counter()
    st = ""
    for c in range(len(text)):
        st += text[c].lower()
        if st[c].isalpha():
            cnt[st[c]] += 1
    mcounter = cnt.most_common()[0][0]
    lcounter = cnt.most_common()[-1][0]
    swp = ""
    for w in range(len(text)):
        if text[w].isalpha():
            if text[w].islower():
                if text[w] == mcounter:
                    swp += lcounter
                elif text[w] == lcounter:
                    swp += mcounter
                else: swp += text[w]
            elif text[w].isupper():
                if text[w] == mcounter.upper():
                    swp += lcounter.upper()
                elif text[w] == lcounter.upper():
                    swp += mcounter.upper()
                else: swp += text[w]
            else: swp += text[w]
        else: swp += text[w]
    print swp
swapchars(raw_input())
