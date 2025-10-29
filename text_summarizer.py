# text_summarizer.py
# Simple Text Summarizer using word frequency

from collections import Counter
import re

def summarize(text, num_sentences=3):
    # Split text into sentences
    sentences = re.split(r'(?<=[.!?]) +', text)

    # Clean and split words
    words = re.findall(r'\w+', text.lower())
    word_freq = Counter(words)

    # Score each sentence based on word frequency
    sentence_scores = {}
    for sent in sentences:
        for word in re.findall(r'\w+', sent.lower()):
            if word in word_freq:
                sentence_scores[sent] = sentence_scores.get(sent, 0) + word_freq[word]

    # Select top sentences
    summary = sorted(sentence_scores, key=sentence_scores.get, reverse=True)[:num_sentences]
    return ' '.join(summary)

if __name__ == "__main__":
    text = input("Enter text to summarize:\n")
    print("\nSummary:\n", summarize(text))