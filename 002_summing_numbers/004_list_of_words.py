def list_of_words(words):
    """Print the length of the longest, shortest and average word length.

    Returns:
        [tuple]: (longest word, shortest word, average word length)
    """

    word_list_lengths = sorted([len(word) for word in words])
    print(f"Word list length: {word_list_lengths}")
    print(f"Shortest word: {min(word_list_lengths)}")
    print(f"Longest word: {max(word_list_lengths)}")
    return max(word_list_lengths), min(word_list_lengths), sum(word_list_lengths) / len(words)


print(
    list_of_words(["tree", "test", "was", "a", "to", "pleasant", "tumeric", "jalfrezi", "interesting"])
)
