def count_words(s):
    return(len(s.split()))

def count_chars(s):
    s=s.lower()
    d={}
    for c in s:
        if c.isalpha():
            d[c]=d.get(c,0)+1
    return(d)

def transform_dict(id):
    return [{"char": key, "num": value} for key,value in id.items()]