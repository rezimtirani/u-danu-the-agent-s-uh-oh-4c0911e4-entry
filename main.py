"""The Agent's Uh-Oh.

Writes exactly one word to $MAKEFUN_OUTPUT_DIR/entry.txt: the word
an agent says when it has no idea what to do. Standard library only.
"""

import os

WORD = "Yikes!"


def check_word(text):
    """Check the word against the competition gate before writing.

    The gate needs plain UTF-8 text of at most 99 characters, in a
    single word: one word an agent says when it has no idea what to
    do, and nothing attached. Returns the cleaned text or raises
    ValueError.
    """
    cleaned = text.strip()
    if not cleaned:
        raise ValueError("word must not be only whitespace")
    if len(cleaned) > 99:
        raise ValueError(
            "word is %d characters, over the 99 limit" % len(cleaned)
        )
    if len(cleaned.split()) != 1:
        raise ValueError("entry must be exactly one word")
    return cleaned


def word_shape(text):
    """Measure the word for one last sanity pass.

    Returns a dict with the character count and the word count of
    the cleaned text. A word padded with a second word, or one so
    long it reads like a sentence instead of a yelp, is caught
    here before anything is written.
    """
    words = text.split()
    return {"chars": len(text), "words": len(words)}


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "output")
    os.makedirs(out_dir, exist_ok=True)
    text = check_word(WORD)
    shape = word_shape(text)
    if shape["words"] != 1:
        raise ValueError("entry must be exactly one word")
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as handle:
        handle.write(text)


if __name__ == "__main__":
    main()
