import wordData as wd
import matplotlib.pyplot as plt

dict_f = {}

def letterFreq(words: dict) -> str:
    """
    The function `letterFreq` takes a dictionary of words and calculates the frequency of each letter in
    the words, returning a formatted string of letters sorted by decreasing frequency.
    
    Author - Liam Scott
    Last update - 04/26/2024
    @param words (dict) - It looks like the code you provided is incomplete. Could you please provide
    the missing part of the code or clarify what you would like assistance with regarding the 'words'
    parameter?
    @returns The function `letterFreq` is returning the formatted string `freqString` if the script is
    not being run as the main program. If the script is being run as the main program, it will print the
    formatted string `freqString` and also call the `plot_formater` function to plot the frequency
    distribution of letters.
    
    """
    new_dict = {}
    for key in words:
        multi = wd.totalOccurrences(key, words)
        for letter in key:
            letter = letter.lower()
            if letter in new_dict:
                new_dict[letter] += multi
            else:
                new_dict[letter] = multi
    freqString = formater(new_dict)
    if __name__ == '__main__':
        print(f"Letters sorted by decreasing frequency: {freqString}")
        plot_formater(new_dict)
    else:
        return freqString

def formater(new_dict: dict) -> str:
    """
    The function `formater` takes a dictionary, sorts it based on values in descending order, and
    returns a string concatenating the keys.
    
    Author - Liam Scott
    Last update - 04/26/2024
    @param new_dict (dict) - The `new_dict` parameter is a dictionary that contains key-value pairs.
    @returns The function `formater` takes a dictionary as input, sorts it based on the values in
    descending order, and then returns a string that concatenates the keys of the sorted dictionary.
    
    """
    new_dict = sorted(new_dict.items(), key=lambda x: x[1], reverse=True)
    return  ''.join([x[0] for x in new_dict])

def plot_formater(new_dict: dict) -> list[list[str], list[int]]:
    """
    The function `plot_formater` takes a dictionary as input, ensures it contains all letters of the
    alphabet with a default value of 0, plots a bar graph of the letter frequencies, and returns lists
    of letters and their corresponding frequencies.
    
    Author - Liam Scott
    Last update - 04/26/2024
    @param new_dict (dict) - The function `plot_formater` takes a dictionary `new_dict` as input. This
    dictionary is used to generate a bar plot where the keys represent letters of the alphabet and the
    values represent the frequency of each letter.
    @returns The function `plot_formater` is returning a list containing two lists: `letter_list` and
    `number_list`. These lists contain the letters and corresponding numbers from the input dictionary
    `new_dict`. Additionally, a bar plot is displayed using `plt.bar` before returning the lists. If the
    function is not being run as the main program, it returns `None`.
    
    """
    if __name__ == '__main__':
        letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
        letter_list = []
        number_list = []
        for letter in letters:
            if letter not in new_dict:
                new_dict[letter] = 0
        for letter in letters:
            letter_list.append(letter)
            number_list.append(new_dict[letter])

        plt.bar(letter_list, number_list, color='skyblue')
        plt.show()
        return letter_list, number_list
    else:
        return None

def main():
    """
    The main function prompts the user to enter a file name, reads words from the file using a function
    called `readWordFile`, and then calculates the frequency of each letter in the words using a
    function called `letterFreq`.
    
    Author - Liam Scott
    Last update - 04/26/2024
    
    """
    input_file = input("Enter the name of the file: ")
    words = wd.readWordFile(input_file)
    letterFreq(words)

# The `if __name__ == '__main__':` block in Python is a common idiom used to check whether the current
# script is being run as the main program or if it is being imported as a module into another script.
if __name__ == '__main__':
    main()

