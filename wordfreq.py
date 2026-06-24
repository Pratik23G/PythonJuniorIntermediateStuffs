import argparse
import re
import sys
from collections import Counter
from typing import Iterator
WORD_RE = re.compile(r"[a-z\']+")
known_sets = {"the", "and", "to", "of", "a", "in", "you", "it", "for", "they"}

def words_in(path: str, min_length: int = 1, skip_word: set = set()) -> Iterator[str]:
    with open(path) as f:
        for line in f:
            for word in WORD_RE.findall(line.lower()):
                if len(word) >= min_length and word not in skip_word:
                    yield word

def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("path")
    parser.add_argument("--top", type=int, default=10)
    parser.add_argument("--min-length", type=int, default=1)
    parser.add_argument("--ignore-stopwords", action='store_true')
    args = parser.parse_args()
    if args.top <= 0:
        sys.stderr.write("--top must be positive integer\n")
        sys.exit(1)
    skip_step = known_sets if args.ignore_stopwords else set()
    counts = Counter(words_in(args.path, args.min_length, skip_step))
    for word, n in counts.most_common(args.top):
        print(f"{word:<20} {n:>5}")

if __name__ == "__main__":
    main()
