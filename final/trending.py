import wordData

def trending(words: dict, startYr: str, endYr: str) -> list:
    """
    The function `trending` takes a dictionary of words with their counts over different years, and
    returns a list of words that have a count of at least 1000 in both the start and end years, sorted
    by the trend value of their counts.
    
    Author - Liam Scott
    Last update - 04/27/2024
    @param words (dict) - The `words` parameter is a dictionary where the keys are words and the values
    are dictionaries containing counts for each year.
    @param startYr (str) - The `startYr` parameter in the `trending` function represents the starting
    year for which you want to analyze the trend of words. It is a string parameter that specifies the
    year in which you want to start the trend analysis.
    @param endYr (str) - The `endYr` parameter in the `trending` function stands for the end year for
    which you want to analyze the trend of words. This parameter specifies the final year within the
    range for which you are checking the word counts.
    @returns The function `trending` returns a list of tuples where each tuple contains a word and its
    corresponding trend value. The list is sorted in descending order based on the trend values.
    
    """
    trending_list = []

    for word, counts in words.items():
        if startYr in counts and endYr in counts:
            if counts[startYr] >= 1000 and counts[endYr] >= 1000:
                start_count = counts[startYr]
                end_count = counts[endYr]
                trend_value = end_count / start_count
                trending_list.append((word, trend_value))
    trending_list.sort(key=lambda x: x[1], reverse=True)
    return trending_list

def top_printer(trendList: list):
    """
    The function `top_printer` prints the top 10 items from a list of trends along with their
    corresponding ranking.
    
    Author - Liam Scott
    Last update - 04/27/2024
    @param trendList () - It looks like the `top_printer` function is designed to print the top 10 items
    from a list of trends. The `trendList` parameter should be a list of tuples where each tuple
    contains a trend and its corresponding value.
    
    """
    for i in range(10):
        print(f"{i+1}. {trendList[i][0]}")

def bottom_printer(trendList: list):
    """
    The function `bottom_printer` prints the last 10 elements of a list of trends along with their
    corresponding index numbers.
    
    Author - Liam Scott
    Last update - 04/27/2024
    @param trendList () - It looks like the `bottom_printer` function is designed to print the bottom 10
    items from a list of trends. The function takes a list of trends as input and then prints the last
    10 items in reverse order.
    
    """
    for i in range(1, 11):
        print(f"{i}. {trendList[-i][0]}")

def main():
    """
    The main function reads words from a file, prompts the user for start and end years, calculates
    trending words within that range, and prints the top and bottom 10 trending words.
    
    Author - Liam Scott
    Last update - 04/27/2024
    
    """
    words_imput = input("Enter the name of the file containing the words: ")
    words = wordData.readWordFile(words_imput)
    startYr = int(input("Enter the start year: "))
    endYr = int(input("Enter the end year: "))
    trendList = trending(words, startYr, endYr)
    print(f"Top 10 trending words from {startYr} to {endYr} :")
    top_printer(trendList)
    print()
    print(f"Bottom 10 trending words from {startYr} to {endYr} :")
    bottom_printer(trendList)

# The `if __name__ == '__main__':` block in Python is a common idiom used to ensure that the code
# inside it is only executed if the script is run directly, and not imported as a module into another
# script.
if __name__ == '__main__':
    main()
