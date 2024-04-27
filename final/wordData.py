def readWordFile(filename: str) -> dict:
    """
    The function `readWordFile` reads a word file, processes the data, and returns a dictionary with the
    processed information.
    
    Author - Liam Scott
    Last update - 04/26/2024
    @param filename (str) - The `filename` parameter in the `readWordFile` function is a string that
    represents the name of the file to be read. The function reads the contents of this file, processes
    the data, and returns a dictionary containing the processed information.
    @returns The function `readWordFile` is returning a processed dictionary containing word frequencies
    for each word read from the file specified by the input `filename`. The word frequencies are stored
    in a nested dictionary structure where the keys are words and the values are dictionaries containing
    years as keys and corresponding word counts as values. The returned dictionary has been processed
    using a function `post_process` before being returned.
    
    """
    result_dict = {}

    with open("data/"+filename, "r") as file:
        key = None
        sub_dict = {}

        for line in file:
            line = line.strip()
            if line.isalpha():
                if key is not None:
                    result_dict[key] = sub_dict
                key = line
                sub_dict = {}
            else:
                year, count = line.split(',')
                sub_dict[int(year)] = int(count)
        if key is not None:
            result_dict[key] = sub_dict
        prossed = post_process(result_dict)

    return prossed

def post_process(words: dict) -> dict:
    """
    This Python function post-processes a dictionary of words by filling in missing years with a value
    of 0 for each word.
    
    Author - Liam Scott
    Last update - 04/26/2024
    @param words (dict) - A dictionary where the keys are words and the values are dictionaries
    containing years as keys and some values associated with those years.
    @returns A dictionary containing the words as keys and a dictionary of years as keys and counts as
    values for each word. The years range from 1900 to 2024, with counts of 0 for any missing years in
    the original input dictionary.
    
    """
    result_dict = {}
    for word in words:
        sub_dict = words[word]
        new_sub_dict = {}
        for year in range(1900, 2009):
            if year not in sub_dict:
                new_sub_dict[year] = 0
            else:
                new_sub_dict[year] = sub_dict[year]
        result_dict[word] = new_sub_dict
    return result_dict

def totalOccurrences(word: str, words: dict) -> int:
    """
    The function `totalOccurrences` calculates the total occurrences of a specific word within a
    dictionary of words.
    
    Author - Liam Scott
    Last update - 04/26/2024
    @param word (str) - The `word` parameter is a string that represents the word for which you want to
    find the total occurrences in the `words` dictionary.
    @param words (dict) - The `totalOccurrences` function takes two parameters: `word`, which is a
    string representing the word to count occurrences for, and `words`, which is a dictionary where keys
    are words and values are dictionaries containing the count of each word in different contexts.
    @returns the total number of occurrences of the given word in the provided dictionary `words`. If
    the word is found in the dictionary, it calculates the total occurrences by summing up the values
    associated with the word in the dictionary. If the word is not found in the dictionary, it returns
    0.
    
    """
    if word in words:
        words_dict = words[word]
        while True:
            total = 0
            for key in words_dict:
                total += words_dict[key]
            return total
    else:
        return 0


def main():
    """
    The main function reads a word file, prompts the user to enter a word, calculates the total
    occurrences of that word in the file, and then prints the result.
    
    Author - Liam Scott
    Last update - 04/26/2024
    
    """
    input_file = input("Enter the name of the file: ")
    words = readWordFile(input_file)
    input_word = input("Enter a word: ")
    total = totalOccurrences(input_word, words)
    print(f"{input_word} appears {total} times in the file.")

# The `if __name__ == '__main__':` block in Python is used to check whether the current script is
# being run directly by the Python interpreter or if it is being imported as a module into another
# script.
if __name__ == '__main__':
    main()
