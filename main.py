from stats import count_words
from stats import count_chars
from stats import transform_dict
import sys

if len(sys.argv) !=2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

def get_book_text(f):
    with open(f,'r') as c:
        return c.read()

def sort_on(items):
    return items["num"]

def main():
    t=sys.argv[1]
    print(f"Analysing book found at {t}")
    b=get_book_text(t)
    print(f"Found {count_words(b)} total words")
    d=count_chars(b)
    dd=transform_dict(d)
    dd.sort(reverse=True, key=sort_on)
    for i in dd:
        print(f"{i['char']}: {i['num']}")

main()

