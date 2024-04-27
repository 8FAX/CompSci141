import wordData as wd
import matplotlib.pyplot as plt

def printedWords(words: dict) -> list:
    year_counts = {}
    for sub_dict in words.values():
        for year, count in sub_dict.items():
            if year in year_counts:
                year_counts[year] += count
            else:
                year_counts[year] = count
    return sorted(year_counts.items())

def wordsForYear(year: int, yearList: list) -> int:
    left, right = 0, len(yearList) - 1
    while left <= right:
        mid = (left + right) // 2
        if yearList[mid][0] == year:
            return yearList[mid][1]
        elif yearList[mid][0] < year:
            left = mid + 1
        else:
            right = mid - 1
    return 0

def main():
    words = wd.readWordFile('z.txt')
    yearList = printedWords(words)
    year = int(input('Enter a year: '))
    print(f'Words in year {year}: {wordsForYear(year, yearList)}')

        # this is a wayyyyy better way to  plot and i will use this in the future
        # looking back at the code i wrote for the letterFreq.py
        # this is a much better way to plot the data
        # i had to jump through so many hoops to get the data in the right format :(
        
    plt.plot([x[0] for x in yearList], [x[1] for x in yearList])
    plt.show()

if __name__ == '__main__':
    main()


