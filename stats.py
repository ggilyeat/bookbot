def count_words(text):
    return len(text.split())

def get_char_dict(text):
    retval = {}
    for ch in list(text):
        ch = ch.lower()
        if ch in retval:
            retval[ch] += 1
        else: 
            retval[ch] = 1
    return retval

def sort_on(items):
    return items["num"]

def sort_dict(d):
    retval = list()
    for k in d:
        retval.append({"char": k, "num": d[k]})
    
    retval.sort(reverse=True, key=sort_on)

    return retval
