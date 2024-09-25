def word_frequency(text, top_n=None):
    words = text.lower().split()
    word_counts = {}
    for word in words:
        word_counts[word] = word_counts.get(word, 0) + 1
    sorted_word_counts = sorted(word_counts.items(), key=lambda x: x[1], reverse=True)
    print(f"Number of unique words: {len(word_counts)}")
    if top_n:
        print(f"Top {top_n} most common words:")
        for word, count in sorted_word_counts[:top_n]:
            print(f"{word}: {count}")

stanza1 = "It was many and many a year ago\nIn a kingdom by the sea\nThat a maiden there lived whom you may know\nBy the name of Annabel Lee\nAnd this maiden she lived with no other thought\nThan to love and be loved by me"
stanza2 = "I was a child and she was a child\nIn this kingdom by the sea\nBut we loved with a love that was more than love\nI and my Annabel Lee\nWith a love that the winged seraphs of Heaven\nCoveted her and me"

word_frequency(stanza1)
word_frequency(stanza2, top_n=5)

