def list_of_words(words):
    """Print the length of the shortest, longest and average word length.

    Returns:
        [tuple]: (shortest word, longest word, average word length)
    """

    word_list_lengths = sorted([len(word) for word in words])
    print(f"Word list length: {word_list_lengths}")
    print(f"Shortest word: {min(word_list_lengths)}")
    print(f"Longest word: {max(word_list_lengths)}")
    return min(word_list_lengths), max(word_list_lengths), sum(word_list_lengths) / len(words)


print(
    list_of_words(["tree", "test", "was", "a", "to", "pleasant", "tumeric", "jalfrezi", "interesting"])
)
