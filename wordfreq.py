import argparse
import re
from collections import Counter
from typing import Iterator
WORD_RE = re.compile(r"[a-z\']+")

def words_in(path: str, min_length: int = 1) -> Iterator[str]:
    with open(path) as f:
        for line in f:
            for word in WORD_RE.findall(line.lower()):
                if len(word) >= min_length:
                    yield word

def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("path")
    parser.add_argument("--top", type=int, default=10)
    parser.add_argument("--min-length", type=int, default=1)
    args = parser.parse_args()
    counts = Counter(words_in(args.path, args.min_length))
    for word, n in counts.most_common(args.top):
        print(f"{word:<20} {n:>5}")

if __name__ == "__main__":
    main()
