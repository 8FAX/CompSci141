import numpy as np
import wordData

def normalize_vector(vector: np.ndarray)-> np.ndarray:
    """
    The function `normalize_vector` takes a vector as input and returns the normalized version of the
    vector.
    
    Author - Liam Scott
    Last update - 04/27/2024
    @param vector () - The `normalize_vector` function takes a vector as input and normalizes it by
    dividing each element of the vector by its Euclidean norm. If the norm of the vector is 0, the
    function returns the original vector since dividing by zero is undefined.
    @returns The function `normalize_vector` returns the normalized vector if the norm of the input
    vector is not zero. If the norm is zero, it returns the input vector itself.
    
    """
    norm = np.linalg.norm(vector)
    if norm == 0:
        return vector
    return vector / norm

def compute_cosine_similarity(word_vector: np.ndarray , other_word_vectors: np.ndarray)-> np.ndarray:
    """
    The function `compute_cosine_similarity` calculates the cosine similarity between a given word
    vector and a set of other word vectors after normalizing them.
    
    Author - Liam Scott
    Last update - 04/27/2024
    @param word_vector () - The `word_vector` parameter is a vector representation of a single word,
    typically in the form of a numerical array that captures the semantic meaning of the word in a
    high-dimensional space. This vector is used to compute the cosine similarity with other word
    vectors.
    @param other_word_vectors () - It seems like you were about to provide more information about the
    `other_word_vectors` parameter but it got cut off. Could you please provide more details or clarify
    what you need help with regarding the `other_word_vectors` parameter?
    @returns The function `compute_cosine_similarity` returns an array of cosine similarities between
    the `word_vector` and each vector in the `other_word_vectors` array.
    
    """
    normalized_word_vector = normalize_vector(word_vector)
    normalized_other_word_vectors = np.apply_along_axis(normalize_vector, 1, other_word_vectors)
    similarities = np.dot(normalized_other_word_vectors, normalized_word_vector)
    return similarities

def topSimilar(words: dict, word: str)-> list:
    """
    The `topSimilar` function finds the most similar words to a given word based on cosine similarity,
    while the `create_word_count_array` function creates a numpy array of word counts over years from a
    dictionary of word data.
    
    Author - Liam Scott
    Last update - 04/27/2024
    @param words (dict) - The `words` parameter in the functions `topSimilar` and
    `create_word_count_array` is a dictionary that contains word data. Each key in the dictionary
    represents a word, and the corresponding value is another dictionary where the keys are years and
    the values are counts or frequencies of the word in that
    @param word (str) - The `word` parameter in the `topSimilar` function is the word for which you want
    to find the most similar words in the dataset. If the provided word is not found in the dataset, the
    function will return the provided word in a list.
    @returns The `topSimilar` function returns a list of up to 5 words that are most similar to the
    input word based on cosine similarity. The `create_word_count_array` function returns a numpy array
    containing word counts for each year and a list of years.
    
    """

    if word not in words:
        print(f"'{word}' not found in the word dataset.")
        return [word]

    word_vector = np.array(list(words[word].values()))
    other_word_vectors = []
    other_words = []

    for w, counts in words.items():
        if w != word:
            other_word_vectors.append(list(counts.values()))
            other_words.append(w)

    other_word_vectors = np.array(other_word_vectors)
    similarities = compute_cosine_similarity(word_vector, other_word_vectors)
    word_similarities = list(zip(other_words, similarities))
    word_similarities.sort(key=lambda x: x[1], reverse=True)
    top_similar_words = [word] + [w for w, _ in word_similarities[:4]]  # Include up to 5 words
    
    return top_similar_words

def create_word_count_array(words_data: dict)-> np.ndarray:
    """
    The function `create_word_count_array` takes a dictionary of word counts per year and returns a
    numpy array of word counts for each word across all years along with a list of years.
    
    Author - Liam Scott
    Last update - 04/27/2024
    @param words_data (dict) - A dictionary where the keys are words and the values are dictionaries
    mapping years to word counts.
    @returns The function `create_word_count_array` returns a numpy array `word_count_array` containing
    word counts for each word in the input `words_data` dictionary, as well as a list of years extracted
    from the input data.
    
    """

    years = sorted(set(year for counts in words_data.values() for year in counts.keys()))
    word_count_list = []

    for word, counts in words_data.items():
        word_counts = np.zeros(len(years))
        for i, year in enumerate(years):
            if year in counts:
                word_counts[i] = counts[year]

        word_count_list.append(word_counts)

    word_count_array = np.array(word_count_list)
    return word_count_array, years

def main():
    """
    This Python function reads words from a file, prompts the user to enter a word, finds similar words
    to the input word, and then prints the similar words.
    
    Author - Liam Scott
    Last update - 04/27/2024
    
    """
    input_file = input("Enter the name of the file containing the words: ")
    words = wordData.readWordFile(input_file)
    word = input("Enter a word to find similar words: ")
    similar_words = topSimilar(words, word)
    print(f"Words similar to '{word}':")
    for i, similar_word in enumerate(similar_words):
        print(f"{i+1}. {similar_word}")

# The `if __name__ == "__main__":` block in Python is a common idiom used to ensure that the code
# inside it is only executed if the script is run directly, and not imported as a module into another
# script.
if __name__ == "__main__":
    main()
