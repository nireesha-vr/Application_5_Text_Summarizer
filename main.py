import re
from collections import Counter

# Stop words
STOP_WORDS = {
    "the", "is", "a", "an", "and", "or", "of", "to", "in",
    "on", "for", "with", "this", "that", "are", "was", "were",
    "as", "at", "by", "it", "from", "be", "has", "have", "had",
    "he", "she", "they", "we", "you", "i", "his", "her", "their",
    "which", "who", "will", "can", "about", "into", "than"
}


def summarize_text(text, number_of_sentences=3):

    # Split text into sentences
    sentences = re.split(r'(?<=[.!?])\s+', text.strip())

    # Remove empty sentences
    sentences = [sentence for sentence in sentences if sentence]

    if len(sentences) <= number_of_sentences:
        return text

    # Find all words
    words = re.findall(r'\b[a-zA-Z]+\b', text.lower())

    # Remove stop words
    useful_words = [
        word for word in words
        if word not in STOP_WORDS
    ]

    # Count word frequency
    word_frequency = Counter(useful_words)

    # Calculate score for each sentence
    sentence_scores = {}

    for sentence in sentences:

        sentence_words = re.findall(
            r'\b[a-zA-Z]+\b',
            sentence.lower()
        )

        score = 0

        for word in sentence_words:
            if word in word_frequency:
                score += word_frequency[word]

        sentence_scores[sentence] = score

    # Select the highest-scoring sentences
    important_sentences = sorted(
        sentence_scores,
        key=sentence_scores.get,
        reverse=True
    )[:number_of_sentences]

    # Keep original sentence order
    summary = []

    for sentence in sentences:
        if sentence in important_sentences:
            summary.append(sentence)

    return " ".join(summary)


# -------------------------------
# MAIN PROGRAM
# -------------------------------

print("=" * 50)
print("             TEXT SUMMARIZER")
print("=" * 50)

print("\nEnter a paragraph.")
print("Type your complete paragraph and press Enter.\n")

text = input("Enter text: ")

if not text.strip():

    print("\nError: Please enter some text.")

else:

    summary = summarize_text(text, 3)

    print("\n" + "=" * 50)
    print("                 SUMMARY")
    print("=" * 50)

    print(summary)

    print("\n" + "=" * 50)
    print("Original sentences :", len(
        re.split(r'(?<=[.!?])\s+', text.strip())
    ))

    print("Summary sentences  :", len(
        re.split(r'(?<=[.!?])\s+', summary.strip())
    ))

    print("=" * 50)