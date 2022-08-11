import re 

def biggerIsGreater(word):
    #Error handler for symbols and numbers
    #Returns true if string doesn't contain symbol or number
    valid_word = re.findall(r'^[a-zA-Z]*$',word) 
    if not valid_word: return "Invalid Input"
    
    
    char_list = list(word)
    length_list = len(char_list) - 1
    # !Find the round defined index while checking the length of string is more than 0
    while length_list>0 and char_list[length_list - 1] >= char_list[length_list]:
        length_list -= 1
    #break when it reaches the minimal length
    if length_list <= 0:
        return "Not Arrangeable"
    
    # same algorithm as above but for finding the pivot to swap
    pivot_s = len(char_list) - 1
    while char_list[pivot_s] <= char_list[length_list - 1]: pivot_s -= 1
    
    #swap the pivot and next character
    char_list[length_list - 1], char_list[pivot_s] = char_list[pivot_s], char_list[length_list - 1]
    
    #Now reverse order the list of characters at the beginning of defined index
    char_list[length_list : ] = char_list[(len(char_list) - 1):(length_list - 1) : -1]
    word = "".join(char_list)
    return word
