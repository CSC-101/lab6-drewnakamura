import data
from typing import Optional

# Write your functions for each part in the space below.

# Part 0

# Finds the index of the smallest value in the list, if there are values,
#     starting from the provided index (if in bounds).
# input: a list of integers
# input: a starting index
# returns: index of smallest value as an int or None if no value is found
def index_smallest_from(values:list[int], start:int) -> Optional[int]:
    if start >= len(values) or start < 0:
        return None

    mindex = start
    for idx in range(start + 1, len(values)):
        if values[idx] < values[mindex]:
            mindex = idx

    return mindex

def index_smallest_from_alphabet(values:list[str], start:int) -> Optional[int]:
    if start >= len(values) or start < 0:
        return None

    mindex = start
    for idx in range(start + 1, len(values)):
        if values[idx].title[0] < values[mindex].title[0]:
            mindex = idx

    return mindex


# Sorts, in place, the elements of a list using the selection sort algorithm.
# input: a list of integers
# returns: nothing is returned; the list is sorted in place
#    <This function modifies/mutates the input list. Though a traditional
#     approach, cloning the list sorting the clone is potentially less
#     surprising. Or even using a different sorting algorithm.>
def selection_sort(values:list[int]) -> None:
    for idx in range(len(values) - 1):
        mindex = index_smallest_from(values, idx)
        tmp = values[mindex]
        values[mindex] = values[idx]
        values[idx] = tmp


# Part 1
#The purpose of this function is to take a list of books and sort them alphabetically.
#values = list
#mindex = int
#tmp = int
#def selection_sort_books(values:list[data.Book]) -> list[data.Book]:
#return values
#book1 = data.Book("Drew", "Hello")
#book2 = data.Book("Drew", "Zoot")
#book3 = data.Book("Drew", "Banana")
#input = [book1, book2, book3]
#expected = [book3, book1, book2]
#selection_sort_books(input)
#expected
def selection_sort_books(values:list[data.Book]) -> list[data.Book]:
    for idx in range(len(values) - 1):
        mindex = index_smallest_from_alphabet(values, idx)
        tmp = values[mindex]
        values[mindex] = values[idx]
        values[idx] = tmp

    return values

# Part 2
#The purpose of this function is to swap all lowercase letter to uppercase, and vise versa.
#string = str
#lists = list
#def swap_case(string:str -> str:
#retirn string
#return ans
#swap_case("Hello")
#return = "hELLO"

def swap_case(string:str) -> str:
    lists = list(string)

    if(string.isalpha() == False):
        return string
    for num in range(len(lists)):
         if lists[num].isupper():
               lists[num] = lists[num].lower()
         else:
             lists[num] = lists[num].upper()
    ans = "".join(lists)
    return ans

# Part 3
#The purpose of this function is to take a 3 stroings, one main string, one string to replace, and one string to use in the replace.
#string = str
#old = str
#new = str
#newString = list
#def str_translate("Hello", "l", "x")
#return = "Hexxo"
def str_translate(string:str, old:str, new:str)->str:
    newString = []
    for num in range(len(string)):
        if(string[num] == old):
            newString.append(new)
        else:
            newString.append(string[num])
    newString = "".join(newString)

    return newString

# Part 4
#The purpose of this function is to create a dictonary holding words used in an string and how many of each.
#input_str = str
#word_input_str.split  = {}
#def histogram("Hello my name is Drew"
#return {"Hello":1, "my": 1, "name": 1, "is":1, "Drew":1}
def histogram(input_str: str) -> dict:
    word_counts = {}
    words = input_str.split()
    for word in words:
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1
    return word_counts